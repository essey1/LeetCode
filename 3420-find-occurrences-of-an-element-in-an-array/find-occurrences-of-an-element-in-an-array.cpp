class Solution {
public:
    vector<int> occurrencesOfElement(vector<int>& nums, vector<int>& queries, int x) {
        std::string multiLineColumn = R"(
        - go through nums once
        - everytime nums[i] == x:
            store i
        )";

        vector<int> positions;
        vector<int> answer;

        for(int i=0; i<size(nums); i++){
            if(nums[i] == x){
                positions.push_back(i);

            };
        };

        for(int i=0; i<size(queries); i++){
            int k = queries[i];
            if (k<= positions.size()){
                answer.push_back(positions[k-1]);
            } else {
                answer.push_back(-1);
            }
        };

        return answer;
    };
};