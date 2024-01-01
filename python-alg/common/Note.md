# Array

1. Two Sum:

   Use map to reduce one layer loop, if diff not exits in map, then add it to map, this can make sure duplicate elements like `[3, 3]` will not return `[0, 0]`.

2. Best time to but and sell stock:

   Assume the first element is min price, then loop the rest to compare, if it is smaller, then update min price to current, do minus if the current price is bigger than min price.

3. Contains Duplicate:

   Pass

4. Contains Duplicate:

   Use a map to map the num and its' index, then check if it is duplicated in the map and its' index minus duplicate to make sure it is  smaller than k.

5. Product of Array Except Self:

   Create two arrays to compute the prefix and postfix, like `[1, 2, 3, 4]`, prefix is `[1, 2, 6, 24]`, postfix is `[24, 24, 12, 4]`, then the result is `prefix[i - 1]` times `postfix[i + 1]`, for element `2`, its prefix is 1, postfix is 12, nums[1] should be `1 * 12`, which is 12.

6. Maximum Subarray:

   Assume the maximum sum starts with the first element. Continue adding elements to the current sum. If the current sum becomes smaller than `0`, reset it to `0`. This indicates that the previous elements do not contribute to the maximum sum, and the next element will be the start of the subarray and continue to do it. Then compare the maximum sum and current sum through `max()`.

7. Maximum Product Subarray:

   To find the maximum product of a subarray, create two dynamic programming arrays (`max_dp` and `min_dp`) to track the maximum and minimum products ending at each index. Iterate through the array, updating both arrays, and return the maximum product encountered.

8. Find Minimum in Rotated Sorted Array:

   Use binary method to see if mid elem is bigger than r elem, if it is, it means the array is rotated and we can move `l` to `mid + 1`, of is not, then we set r  = `mid` not `mid - 1` because this would miss the min value, like `[3, 1, 2]`, it will return 3 not 1. So the final min value should be `nums[l]`.

9. Search in Rotated Sorted Array:

   Similarly, as the last question, we can also use binary method to solve this problem, the core problem is in `if nums[mid] > nums[r]:` statment, we have to determine wether go left half or go right half, so if  `nums[mid] > target >= nums[l]`, this means target is in somewhere in this array from `left to mid`, then we have to set `r = mid - 1 else l = mid + 1`, also in else case of  `nums[mid] > nums[r]`, we have to check if  `nums[mid] < target <= nums[r]`, this means we have go through this part to find target index, so we set `l = mid + 1 else r = mid - 1`.

10. Two sum II:

   Also use binary method, compare `arr[l] + arr[r]` with `target`, if smaller than `target`, this means `l` should be bigger and will get `bigger total` compare to `target`, `r` should be smaller otherwise, the overall time complexity is `O(n)`.

