import requests


def get_abuse_confidence(ip):
    """get abuseipdb's confidence level on an ip passed in, and return that value"""
    base_url = "https://api.abuseipdb.com/api/v2/check"
    api_key = "YOUR API KEY"
    headers = {"Key": api_key, "Accept": "application/json"}
    data = {"ipAddress": ip, "maxAgeInDays": 90}
    r = requests.get(base_url, headers=headers, json=data)
    confidence = r.json()["data"]["abuseConfidenceScore"]
    whitelist = r.json()["data"]["isWhitelisted"]
    return [confidence, whitelist]


def formatter(data, headers):
    """format a message sent with crowdsec http endpoints"""
    data_out = ""
    for row in data["body"]:
        ip = row["host"]
        duration = row["duration"]
        confidence, whitelisted = get_abuse_confidence(ip)
        if "crowdsecurity" in row["scenario"]:
            source, scenario, *_ = row["scenario"].split("/")
            row[
                "scenario"
            ] = f"[{scenario}](https://hub.crowdsec.net/author/crowdsecurity/configurations/{scenario})"
        data_out += f"{ip} has been banned {duration} due to {row['scenario']}\n\n"
        if whitelisted:
            data_out += "**Note: AbuseIPDB has whitelisted this address\n\n"
        data_out += (
            f"[AbuseIPDB](https://www.abuseipdb.com/check/{row['host']})({confidence}%) | "
            f"[Crowdsec](https://app.crowdsec.net/cti/{row['host']})\n\n"
        )
    data["body"] = data_out
    return data
