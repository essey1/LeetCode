class Solution {
public:
    string reverseVowels(string s) {
        vector<char> vowels(0);
        string output = s;
        for (int i=0; i < s.size(); i++){
            if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' ||
                s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U') {
                vowels.push_back(s[i]);
            }
        
        }
        for (int j=0; j < s.size(); j++){
                if (s[j] == 'a' || s[j] == 'e' || s[j] == 'i' || s[j] == 'o' || s[j] == 'u' ||
                s[j] == 'A' || s[j] == 'E' || s[j] == 'I' || s[j] == 'O' || s[j] == 'U') {
                output[j] = vowels.back();
                vowels.pop_back();
            }
           
            
        }


        return output;
    }
};