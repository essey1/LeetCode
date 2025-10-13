class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int pointer = 0;
        for (int i=0; i<nums.size(); i++){
           if (nums[i] != 0){
                if (pointer != i){
                    nums[pointer] = nums[i];
                    nums[i] = 0;
                }
            pointer ++;
           }
           
        }
    }
};