class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int l = 0;
        int r = matrix[0].size();
        int b = matrix.size();
        int t = 0;
        vector<int> output;
        
        while (l<r && t<b){
            for (int i=l; i < r; i++){
                output.push_back(matrix[t][i]);
            }
            t++;

            for (int i=t; i < b; i++){
                output.push_back(matrix[i][r-1]);
            } 
            r--;

            if (t<b){
                for (int i=r-1; i >= l; i--){
                    output.push_back(matrix[b-1][i]);
                }
                b--;
            }
            
            if (l<r){
                for (int i=b-1; i >= t; i--){
                    output.push_back(matrix[i][l]);
                }
                l++;
            }
            
        }

        return output;
        
    }
};