from users_module import user_input


def my_max(a: int, b: int, c: int) -> int:
    return max((a + b, b + c, c + a))


print(my_max(user_input('a'), user_input('b'), user_input('c')))
