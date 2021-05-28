def fatorial(n):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


print(fatorial(4))


def test_fatorial1():
    assert fatorial(1) == 1


def test_fatorial4():
    assert fatorial(4) == 24


def test_fatorial5():
    assert fatorial(5) == 120

