def solution(digits):  

	digits = list(digits)
	
	= formula(digits, 5)

	

# '123456', '5'
def formula(digits, count_digits)

	max_count = digits.count(max(digits))

	if max_count < count_digits:

		count_digits -= max_count

		digits = [x for x in digits if x != max(digits)] 

		return digits, count_digits, max_count

		

  	print digits

solution('123456')