def is_prime(n): 
  mult = 0
  for count in range(2,n):
    if (n % count == 0):
      mult += 1
      
  if (mult == 0):
      return True
  else:
      return False

"""
Essa função verifica se um número é primo ou não é.
"""

is_prime()
