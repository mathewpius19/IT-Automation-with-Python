def validate_user(username, minlen):
    if minlen<3:
        raise ValueError("Value should be atleast 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True