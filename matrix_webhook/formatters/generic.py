def formatter(data, headers):
    """Just dump the json data"""
    data["body"] = f"{data}"
    return data
