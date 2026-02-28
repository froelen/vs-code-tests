def printMessage(message, version):
    assert isinstance(message, str), "'message' must be a string (type:str)."
    if version:
        print("Current version: 2026.02.28")
    else:
        print(message)