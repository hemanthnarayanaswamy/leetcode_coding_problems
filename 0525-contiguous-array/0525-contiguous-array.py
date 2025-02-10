class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_track = {0: -1} ## {prefix_sum: irst occurance of prefix sum detected}
        prefix_sum = 0 ## To keep TRack of prefix sum 
        max_subarray_length = 0 ## Keeping track of subarray length whenever we detect the prefix sum again

        nums_length = len(nums)
## we are checking if the number of zeros are equal to number of ones if half of the length of the array is equal to sum of the array then we can return the length of the array
        if nums_length/2 == sum(nums): 
                return nums_length

        for i in range(nums_length):
            prefix_sum += 1 if nums[i] == 1 else -1

            if prefix_sum not in sum_track:
                sum_track[prefix_sum] = i
            else: 
                first_occurence = sum_track[prefix_sum]
                if max_subarray_length < i - first_occurence:
                    max_subarray_length =  i - first_occurence
        
        return max_subarray_length

        