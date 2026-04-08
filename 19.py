import numpy as np
import sys

def log_10(x):
	return np.log_10(x)

def print_log10(n):
	#range(n) -> [0, 1, 2, 3,...n-1]
	for i in range(n):
		pring(log_10(i))

def main():
	n = 10 #default value of n

	if len(sys.argv) > 1:
		n = int(sys.argv[1])

	print_log10(n) #calling my print function


if__name__ == '__main__':
	main()