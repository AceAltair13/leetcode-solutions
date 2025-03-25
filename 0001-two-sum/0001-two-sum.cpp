class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // TC: O(N)
        // SC: O(N)
        
        unordered_map<int, int> hashset;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if (hashset.contains(complement)) {
                return {hashset[complement], i};
            }
            hashset[nums[i]] = i;
        }

        return {};
    }
};