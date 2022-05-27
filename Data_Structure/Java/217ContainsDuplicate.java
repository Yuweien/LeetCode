package Data_Structure.Array.Java;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution1 {
    /**Approach#1:Native Linear Search[Time Limit Exceeded]
    searching for any pair with duplicates
     */
    public boolean containsDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; ++i) {
            for (int j = 0; j < i; ++j) { //nested loops, n(n-1)/2 pairs
                if (nums[j] == nums[i]) return true;
            }
        }
        return false;
    }
}
//Time:O(n^2)
//Space:O(1):constant extra space


class Solution2 {
    /**Approach#2:Sorting[Accepted]
    heapsort: provide O(nlogn)worst-case performance.
     */
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums); //sort the array
        for (int i = 0; i < nums.length -1; ++i) {
            if (nums[i] == nums[i + 1]) return true; //compare each item to the next
        }
        return false;
    }   
}
//Time: O(nlogn). Sorting: O(nlogn), sweeping: O(n)
//Space: O(1). heapsort: O(1)


class Solution3 {
    /**Approach#2:Hash Table[Accepted]
    dynamic set:harsh table. Searching in unsorted array: O(n)
     */
    public boolean containsDuplicate(int[] nums) {
       Set<Integer> set = new HashSet<>(nums.length); // new set
       for (int x: nums) {
           if (set.contains(x)) return true;
           set.add(x);
       }
       return false;
    }   
}
//Time: O(n). search(): constant, insert(): constant, do search and insert n times
//Space: O(n). Harsh table: linear with the number of elements of int[]