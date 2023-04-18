def foo(n: int):
    if n >= 2025:
        return n
    else:
        return n + foo(n + 2)


print(foo(2022) - foo(2023))
