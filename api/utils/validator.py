from re import compile, match, search


def email_valid(value):
    if not isinstance(value, str):
        return False
    return match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$', value)


def password_valid(value):
    regex = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$'
    pattern = compile(regex)
    return search(pattern, value)
