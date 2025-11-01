def oscillate():
    result = []
    for i in range(-3, 5):  # từ -3 đến 4
        result.append(i)
        result.append(-i)
    print(' '.join(str(x) for x in result))

oscillate()