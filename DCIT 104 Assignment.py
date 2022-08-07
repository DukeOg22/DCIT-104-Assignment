MAX = 10000
print("Input any number less or equal to 10000:")
is_prime = [True for _ in range(MAX)]
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX ** (1 / 2)) + 1):
  if is_prime[i]:
    for j in range(i ** 2, MAX, i):
      is_prime[j] = False
primes = [i for i in range(MAX) if is_prime[i]]
while True:
  p = int(input())
  Average = sum(primes[:p]) / p
  if not p:
    break
  print("Sum of first",p,"prime numbers:")
  print(sum(primes[:p]))
  print("Average of the sum of",p,"prime numbers:")
  print(Average)
