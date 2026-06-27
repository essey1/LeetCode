class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        // up right: mat[r-1][c+1]
        // down left: mat[r+1][c-1]

        int m = mat.size();
        int n = mat[0].size();
        vector<int> out;

        int r = 0;
        int c = 0;
        bool up = true;
        for (int i=0; i<(m*n); i++){
            out.push_back(mat[r][c]);

            if (up == true){
                if (c == n-1){
                    r++;
                    up = false;
                } else if (r == 0){
                    c++;
                    up = false;
                } else {
                    r--;
                    c++;
                }
                
            } else {
                if (r == m-1){
                    c++;
                    up = true;
                } else if (c == 0){
                    r++;
                    up = true;
                } else {
                    r++;
                    c--;
                }
            }
            
        }

        return out;

    }
};