// Questions
// Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.
 

// Example 1:

// Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
// Output: [3,2]
// Explanation: The values that are present in at least two arrays are:
// - 3, in all three arrays.
// - 2, in nums1 and nums2.

public class Solution {

    public bool checkExist(int[] nums1, int[] nums2, int x){
        if(nums1.Contains(x) && nums2.Contains(x)){
            return true;
        }
        return false;
    }
    public IList<int> TwoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        List<int> res = new List<int>();
        for(int i=1;i<=100;i++){
            if(checkExist(nums1,nums2, i) || checkExist(nums1,nums3, i) || checkExist(nums2,nums3, i)){
                res.Add(i);
            }

        }
        return res;

        
    }
}