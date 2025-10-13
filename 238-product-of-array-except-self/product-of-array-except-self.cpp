class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> answer(nums.size(), 1);
        int prefix = 1;
        int postfix = 1;
        for (int i=0; i < nums.size(); i++){
            answer[i] = prefix;
            prefix = prefix*nums[i];
        }
        for (int j=nums.size()-1; j >= 0; j--){
           answer[j] = answer[j]*postfix;
           postfix = postfix*nums[j];
        } 
        return answer;
    }
};