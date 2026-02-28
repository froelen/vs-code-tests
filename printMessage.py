def printMessage(message, version):
    assert isinstance(message, str), "'message' must be a string (type:str)."
    if version:
        print("Current version: alpha 0.1.0")
    else:
        print(message)