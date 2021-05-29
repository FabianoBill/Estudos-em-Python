def primo(n):
    f = n - 1
    while n % f != 0:
        while f > 1:
            if n % f == 0:
                return False
            f -= 1
    return True
