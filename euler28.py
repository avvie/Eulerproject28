
diag1 = 0
diag2 = 1
lastNumber = 1
flip = False
for i in range(2, 1002,2):
    for j in range(1,5):
        if not flip:
            lastNumber = lastNumber + i
            diag1 = diag1 + lastNumber
            flip = not flip
        else:
            lastNumber = lastNumber + i
            diag2 = diag2 + lastNumber
            flip = not flip


print("sum " + str(diag1 + diag2))
