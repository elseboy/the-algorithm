# Array

1. Two Sum:

   Use map to reduce one layer loop, if diff not exits in map, then add it to map, this can make sure duplicate elements like `[3, 3]` will not return `[0, 0]`.

2. Best time to but and sell stock:

   Assume the first element is min price, then loop the rest to compare, if it is smaller, then update min price to current, do minus if the current price is bigger than min price.

3. Contains Duplicate:

   Pass

4. Contains Duplicate II:

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

   Also use binary method, compare `arr[l] + arr[r]` with `target`, if smaller than `target`, this means `l` should be bigger and will get `bigger total` compare to the  `target`, `r` should be smaller otherwise, the overall time complexity is `O(n)`.

11. Three sum:

    Also use binary method, especially `two sum II` soluton, the first thing is sort array, then apply the `two sum II` solution, the only dfference is when `total == 0`, we have to remove duplicates on the both sides of `left` and `right` using while, if no duplicates, just simply move two points until they do not meet the condition of `l < r`, this means the current `i` only have these much triplets.

12. Container with most water:

    Pass

13. Next Permutation:

    First thing is to handle case like `[4, 3, 2, 1]`, the next smallest permutation is `1, 2, 3, 4`, so we have to check if the entire list is decending order from back to start, if it is, just `reverse list` is enough. Then, we have to start at the end of the list again to  comapre `nums[j]` smaller than `nums[i]` because we have to get `i` and `j` as close as possibale, so we can get smallest permutaion, which is next permutation. Once we get `i` and  `j`, we can simply just `swap` them and make sure the rest sub array is increasing order after `i` because we can make sure that this is smallest next permutation.

14. Remove Duplicates from Sorted Array:

    Only need to count the different element, like `[1, 1, 2, 2, 2, 3, 3]`, only increase times when it appears `nums[i] != nums[i + 1]`, the final times is the answer.

15. Find First and Last Position of Element in Sorted Array:

    Create two functions with binary search method to search the left most and right most, return the index of each index.

16. Trapping Rain Water:

    Assume `leftMax = l` and  `rightMax = r`, so the core soluton is how to move pointers, when `leftMax < rightMax`, we can shift `l` to `1` more position, and take the bigeest so far to minus `height[l]`, so there are only two possible outcomes, one is like use case `[1, 0, 2]`, `leftMax` will remain `1` when we shift `l` pointer to `0`, so we say there is only `1` water that we can trap. Another is where use case like `[1, 2, 3]`, the `leftMax` will update at the same time when we shift `l` pointer, so we say there is no water that we can trap because we are doing `maxLeft - height[l]`. Same thing for `rightMax`.

17. Kth Largest Element in an Array:

    Quick select would solve the problem, first set `pivot, pointer = nums[r], l`, then loop it and compare `nums[i] <= pivot`, if this is the case, then swap `nums[p], nums[i] = nums[i], nums[p]`, this can make sure on the left side are the elements that are smaller than `pivot` and right side are bigger elements, then swap `pivot, nums[p] = nums[p], pivot`, this will arrange the array to be a true  ` smaller | piovt | bigger` array, then comapre `k < p`, then call fuction again and pass `l, p - 1`, or `k > p`, then call function agagin and pass `p + 1, r`, or we found `k == p`, then simply just return `nums[p]`.

18. Sort an Array:

    Mark

19. Merge Sorted Array

    Set `p1, p2, p = m - 1, n - 1, m + n - 1`, then `if p2 >= 0` as `while` condition because we are going to midify `nums1`, in the loop, we also have to check `if p1 >= 0 and nums1[p1] > nums2[p2]` because if `nums1` shorter and `nums2` not done yet, `p1 >= 0`  will make sure it will copy the rest to the `nums1[p]`.

20. Merge Intervals

    So bascially we have to sort the sub list of list first, we can't make sure are they overlapping otherwsie. `list.sort(key=lambda i: i[0])`, then take out the first element, like `output = [list[0]]`, then loop the rest and take the last end  out `output[-1][1]`, if current `start <= lastEnd`, this means they are overlapping and we need update the `lastEnd` because we are not sure which end is bigger, so we do `output[-1][1] = max(lastEnd, end)`, else they are not overlapping, just append to `output`.

# Dynamic Programming

1. Climbing Stairs:

   The base case is when `n == 1` we will have only `1` step and if it is `n == 2` then we will have `2`. The core idea is when it comes to the next  `i`, we have to combine both cases, like `dp[i] = dp[i - 1] + dp[i - 2]`. Then `dp[n]` is the answer. 

2. Coin Change:

   Use `dp array` to track minimum from smaller to bigger `(bottom up)`, all we need is two loops, first one is coins loop and inner loop is i from coin to amount, take the `min(dp[i], dp[i - coin] + 1)`, and `dp[amount]` is the answer.

3. Coin Change II:

   Same as `coin change I` , also use `dp[0] * (amount  + 1)` to keep track, the only difference is in this question, we are counting the combinations, so inside of the inner loop, we do ` dp[i] += dp[i - coin] `.

4. Longest Increasing Subsequence:

   The main solution for this question is two loops, where `i` is backwards and `j` to loop the rest element after `i`, if `nums[i] < nums[j]`, this means it is increasing order from `i` to  `j` and we only take `max(dp[i], 1 + dp[j])`,  also, each element is considered as a subsequence, so we have to init `dp[1] * n`.

5. Longest Common Subsequence:

   The main solution is init a matrix where row is `m + 1` and column is `n + 1` so that we can get the answer from bottom-up easier. Then, two backwards loops will compare `text1[i]` and `text2[j]`, if they are same, it means that this is a subsequence, we have to set `dp[i][j] = 1 + dp[i + 1][j + 1]`, we create bigger matrix so this will not out of index, if they do not match, there is no common character at the current positions, so we need to make a decision, so `dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])`, we take the maximum of these two possibilities as we want to find the longest common subsequence, then, `dp[0][0]` is the answer. 

6. Word Break:

   So the first thing is to create a `dp[False] * len(s) + 1` and set `dp[len(s)]` to `True` because it is our base case, and then loop  `s` backwards and loop `dict` inside of the loop, the core is to check `i + len(w) <= len(s)` because use case like `aaaabbbb` and dict is `aaaa, bbbb`,  when we reach the last `b` (backwards), it will fit the length condition, otherwise, current string from `i` to end does not have `len(w)` this long, and add `s[i:i + len(w)] == w`, if they are the same, it means the current `i` plus `len(w)` can reach the end, where is our base case (True), we simply just set `dp[i] = dp[i + len(w)]`, then return `dp[0]`.

7. House Robber:

   So the basic recurrence relation is either we rob the current house or skip it to rob the next one, we have to compare which one is bigger because we are getting the max money that we can rob, so `dp[i] = max(dp[i−1], dp[i−2] + current house money)`.

8. House Robber II:

   Just simple exclusive the first element and last element, each time call the `House Robber I` solution, then return `max`.

9. Decode Ways:

   So basically there are only two ways that we can decode a input string of numbers. First create `dp = [0] * (n + 1)` the set `dp[0] = 1` because empty string only has one way to decode and set `dp[1] = 0 if s[0] == '0' else 1` because there is no match to the letters string starts at `0`. Then loop from `2, n + 1` and check single number first, if it is single number, it must fit `1 <= int(s[i  - 1]) <= 9` , if this is the case, we simply just  `dp[i] += dp[i - 1]`. another is two digits, `two_digits = int(s[ i - 2:1])`, then check `10 <= two_digits <= 26`, same as previous, we simply just add `dp[i] += dp[i - 2]`.

10. Unique Paths:

    Use bottom-up dp to set `dp[i][j] = dp[i + 1][j] + dp[i][j + 1]` because we can only mobe down or right, which means the edges of this martrix will be only 1, we are only computing `m - 2` and `n - 2` when looping backwards.

11. Pascal's Triangle:

    First init matrix `dp` to be rows by rows, then set `dp[0][0] = 1` because there is only `1` number in the first row, the loop the rest and to rows and set the start of each row to be `1` because this can be only `1`, then compute `j` from `1` to `i + 1`, set `dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]`, before `+` is the the previous row of  current  `i'` left, the right is `dp[i - 1][j]`, so plus them we can have result for  current `i` position.

12. Edit Distance

    Just like Unique paths problem, we also need `dp` with extra layers and set these layers to increaing order from bottom-up, then we loop backwards `i` as `m - 1, -1, -1` and `j` as `n - 1, -1, -1`, if `word1[i] == word2[j]`, then `dp[i][j] = diagonal`，else we have to find min operations, so `dp[i][j] = min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1]) + 1 `.

13. Minimum Path Sum:

    init matrix dp and set `dp[rows - 1][cols] = 0` and `dp[rows][cols - 1] = 0` because we are looking the right and down of the current value from bottom-up way, so `down = dp[r + 1][c]`, `right = dp[r][c + 1]`, then set `dp[r][c]`  to current  plus  the smaller one between right and down because we are computing the minimum, then return `dp[0][0]`.

14. Fibonacci Number: 

    Pass

# Greedy

1. Jump Game I

   The basic idea is that reverse check,  record last index of the array, and loop the rest from back to start to check the `nums[i]`  of current index to see how far we can go, which indicates that `i + nums[i]`, it means, if `i` is `2` and `nums[i]` is `4`, we can jump `4` more steps to reach index `6`, so the condition is `i + nums[i] >= r` , then set `r = i`, if reachable, `r` must be 0. 

2. Jump Game II

   First get the farthest, which is `farthest = max(farthest, i + nums[i])`, then when we reach this `farthest` index, lets say `curr_end`, when `i == curr_end`, we have to reset `curr_end` to the next `farthest` index that we can reach and increases `jumps += 1`. This way can ensure  minimum number of jumps.

# Backtrack

1. Subsets

   In `backtrack` function, first copy the current path to res, then compare `start == len(nums)`, if true, return to last loop, otherwise, make a loop, from `start, len(nums)`, in side of the loop, we have to make sure they are not duplicates, so we do `i > start and nums[i] == nums[i - 1]`, if so, just  `continue`, else, we append current i to path `append(nums[i])`, then call `backtrack(i + 1, path)`, and after that, we just  `pop` one unit from the path. Also, we have `sort()` array because this related to duplcates matter first.

2. Combination Sum

   The basic idea is also use `backtrack`, the only difference is we pass `backtrack(i, target - candidates[i], path)`, this will divide target into smaller. We also need to sort because this can avoiding duplicates.

3. Generate Parentheses

   So the basic idea is that use backtrack, and the `return` statment is when `len(s)` resches `n * 2` because we only can generate `() * n`, if this is true, we append `res` and return. the next thing is we have to set `l, r` to keep track how mang `(` `)` we have currently, so `if l < n` means we need to add more `(`, we call backtrack again: `backtrack(s + "(", l + 1, r)`, if `r < l` means we need more `)` to match the numbers of `(` in our s, so we call `s + ")", l, r + 1`.

4. Permutations

   It is the same as the previous solution, all we have to do is ensure that `nums[i] not in path` because this will create duplicates.

# String

1. Longest Substring Without Repeating Characters

   Use set to keep track chars, if found duplicates in set, we use `while` loop to remove it, use while loop because we might encounter issue like `bacab`, then we will have only `c` left, but res is still remained 3,  otherwise, the repeated har will still in set because we are removing char based on `s[count]`, so we have to use while,  then add to set `chars.add(nums[i])`, and update `res = max(res, i - count) + 1`.

2. Longest Palindromic Substring

   The idea is that middle out, define `expand` function to exapnd each index `i`, for exmple, `l - 1, r + 1`, and also we have to check`l >= 0 and r < len(s)` and `s[l] == s[r]` in th while statement, this will ensures that we are getting the longest palindromic index,  when `l - 1 == -1`, this means we can not expand anymore, so we return `l + 1, r - 1`. Then the main logic is loop each element and set `l1, r1 = expand(i , i)` for old number, `l2, r2 = exapnd(i, i + 1)` for the sapce between even numbers. Then check the length, `r1 - l1` or  `r2 - l2` greater than `end - start`, if so, update `start, end`, finally return `s[start:end + 1]`, this is the palindromic.

3. Add Strings

   Loop over both strings and start to do plus from the end, get single `x`, `y`, and set `total = x + y + carry`, then get `carry = total // 10` and `digit = total % 10`, then just insert it, like `res.insert(0, digit)`.

4. Reverse Words in a String

   The basic logic is that loop the string backwards, and set `end = len(s)`, then if `s[i] == " "`, this means last word is space, so we set `end = i` or `i == 0 or s[i - 1] == " "`, this ensures that we can check is current word finished, if so, we append like this: `if res: res.append(" ") res.append(s[i:end])`.  Then return `"".join(res)`.

5. Longest Common Prefix

   First find the shortest word in array, use this `prefix = min(strs, key=len)`, then loop its length and innner loop is `word in strs`, then check `if prefix[i] != word[i]`, this means we found the different, then just return `prefix[:i]`, otherwise return `prefix` because shortest is also a common prefix.

6. Group Anagrams

   First thing is create a map to stored them, loop them `for s in strs:`, then get sorted key, like this: `key = ''.join(sorted(s))`, so if `key` not in map, then set `map[key] = []`, if already exties in the map, then just append to the list, like this: `map[key].append(s)`, then return all the vlaues as list, like `return list(map.values())`.

   

# Linked List

1. Reverse Linked List I

   PASS

2. Reverse Linked List II

   PASS

3. Reverse Nodes in k-Group

   Mark

4. Merge Two Sorted Lists

   PASS

5. Linked List Cycle I

   PASS

6. Linked List Cycle II

   Two pointers, set `fast, slow = head, head`, then `while True:`, `fast, slow = fast.next.next, slow.next`, if there is a cycle, they will meet, then break it `if fast == slow: break`, and reset `fast`, start to loop and  check`while fast != slow`, if they are not equal, then move forward, like`fast = fast.next, slow = slow.next`, if they meet, just return `fast`, this is answer.

7. Intersection of Two Linked Lists

   PASS

8. Merge k Sorted Lists

   Use `Merge Two Sorted Lists` solution, and loop every two nodes from the array, and pass them tp `merge`, define an `array` to collect them, and pass it to `lists = next_level`, make sure `while len(lists) >  1` to run this code again until we have only one element in the `lists[0]`.

9. Reorder List

   First find middle, then reverse `mid.next`, then set `mid.next = None`, this will make us have 2 sub lists, then `merge(head, reversed)`.

10. Remove Nth Node From End of List

    Use two pointers, first create dummy node, and loop `n + 1` to set `fast` to ahead  `slow`, then `while fast` and move both `slow = slow.next` and `fast = fast.next`. Then set `slow.next = slow.next.next`, this means we accors the ith node.

11. Remove Duplicates from Sorted List I

    PASS

12. Remove Duplicates from Sorted List II

    First create dummy and set `prev = dummy`, then loop `head`, in side of this loop, we also have to check current node's and next node's value: `while head.next and head.val == head.next.val:`, if so, this means they are duplicated, we shift `head = head.next`, this will make sure head on the last duplicates, then check do we need to skip duplicates to connect, like `if prev.next = head:` if so, this means this is no duplicates, because we satrt at `head` and `prev` is always behide one step of `head`, so this means the current node is not the same as previous, if not, then we have to reconnect to head's next because the current head is still one of the duplicates and they told us to clean all the duplciates, so we set `prev.next = head.next`, then we have to shift `head = head.next`. Finally return `dummy.next.`

13. Sort List

    Use merge sort, first find middle, then sort left and right, then merge the results ffrom left and right.

14. Add Two Numbers

    Bascially, it is the same solution as `AddStrings` problem, create dummy node and set `curr = dummy`, then the loop condition is different, we have to make sure if there is only `l1` or `l2` or `carry` because there might be different length of nodes or carrys. so we do `while l1 or l2 or carray:`, then take `x` and  `y`, just like `AddStrings` problem, then we plus them: `x + y + carry`, and get  `carry = total // 10`, and we create new node, like `curr.next = ListNode(total % 10)`. Then move `l1`,`l2` pointers if they are not empty. and return `dummy.next`.

15. Palindrome Linked List (Space complexity O(1))

    First thing is find the middle, them reverse the `mid.next`, then compare `head.val != r.val`, this means they are not palindrome, make sure that we loop `while r:` not `head`. This takes O(1) space complexity.

# Tree

1. Binary Tree Level Order Traversal

   PASS

2. Binary Tree Inorder Traversal

   PASS

3. Binary Tree Preorder Traversal

   PASS

4. Binary Tree Postorder Traversal

   PASS

5. Lowest Common Ancestor of a Binary Tree

   Recursive to sovle.

6. Binary Tree Zigzag Level Order Traversal

   `True` and  `False` to control use `popleft` or `pop`.

7. Binary Tree Maximum Path Sum

   MARK

8. Binary Tree Right Side View

   Level Travel, take the `deque[-1].val`.

9. Maximum Depth of Binary Tree

   PASS

10. Balanced Binary Tree

    Use `dfs` to get `l_height` and `r_height`, then compare them `abs(l_height - r_height) > 1`, if this is true, it means it is not balanced.

11. Sum Root to Leaf Numbers

    So basically it is the same as level travel, but we need to append like this `queue.append((root, 0))`, this is to track current level sum, the only patteren is  `curr_sum = curr_sum * 10 + node.val`, and when `not node.left and not node.right`, this means the entire level is sum up, so we do  `total += curr_sum`, then move `left` `right` pointers.

12. Symmetric Tree

    Use `bfs`, first append `root.left` and `root.right`, then start to loop, then take `l` and `r` out of `queue`, if one of them is empty or `left.val != right.val`, then return False.

13. Validate Binary Search Tree

    Inorder travel, and set `prev = float('inf')` and  check  `temp.val <= prev:`, if this is true, then the tree is not valid.

14. Path Sum I

    Use dfs to solve, when reach left and right, like `if not node.left and not node.right:`, then `return curr_sum == target`.

# Stack

1. Valid Parentheses

   Use `stack` and `dic` to map the pairs, like this: `dic = {"{": "}", "[": "]", "(": ")"}`. Then loop check `c` in `s`.

2. Implement Queue using Stacks

   Two stacks trick.

3. Implement Stack using Queues

   Two deques to move elements.

4. Min Stack

   Two stacks trick, one is noremal save, another one always saves `min(val, min_stack[-1])`.

5. Longest Valid Parentheses

   First thing is init stack like `stack[-1]`, this way will ensure the correct sum, then use `enumerate` to loop, if `p == '('`, this we an append to `stack`,  we `pop` it otherwise, in `else`, we also have to check `stack` is empty or not, if it is `emoty`, then we append `index` again,  n `else` statment, we use `ma()` to get `i - stack[-1]`.

   

# Graph

1. Number of Islands

   ```python
       def numIslands(self, grid: List[List[str]]) -> int:
           rows, cols = len(grid), len(grid[0])
           visited = set()
           islands = 0
   
           def bfs(r , c):
               queue = deque()
               visited.add((r, c))
               queue.append((r, c))
   
               while queue:
                   row, col = queue.popleft()
                   directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
   
                   for dr, dc in directions:
                       r, c  = row + dr, col + dc
                       if (r in range(rows) and c in range(cols)
                           and grid[r][c] == '1' and (r, c) not in visited):
                           queue.append((r, c))
                           visited.add((r ,c))
                           
           for r in range(rows):
               for c in range(cols):
                   if grid[r][c] == "1" and (r ,c) not in visited:
                       bfs(r ,c )
                       islands += 1
           
           return islands
   ```

   

2. Spiral Matrix

   ```python
   def spiralOrder(matrix):
       l, r = 0, len(matrix[0])
       t, b = 0, len(matrix)
       res = []
   
       while l < r and t < b:
           for i in range(l, r):
               res.append(matrix[t][i])
           t += 1
   
           for i in range(t, b):
               res.append(matrix[i][r - 1])
           r -= 1
   
           if not (l < r and t < b):
               break
   
           for i in range(r - 1, l - 1, -1):
               res.append(matrix[b - 1][i])
           b -= 1
   
           for i in range(b - 1, t - 1, -1):
               res.append(matrix[i][l])
           l += 1
   
       return res
   ```

   

3. Rotate Image

   ```python
           l, r = 0, len(matrix[0]) - 1
   
           while l < r:
               for i in range(r - l):
                   top, bottom = l , r
   
                   topLeft = matrix[top][l + i]
   
                   matrix[top][l + i] = matrix[bottom - i][l]
   
                   matrix[bottom - i][l] = matrix[bottom][r - i]
   
                   matrix[bottom][r - i] = matrix[top + i][r]
   
                   matrix[top + i][r] = topLeft
               
               r -= 1
               l += 1
   ```

   

4. Search a 2D Matrix II

   Use Binary search

# Sliding Window

1. Sliding Window Maximum

   MARK

# Others

1. LRU Cache

2. Meeting Room 1

   Overlapping problem.

3. Meeting Room II

   Find overlapped tuples. Sort tuple's start and end, put them in different list, then compare, like `if start[i] < end[j]:` this means there is a meeting, we do `count += 1` and `i + 1`, else statement is `count -= 1` and `j += 1`, we have to keep our result like this `res = max(res, count)`.