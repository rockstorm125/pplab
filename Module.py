def fibo(count):
    out = [0, 1]
    counter = 0
    while counter != (count - 2):
        x = out[-1] + out[-2]
        out.append(x)
        counter += 1
    return (out)


def addition(x, y):
    return (x + y)
