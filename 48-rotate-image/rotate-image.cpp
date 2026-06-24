class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix[0].size();
        int l = 0;
        int r = n-1;
        int t = 0;
        int b = n-1;

        while (l<r){
            for (int i=0; i<r-l; i++){
                // bl to tl
                int temp = matrix[t][l+i];
                matrix[t][l+i] = matrix[b-i][l];

                // br to bl
                matrix[b-i][l] = matrix[b][r-i];

                //tr to br
                matrix[b][r-i] = matrix[t+i][r];

                
                matrix[t+i][r] = temp;

            }
            l++;
            r--;
            t++;
            b--;
        }
        

    }
};