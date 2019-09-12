#author: Zain Quraishi
#date: 08/05/2018
#description: Simple python script that allows the user to compute specific prime values or return a list of prime values given a search space.

import os

def new_prime_calculator(n):
	if (n < 2): return False;
	for i in range(2, int(math.sqrt(n)+1)):
		if n%i != 1:
			return false
	return True

#redundant function only adds returning primes in search space.
#function generates list of all primes within given range and returns list
def get_primes(ceiling):
	#generate list of candidate numbers
	candidate_list = []
	for i in range (2, ceiling + 1):
		candidate_list.append(i)
		#parse candidates for primes
	result = []
	j = 0
	while (j < len(candidate_list)):
		m = j
		while m < len(candidate_list):
			temp = candidate_list[m]
			index = candidate_list[j]
			if temp % index == 0 and temp != index:
				candidate_list.remove(temp)			
			m += 1
		j += 1
	return candidate_list

if __name__ == '__main__':
	clear = lambda: os.system('clear')
	
	print ("--- Selection Menu ---")
	
	#user can choose which operation to perform
	option = input ("(1) Compute primes in specified search space\n(2) Check if number is prime\nEnter Selection (1 or 2): ")	

	if (int(option) == 1):
		clear()
		print ("--- Check for Primes in Search Space (Max: 500) ---")
		limit = input ("Enter prime search space quantity: ")
		
		#check for legal input
		if int(limit) > 0 and int(limit) < 501:
			resulting_primes = get_primes(int(limit))
			print ("Resulting Primes ... \n" + str(resulting_primes))
		else:
			print ("Error! Invalid Input...")
	else:
		clear()
		print ("--- Check if a Number is Prime (Max: 1000) ---")
		check_number = input ("Enter Number : ")
		
		#check for legal input
		if int(check_number) < 1001 and int(check_number) > -1:
			verdict = get_primes(int(check_number))
			if int(check_number) in verdict:
				print (str(check_number) + " is PRIME")
			else:
				print (str(check_number) + " is NOT PRIME")
		else: 
			print("Error! Invalid Input...")
