from uuid import uuid4


def uuid():
    return uuid4().int & (1 << 63) - 1
