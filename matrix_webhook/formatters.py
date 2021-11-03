"""Formatters for matrix webhook."""
from datetime import datetime


def grafana(data, headers):
    """Pretty-print a grafana notification."""
    text = ""
    if "title" in data:
        text = "#### " + data["title"] + "\n"
    if "message" in data:
        text = text + data["message"] + "\n\n"
    if "evalMatches" in data:
        for match in data["evalMatches"]:
            text = text + "* " + match["metric"] + ": " + str(match["value"]) + "\n"
    data["body"] = text
    return data


def github(data, headers):
    """Pretty-print a github notification."""
    # TODO: Write nice useful formatters. This is only an example.
    if headers["X-GitHub-Event"] == "push":
        pusher, ref, a, b, c = [
            data[k] for k in ["pusher", "ref", "after", "before", "compare"]
        ]
        pusher = f"[@{pusher['name']}](https://github.com/{pusher['name']})"
        data["body"] = f"{pusher} pushed on {ref}: [{b} → {a}]({c}):\n\n"
        for commit in data["commits"]:
            data["body"] += f"- [{commit['message']}]({commit['url']})\n"
    else:
        data["body"] = "notification from github"
    data["digest"] = headers["X-Hub-Signature-256"].replace("sha256=", "")
    return data


def pingdom(data, headers):
    """Pretty-print a pingdom notification."""
    #JSON data formatting was obtained from https://www.pingdom.com/resources/webhooks/
    check_id = data["check_id"]
    check_name = data["check_name"]
    current_state = data["current_state"]
    local_time = datetime.fromtimestamp(data["state_changed_timestamp"])

    if data["check_type"].lower() == "http":
        try:
            check_url = data["check_params"]["full_url"]
            data["body"] = (
                f"###{check_name} is {current_state}\n\n{check_url}"
                f" marked {current_state} at {local_time} ⚬ "
                f"[view details](https://my.pingdom.com/reports/responsetime#check={check_id})"
            )
        except Exception as error:
            data[
                "body"
                ] = (
                    f"Error: An attempt to post from pingdom was malformed "
                    "(or I don't know how to handle what was sent).\n\n"
                    f"{repr(error)}"
                )
    elif data["check_type"].lower() == "dns":
        # There are a bunch of values that are blanke when you do a test
        # so ignore them if value is unset
        try:
            first_ip = data["first_probe"]["ip"]
        except KeyError:
            first_ip = "unknown"
        try:
            second_ip = data["second_probe"]["ip"]
        except KeyError:
            second_ip = "unknown"
        try:
            first_location  = data["first_probe"]["location"]
        except:
            first_location = "unknown"
        try:
            second_location = data["second_probe"]["location"]
        except:
            second_location = "unknown"
        try:
            expected_ip = data["check_params"]["expected_ip"]
            data["body"] = (
                f"###{check_name} is {current_state}\n\n"
                f"expected {expected_ip} but got:\n\n"
                f"    {first_ip} ({first_location})\n\n"
                f"    {second_ip} ({second_location})\n\n"
                f" marked {current_state} at {local_time} ⚬ "
                f"[view details](https://my.pingdom.com/reports/responsetime#check={check_id})"
            )

        except Exception as error:
            print(error)

    return data
