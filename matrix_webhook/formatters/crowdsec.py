def formatter(data, headers):
    """format a message sent with crowdsec http endpoints"""
    data_out = ""
    for row in data["body"]:
        if "crowdsecurity" in row["scenario"]:
            source, scenario, *_ = row["scenario"].split("/")
            row[
                "scenario"
            ] = f"[{scenario}](https://hub.crowdsec.net/author/crowdsecurity/configurations/{scenario})"
        data_out += (
            f"{row['host']} has been banned {row['duration']} due to {row['scenario']}\n\n"
            f"[AbuseIPDB](https://www.abuseipdb.com/check/{row['host']})|"
            f"[Crowdsec](https://app.crowdsec.net/cti/{row['host']})\n\n"
        )
    data["body"] = data_out
    return data
