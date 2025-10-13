class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double sum = accumulate(nums.begin(), nums.begin()+k, 0);
        double new_sum = sum;
        for (int i=k; i<nums.size(); i++){
            new_sum = new_sum + nums[i] - nums[i-k];
            sum = max(sum, new_sum);
        }
        double max_ave = sum/k;
        return max_ave;
    }
};