def primo(num):
    import math
    x = math.ceil(num)
    y = math.floor(num)
    cond_up = num/2
    divisor = 2
    sim = 0
    if num == 1:
        return "N�o"
    if num < 0:
        return "N�o"
    if num == 0:
        return "N�o"
    if x != y:
        return "N�o"
    while divisor <= cond_up:
        if num % divisor == 0:
            return "N�o"
        else:
            divisor += 1
            sim = sim + 1
    if sim > cond_up - 2:
        return "Sim"