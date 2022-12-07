

def addMatriceCarre(n):
    matrice = None
    for i in range (n):
        for j in range (n):
            matrice[i][j] = float(input(f"L{i}, C{j}: "))


addMatriceCarre(2)