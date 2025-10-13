class Solution {
public:
    int compress(vector<char>& chars) {
        int counter = 0;
        int j = 0;
        string s;
        for(int i=0; i<chars.size(); i++){
            if (i > (chars.size()-1)){
                break;
            }
            if (chars[i] == chars[j]){
                counter ++;
            } else {
                if (counter == 1){
                    s.push_back(chars[j]);
                    j=i;
                } else {
                    s.push_back(chars[j]);
                    int c = counter;
                    s += (to_string(c));
                    j=i;
                    counter = 1;
                }
            }
        }
        if (counter > 0) {
            s.push_back(chars[j]);
            if (counter > 1) {
                s += to_string(counter);
            }
        }
        chars = vector<char>(s.begin(), s.end());
        return s.size();
    }
};