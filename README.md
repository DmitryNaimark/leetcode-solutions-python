# LeetCode Solutions (Python)
This repository contains solutions for LeetCode problems I've solved(using Python), links to official(and clever unofficial) solutions.  
  
Solutions are grouped by Topics(see `topics` folder).  

Feel free to Fork, Clone or Star this repository.  

Also, check out [my JavaScript Repository](https://github.com/DmitryNaimark/leetcode-solutions), which contains JS solutions for all problems below and a lot more.
<br />

| Difficulty | Title | Tags | My Solutions | LeetCode Solution | Other cool solutions | Solved on my own? | Date |
|:----------:|-------|------|:------------:|:-----------------:|:--------------------:|:-----------------:|:----:|
| ![][easy] | [1. Two Sum](https://leetcode.com/problems/two-sum/description/) | `HashTable`, `Array` | [![](./images/solution.png)](topics/HashTable/Two_Sum_1/Two_Sum_1.py) | [![](./images/solution.png)](https://leetcode.com/problems/two-sum/solution/) |  | Simple HashTable | `2019-10-15`
| ![][easy] | [276. Paint Fence](https://leetcode.com/problems/paint-fence/description/) | `DP`, `Probability`, `Math` | [![](./images/solution.png)](topics/DynamicProgramming/Paint_Fence_276/Paint_Fence_276.py) | - | 1) [Decent explanation](https://leetcode.com/problems/paint-fence/discuss/71156/O(n)-time-java-solution-O(1)-space) | Probability, DP | `2019-10-16`
| ![][easy] | [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/description/) | `Stack`, `Monotonic Stack`, `deque` | [![](./images/solution.png)](topics/Stack/Next_Greater_Element_I_496/Next_Greater_Element_I_496.py) | [![](./images/solution.png)](https://leetcode.com/problems/next-greater-element-i/solution/) |  | Monotonic Stack | `2019-10-17`
| ![][easy] | [1232. Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/description/) | `Geometry`, `Math` | [![](./images/solution.png)](topics/Geometry/Check_If_It_Is_a_Straight_Line_1232/[Check_rect_area]_Check_If_It_Is_a_Straight_Line_1232.py) [![](./images/solution.png)](topics/Geometry/Check_If_It_Is_a_Straight_Line_1232/[Check_slopes]_Check_If_It_Is_a_Straight_Line_1232.py) [![](./images/solution.png)](topics/Geometry/Check_If_It_Is_a_Straight_Line_1232/[Check_slopes_using_all]_Check_If_It_Is_a_Straight_Line_1232.py) | - | 1) [Check slopes, Python "all"](https://leetcode.com/problems/check-if-it-is-a-straight-line/discuss/408984/JavaPython-3-check-slopes-short-code-w-explanation-and-analysis.), <br><br>2) [Is Triangle area == 0](https://leetcode.com/problems/check-if-it-is-a-straight-line/discuss/408968/Check-collinearity) | Formulas: Slopes, Triangle area | `2019-10-21`
| ![][medium] | [1233. Remove Sub-Folders from the Filesystem](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/) | `String`, `Substring`, `HashSet`, `Sorting` | [![](./images/solution.png)](topics/String/Remove_Sub-Folders_from_the_Filesystem_1233/[Sort_by_length_use_seen_set]_Remove_Sub-Folders_from_the_Filesystem_1233.py) [![](./images/solution.png)](topics/String/Remove_Sub-Folders_from_the_Filesystem_1233/[Sort_lexicogr_check_previous]_Remove_Sub-Folders_from_the_Filesystem_1233.py) | - | 1) [1. Sort by length -> use HashSet 2. Sort lexic. -> compare only with previous potentian parent](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/discuss/409028/JavaPython-3-2-simple-methods-check-parent-w-brief-explanation-and-analysis.) | Difficult time/space estim., interesting solutions | `2019-10-22`
| ![][easy] | [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/description/) | `Stack`, `Queue` | [![](./images/solution.png)](topics/Stack/Implement_Queue_using_Stacks_232/[Better_Two_stacks_one_reversed]_Implement_Queue_using_Stacks_232.py) [![](./images/solution.png)](topics/Stack/Implement_Queue_using_Stacks_232/[Slower_One_stack_pop_O_N]_Implement_Queue_using_Stacks_232.py) | [![](./images/solution.png)](https://leetcode.com/problems/implement-queue-using-stacks/solution/) |  | 2 Stacks(1 reversed) to get amortized O(1) pop | `2019-10-22`
| ![][easy] | [674. Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/) | `Array`, `Subseq.` | [![](./images/solution.png)](topics/Array/Longest_Continuous_Increasing_Subsequence_674/Longest_Continuous_Increasing_Subsequence_674.py) [![](./images/solution.png)](topics/Array/Longest_Continuous_Increasing_Subsequence_674/[Moving_anchor]_Longest_Continuous_Increasing_Subsequence_674.py) | - |  | Anchor technique, Sliding Window | `2019-10-22`
| ![][medium] | [120. Triangle](https://leetcode.com/problems/triangle/description/) | `DP`, `Bottom-Up DP` | [![](./images/solution.png)](topics/DynamicProgramming/Triangle_120/[DP_Space_O(N)]_Triangle_120.py) [![](./images/solution.png)](topics/DynamicProgramming/Triangle_120/[In_place]_Triangle_120.py) | - | 1) [Bottom-up explanation](https://leetcode.com/problems/triangle/discuss/38730/DP-Solution-for-Triangle) | DP Bottom-up, In-place | `2019-10-24`
| ![][easy] | [1022. Sum of Root To Leaf Binary Numbers](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/) | `Tree`, `Recursive`, `Iterative`, `Stack` | [![](./images/solution.png)](topics/Tree/Sum_of_Root_To_Leaf_Binary_Numbers_1022/[Iterative_DFS_stack_with_2_values]_Sum_of_Root_To_Leaf_Binary_Numbers_1022.py) [![](./images/solution.png)](topics/Tree/Sum_of_Root_To_Leaf_Binary_Numbers_1022/[Iterative_DFS_stack_with_tuple]_Sum_of_Root_To_Leaf_Binary_Numbers_1022.py) [![](./images/solution.png)](topics/Tree/Sum_of_Root_To_Leaf_Binary_Numbers_1022/[Recursive_DFS]_Sum_of_Root_To_Leaf_Binary_Numbers_1022.py) | - |  | Stack with Tuple or 2 values, Iterative DFS | `2019-10-24`
| ![][medium] | [129. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/description/) | `Tree`, `Recursive`, `Iterative`, `Stack` | [![](./images/solution.png)](topics/Tree/Sum_Root_to_Leaf_Numbers_129/[Iterative_DFS_stack_with_tuple]_Sum_Root_to_Leaf_Numbers_129.py) [![](./images/solution.png)](topics/Tree/Sum_Root_to_Leaf_Numbers_129/[Recursive_DFS]_Sum_Root_to_Leaf_Numbers_129.py) | - |  | Same as #1022 | `2019-10-24`
| ![][hard] | [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/) | `Tree`, `Path`, `nonlocal`, `Recursive` | [![](./images/solution.png)](topics/Tree/Binary_Tree_Maximum_Path_Sum_124/[Using_nonlocal_Python_keyword]_Binary_Tree_Maximum_Path_Sum_124.py) [![](./images/solution.png)](topics/Tree/Binary_Tree_Maximum_Path_Sum_124/[Using_self_variable]_Binary_Tree_Maximum_Path_Sum_124.py) [![](./images/solution.png)](topics/Tree/Binary_Tree_Maximum_Path_Sum_124/[Using_shared_object]_Binary_Tree_Maximum_Path_Sum_124.py) | [![](./images/solution.png)](https://leetcode.com/problems/binary-tree-maximum-path-sum/solution/) |  | Max gain idea: left_sum = max(left_sum, 0), to shorten code | `2019-10-25`
| ![][medium] | [1171. Remove Zero Sum Consecutive Nodes from Linked List](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/) | `LinkedList`, `HashTable`, `Prefix Sum`, `Delete` | [![](./images/solution.png)](topics/LinkedList/Remove_Zero_Sum_Consecutive_Nodes_from_Linked_List_1171/[HashTable_delete_continuous_sublists]_Remove_Zero_Sum_Consecutive_Nodes_from_Linked_List_1171.py) [![](./images/solution.png)](topics/LinkedList/Remove_Zero_Sum_Consecutive_Nodes_from_Linked_List_1171/[HashTable_Smart_two_pass]_Remove_Zero_Sum_Consecutive_Nodes_from_Linked_List_1171.py) | - | 1) [Smart two-pass solution (last)](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/discuss/366319/JavaC%2B%2BPython-Greedily-Skip-with-HashMap), <br><br>2) [Explanation picture](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/discuss/366350/C%2B%2B-O(n)-(explained-with-pictures)) | No memory leak in GC, smart two pass | `2019-10-29`
| ![][easy] | [733. Flood Fill](https://leetcode.com/problems/flood-fill/description/) | `Matrix`, `DFS`, `BFS`, `Iterative`, `Recursive` | [![](./images/solution.png)](topics/Matrix/Flood_Fill_733/[Iterative_DFS_getNeighbors_helper]_Flood_Fill_733.py) [![](./images/solution.png)](topics/Matrix/Flood_Fill_733/[Iterative_DFS_simple_short]_Flood_Fill_733.py) [![](./images/solution.png)](topics/Matrix/Flood_Fill_733/[Recursive_DFS]_Flood_Fill_733.py) | [![](./images/solution.png)](https://leetcode.com/problems/flood-fill/solution/) |  | Good template for DFS, BFS problems | `2019-10-29`
| ![][easy] | [443. String Compression](https://leetcode.com/problems/string-compression/description/) | `String`, `Two Pointers` | [![](./images/solution.png)](topics/String/String_Compression_443/[Better]_String_Compression_443.py) [![](./images/solution.png)](topics/String/String_Compression_443/[Clumsy]_String_Compression_443.py) | [![](./images/solution.png)](https://leetcode.com/problems/string-compression/solution/) |  | Iterate and check the next to handle last char, Iterate over digits without split | `2019-10-29`
| ![][medium] | [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/description/) | `LinkedList`, `Default Dict`, `HashTable`, `Recursive` | [![](./images/solution.png)](topics/LinkedList/Copy_List_with_Random_Pointer_138/[Awesome_Default_Dict_One_pass_no_new_List]_Copy_List_with_Random_Pointer_138.py) [![](./images/solution.png)](topics/LinkedList/Copy_List_with_Random_Pointer_138/[Clumsy_Iteratively_one_pass_with_HashTable]_Copy_List_with_Random_Pointer_138.py) [![](./images/solution.png)](topics/LinkedList/Copy_List_with_Random_Pointer_138/[Clumsy_Iteratively_two_pass_with_HashTable]_Copy_List_with_Random_Pointer_138.py) [![](./images/solution.png)](topics/LinkedList/Copy_List_with_Random_Pointer_138/[Recursively_with_HashTable]_Copy_List_with_Random_Pointer_138.py) [![](./images/solution.png)](topics/LinkedList/Copy_List_with_Random_Pointer_138/[Two_pass_no_new_List]_Copy_List_with_Random_Pointer_138.py) | [![](./images/solution.png)](https://leetcode.com/problems/copy-list-with-random-pointer/solution/) | 1) [Awesome use of Default Dict, great one pass, two pass code](https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43485/Clear-and-short-python-O(2n)-and-O(n)-solution), <br><br>2) [O(1) official solution  explained](https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)) | 1. No need for new List, store nodes in Dict only 2. Default Dict - create node on the fly | `2019-10-30`
| ![][easy] | [594. Longest Harmonious Subseq.](https://leetcode.com/problems/longest-harmonious-subsequence/description/) | `Array`, `HashTable`, `Counter`, `List Compreh.`, `Sorting` | [![](./images/solution.png)](topics/Array/Longest_Harmonious_Subsequence_594/[Counter_List_Comprehension]_Longest_Harmonious_Subsequence_594.py) [![](./images/solution.png)](topics/Array/Longest_Harmonious_Subsequence_594/[HashTable_single_pass]_Longest_Harmonious_Subsequence_594.py) [![](./images/solution.png)](topics/Array/Longest_Harmonious_Subsequence_594/[HashTable_two_passes]_Longest_Harmonious_Subsequence_594.py) [![](./images/solution.png)](topics/Array/Longest_Harmonious_Subsequence_594/[Sort]_Longest_Harmonious_Subsequence_594.py) | [![](./images/solution.png)](https://leetcode.com/problems/longest-harmonious-subsequence/solution/) |  | Tricky iteration after Sorting, Counter + List Compreh. | `2019-11-04`
| ![][medium] | [548. Split Array with Equal Sum](https://leetcode.com/problems/split-array-with-equal-sum/description/) | `Array`, `HashTable`, `Prefix Sum` | [![](./images/solution.png)](topics/Array/Split_Array_with_Equal_Sum_548/[2_Loops_HashTable_Skip_zeros]_Split_Array_with_Equal_Sum_548.py) [![](./images/solution.png)](topics/Array/Split_Array_with_Equal_Sum_548/[3_Loops]_Split_Array_with_Equal_Sum_548.py) | [![](./images/solution.png)](https://leetcode.com/problems/split-array-with-equal-sum/solution/) | 1) [Short Python solutions with "any", "check", slicing, list compreh.](https://leetcode.com/problems/split-array-with-equal-sum/discuss/101495/5-lines-simple-Python) | Prefix sums, HashTable, Skip recalculating Zeros | `2019-11-06`
| ![][medium] | [1254. Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/description/) | `Matrix`, `BFS`, `DFS` | [![](./images/solution.png)](topics/Matrix/Number_of_Closed_Islands_1254/[In_Place_Iterative_BFS]_Number_of_Closed_Islands_1254.py) [![](./images/solution.png)](topics/Matrix/Number_of_Closed_Islands_1254/[In_Place_Iterative_DFS]_Number_of_Closed_Islands_1254.py) [![](./images/solution.png)](topics/Matrix/Number_of_Closed_Islands_1254/[In_Place_Recursive_DFS]_Number_of_Closed_Islands_1254.py) | - |  | Fill from edges, BFS, DFS | `2019-12-12`
| ![][easy] | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/) | `Array`, `Rolling min` | [![](./images/solution.png)](topics/Array/Best_Time_to_Buy_and_Sell_Stock_121/Best_Time_to_Buy_and_Sell_Stock_121.py) | [![](./images/solution.png)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/) |  | Rolling min | `2019-12-14`
| ![][easy] | [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/) | `HashTable`, `Sorting` | [![](./images/solution.png)](topics/HashTable/Contains_Duplicate_217/[HashTable]_Contains_Duplicate_217.py) [![](./images/solution.png)](topics/HashTable/Contains_Duplicate_217/[Sorting]_Contains_Duplicate_217.py) | [![](./images/solution.png)](https://leetcode.com/problems/contains-duplicate/solution/) |  | Sorting = better *Space* complexity | `2019-12-14`
| ![][medium] | [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/description/) | `Intervals`, `Merging` | [![](./images/solution.png)](topics/Intervals/Merge_Intervals_56/[1_Simple_but_longer]_Merge_Intervals_56.py) [![](./images/solution.png)](topics/Intervals/Merge_Intervals_56/[2_Shorter]_Merge_Intervals_56.py) | [![](./images/solution.png)](https://leetcode.com/problems/merge-intervals/solution/) |  | Sort by start only, compare with last added | `2019-12-23`
| ![][medium] | [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/) | `Array`, `Prefix Product`, `Rolling Product` | [![](./images/solution.png)](topics/Array/Product_of_Array_Except_Self_238/[1_left_arr_right_rolling]_Product_of_Array_Except_Self_238.py) [![](./images/solution.png)](topics/Array/Product_of_Array_Except_Self_238/[2_use_output_as_left_and_right]_Product_of_Array_Except_Self_238.py) [![](./images/solution.png)](topics/Array/Product_of_Array_Except_Self_238/[3_use_output_as_left_and_right_excluding_i]_Product_of_Array_Except_Self_238.py) | [![](./images/solution.png)](https://leetcode.com/problems/product-of-array-except-self/solution/) |  | Idea to use prod[i] as product to the left **excluding** prod[i] | `2019-12-30`
| ![][easy] | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/) | `Array`, `Kadane`, `Divide and Conquer` | [![](./images/solution.png)](topics/Array/Maximum_Subarray_53/[1_Kadane_algorithm]_Maximum_Subarray_53.py) [![](./images/solution.png)](topics/Array/Maximum_Subarray_53/[2_Suboptimal_Divide_and_Conquer]_Maximum_Subarray_53.py) | [![](./images/solution.png)](https://leetcode.com/problems/maximum-subarray/solution/) |  | Kadane, Suboptimal non-obvious Divide and Conquer | `2020-01-01`
| ![][medium] | [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/description/) | `Array`, `Rolling Products` | [![](./images/solution.png)](topics/Array/Maximum_Product_Subarray_152/[1_Rolling_min_max_candidates]_Maximum_Product_Subarray_152.py) [![](./images/solution.png)](topics/Array/Maximum_Product_Subarray_152/[2_Rolling_min_max_swapping]_Maximum_Product_Subarray_152.py) [![](./images/solution.png)](topics/Array/Maximum_Product_Subarray_152/[3_Rolling_left_prod_right_prod]_Maximum_Product_Subarray_152.py) | - |  | Rolling Products, swap min and max | `2020-01-01`
| ![][medium] | [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/) | `Array`, `Binary Search` | [![](./images/solution.png)](topics/Array/Find_Minimum_in_Rotated_Sorted_Array_153/[Binary_Search_Invariants_Ascending]_Find_Minimum_in_Rotated_Sorted_Array_153.py) [![](./images/solution.png)](topics/Array/Find_Minimum_in_Rotated_Sorted_Array_153/[Binary_Search_Invariants_left_right_contains_min]_Find_Minimum_in_Rotated_Sorted_Array_153.py) | [![](./images/solution.png)](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/) |  | Invariants: 1. [-Inf, left], [right, Inf] ascending 2. min is inside [left, right] | `2020-01-01`
| ![][medium] | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/) | `Array`, `Binary Search` | [![](./images/solution.png)](topics/Array/Search_in_Rotated_Sorted_Array_33/[1_Find_min_then_find_target]_Search_in_Rotated_Sorted_Array_33.py) [![](./images/solution.png)](topics/Array/Search_in_Rotated_Sorted_Array_33/[2_Find_target_in_one_pass_more_conditions]_Search_in_Rotated_Sorted_Array_33.py) | [![](./images/solution.png)](https://leetcode.com/problems/search-in-rotated-sorted-array/solution/) | 1) [Clean Binary Search conditions for one pass](https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14437/Python-binary-search-solution-O(logn)-48ms) | Complex one-pass solution | `2020-01-04`
| ![][medium] | [15. 3Sum](https://leetcode.com/problems/3sum/description/) | `Array`, `Two Pointers` | [![](./images/solution.png)](topics/Array/3Sum_15/3Sum_15.py) | - | 1) [Sorting, two pointers solution explained](https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)) | A lot of tricks to stop/skip in the loop | `2020-01-04`
| ![][medium] | [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/) | `Array`, `Two Pointers`, `Area` | [![](./images/solution.png)](topics/Array/Container_With_Most_Water_11/Container_With_Most_Water_11.py) | [![](./images/solution.png)](https://leetcode.com/problems/container-with-most-water/solution/) |  | Two pointers, move shorter | `2020-01-05`
| ![][easy] | [371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/description/) | `Bitwise`, `Xor`, `Shift`, `And`, `Two's Compl.` | [![](./images/solution.png)](topics/Bitwise/Sum_of_Two_Integers_371/[1_WRONG_IN_PYTHON_And_Shift_carry_Xor]_Sum_of_Two_Integers_371.py) [![](./images/solution.png)](topics/Bitwise/Sum_of_Two_Integers_371/[2_And_Shift_carry_Xor_Use_mask_in_Python]_Sum_of_Two_Integers_371.py) | - | 1) [Explanation for 32-bit languages (JS)](https://leetcode.com/problems/sum-of-two-integers/discuss/132479/Simple-explanation-on-how-to-arrive-at-the-solution), <br><br>2) [Python mask fix for infinite bits in two's compl.](https://leetcode.com/problems/sum-of-two-integers/discuss/84282/Python-solution-with-no-%22%2B-*%22-completely-bit-manipulation-guaranteed) | Not easy: Xor, Shift, Carry. Python TLE for negative numbers, mask workaround | `2020-01-06`
| ![][easy] | [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/description/) | `Bitwise` | [![](./images/solution.png)](topics/Bitwise/Number_of_1_Bits_191/[1_Using_binary_operations_remove_right_bit]_Number_of_1_Bits_191.py) [![](./images/solution.png)](topics/Bitwise/Number_of_1_Bits_191/[2_Using_binary_operations_remove_right_one]_Number_of_1_Bits_191.py) [![](./images/solution.png)](topics/Bitwise/Number_of_1_Bits_191/[3_Using_bin_function]_Number_of_1_Bits_191.py) | [![](./images/solution.png)](https://leetcode.com/problems/number-of-1-bits/solution/) |  | 1. check if every bit is 1, or 2. use `n &= n - 1` to remove right-most 1 | `2020-01-06`
| ![][easy] | [268. Missing Number](https://leetcode.com/problems/missing-number/description/) | `Bitwise`, `XOR`, `Gauss`, `Arithmetic Progression`, `Binary Search` | [![](./images/solution.png)](topics/Bitwise/Missing_Number_268/[1_Bitwise_XOR]_Missing_Number_268.py) [![](./images/solution.png)](topics/Bitwise/Missing_Number_268/[2_Sum_and_Expected_Sum]_Missing_Number_268.py) [![](./images/solution.png)](topics/Bitwise/Missing_Number_268/[3_Sorting_and_Binary_Search]_Missing_Number_268.py) [![](./images/solution.png)](topics/Bitwise/Missing_Number_268/[4_HashTable]_Missing_Number_268.py) | [![](./images/solution.png)](https://leetcode.com/problems/missing-number/solution/) | 1) [Binary search solutions (in post and comments)](https://leetcode.com/problems/missing-number/discuss/69786/3-different-ideas%3A-XOR-SUM-Binary-Search.-Java-code) | Xor is best, careful with Binary Search after sorting | `2020-01-10`
<!-- Placeholder Helper for new solutions(used to programmaticaly insert new solutions here) -->


<!-- References to images, which can be used in markdown -->
[easy]: ./images/easy.png
[medium]: ./images/medium.png
[hard]: ./images/hard.png
