def palindromo(string):
    size = len(string)
    if size == 0:
        return False
    for i in range(0, size // 2):
        if string[i] != string[size - i - 1]:
            return False
    return True

"""
Essa função verifica se uma string é palíndoma ou não.
"""

palindromo()
