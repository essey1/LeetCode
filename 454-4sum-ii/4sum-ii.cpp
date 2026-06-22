class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        unordered_map<int, int> count12;
        int s12;
        int s23;
        int count=0;
        for (int i: nums1){
            for (int j:nums2){
                s12 = i+j;
                count12[s12]++;
            }
        }

        for (int i: nums3){
            for (int j:nums4){
                s23 = i+j;
                if (count12.contains(-s23)){
                    count = count + count12[-s23];
                }
            }
        }
        return count;
    }
};