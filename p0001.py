"""
@author		Tee Kai Yoong
"""
def main():
	"""Return the sum of all the multiples of 3 or 5 below 1000."""
	sum = 0
	count = 1
	while count < 1000:
		if count % 3 == 0 or count % 5 == 0:
			sum += count
		count += 1
	
	return sum

if __name__ == "__main__":
	main()