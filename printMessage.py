def printMessage(message, version):
    """Prints the given message or the current version based on the 'version' flag."""
    assert isinstance(message, str), "'message' must be a string (type:str)."
    if version:
        print("Current version: alpha 0.1.0")
    else:
        print(message)