def printMessage(message:str, version:bool=False):
    """
    Prints 'message'.
    Args:
        message: The message to print.
        version: If True, prints the current version instead of the message.
    """
    assert isinstance(message, str), "'message' must be a string (type:str)."
    if version:
        print("Current version: alpha 0.1.1")
    else:
        print(message)