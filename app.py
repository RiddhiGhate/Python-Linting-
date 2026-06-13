def greet(name):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string")
    return f"Hello, {name}!"


def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


if __name__ == "__main__":
    print(greet("World"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"4 is even: {is_even(4)}")
