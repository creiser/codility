def fibonacciModulo(n, z):
  fib = [0] * (n + 2)
  fib[1] = 1
  for i in range(2, n + 1):
    fib[i] = fib[i - 1] + fib[i - 2]
    if fib[i] >= z:
      fib[i] -= z
  return fib

def solution(A, B):
	table = [[]] * 30
	for z in range(1, 31):
	  #print('z=' + str(z + 1))
	  table[z - 1] = fibonacciModulo(30000, 2 ** z)
	  #print(table[z])

	res = [0] * len(A)
	for i in range(len(A)):
		res[i] = table[B[i] - 1][(A[i] + 1)]
	return res