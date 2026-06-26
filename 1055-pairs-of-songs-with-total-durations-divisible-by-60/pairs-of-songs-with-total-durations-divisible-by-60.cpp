class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        vector<int> count(60, 0);
        int output=0;
        int need;
        int r;
        for (int i=0; i<time.size(); i++){
            r = time[i]%60;
            need = (60-r)%60;
            output += count[need];
            count[r]++;
        }
        return output;
    }
};