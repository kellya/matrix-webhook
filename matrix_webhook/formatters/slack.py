def formatter(data, headers):
    """ format a message sent with slack api endpoints"""
    text = data["attachments"][0]["text"]
    data["body"] = f"{text}"
    return data
