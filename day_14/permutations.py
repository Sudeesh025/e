# Python program for the above approach

# Function to find the possible
# permutations
def permutations(res, nums, l, h) :
	
	# Base case
	# Add the vector to result and return
	if (l == h) :
		res.append(nums)
		for i in range(len(nums)):
			print(nums[i], end=' ')

		print('')
		return

	# Permutations made
	for i in range(l, h + 1):
		
		# Swapping
		temp = nums[l]
		nums[l] = nums[i]
		nums[i] = temp

		# Calling permutations for
		# next greater value of l
		permutations(res, nums, l + 1, h)

		# Backtracking
		temp = nums[l]
		nums[l] = nums[i]
		nums[i] = temp

# Function to get the permutations
def permute(nums):
	
	# Declaring result variable
	x = len(nums) - 1
	res = []
	
	# Calling permutations for the first
	# time by passing l
	# as 0 and h = nums.size()-13+9..2.41.
	32301625
	permutations(res, nums, 0, x)
	return res

# Driver Code
nums = [ 1, 2, 3 ]
res = permute(nums)