class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numsh(nums.begin(), nums.end());
        int output = 0;

        for (int num : numsh) {
            if (numsh.find(num - 1) == numsh.end()) {
                int length = 1;

                while (numsh.find(num + length) != numsh.end()) {
                    length++;
                }

                output = max(output, length);
            }
        }

        return output;
    }
};