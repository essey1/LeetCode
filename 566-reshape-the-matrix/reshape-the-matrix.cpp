class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int n = mat.size();
        int m = mat[0].size();
        int lin;
        vector<vector<int>> output;

        for (int i = 0; i < r; i++) {
            output.push_back(vector<int>());
            for (int j = 0; j < c; j++) {
                output[i].push_back(0);
            }
        }

        if (n*m != r*c){
            return mat;
        }
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                lin = m*i+j;
                output[lin/c][lin%c] = mat[i][j];
            }
        }
        return output;    
    }
};