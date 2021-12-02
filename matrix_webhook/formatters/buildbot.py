from datetime import datetime


def formatter(data, headers):
    """Pretty-print a buildbot notification."""
    buildid = data["buildid"]
    buildstate = data["state_string"]
    buildlink = data["url"]
    reason = data["buildset"]["reason"]
    project = data["properties"]["project"][0]
    submittime = datetime.fromtimestamp(data["buildset"]["submitted_at"])
    if buildstate == "starting":
        try:
            data["body"] = (
                f"###Buildbot job #{buildid} for {project} - {buildstate}\n\n"
                f"{reason}\n\n"
                f"**started at** {submittime}\n\n"
                f"[view details]({buildlink})"
            )
        except Exception as error:
            print(error)
    elif buildstate == "build successful":
        try:
            data["body"] = (
                f"###Buildbot job #{buildid} for {project} - {buildstate}\n\n"
                f"**completed at** {datetime.fromtimestamp(data['complete_at'])}\n\n"
                f"[view details]({buildlink})"
            )
        except Exception as error:
            print(error)

    return data
