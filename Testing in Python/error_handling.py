def validate_user(username, minlen):
    assert type(username) == str, "Username must be a string"
    if minlen<1:
        raise ValueError("Value should be atleast 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True
