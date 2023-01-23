
def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res


print(concatenatio('1', '2', '3', '4')) # TypeError: ...