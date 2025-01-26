
def is_prime(num):
  y = 2
  prime = True
  while(y < num):      
    if (num % y) == 0:
      prime = False
      break
    y = y+1

  if (prime == True):
    print(num, " is prime")

#is_prime(9)

def get_primes(num):
  for i in range(2, num):
    is_prime(i)

#get_primes(100)

def get_prime_factors(n):
  list = []
  i = 2
  remain = n
  while(remain > 2):
    if remain%i == 0:
      list.append(i)
      remain = remain // i
    else:
      i = i + 1
  #   print(remain)
  #   print(i)
  print(list)

get_prime_factors(630)
