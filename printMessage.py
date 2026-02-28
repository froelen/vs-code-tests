<<<<<<< HEAD
def printMessage(message, version):
    """Prints the given message or the current version based on the 'version' flag."""
=======
def printMessage(message:str, version:bool=False):
    """
    Prints 'message'.
    Args:
        message: The message to print.
        version: If True, prints the current version instead of the message.
    """
>>>>>>> testCodeLens
    assert isinstance(message, str), "'message' must be a string (type:str)."
    if version:
        print("Current version: alpha 0.1.1")
    else:
        print(message)