def printGfg(n):
    if n == 0:
        return
    printGfg(n - 1)
    print("GFG", end=" ")


printGfg(40)
