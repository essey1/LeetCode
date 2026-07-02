class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string, int> seen;
        int output = 0;

        for (int i=0; i<words.size(); i++){
            string rev = words[i];
            swap(rev[0], rev[1]);
            if (seen[rev] > 0) {
                output += 4;
                seen[rev]--;
            } else {
                seen[words[i]]++;
            }
        }
        for (const auto& [word, count] : seen) {
            if (count>0 && word[0] == word[1]) {
                output += 2;
                break;  // only one center word is allowed
            }
        }
        return output;
        
    }
};