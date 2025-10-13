class Solution {
public:
    string reverseWords(string s) {
        vector<string> words;
        vector<string> reversed_words;
        string word;
        string output;
        for (int i=0; i<s.length(); i++){
            if (s[i] != ' '){
                word += s[i];
            } else {
                if (!word.empty()) { 
                    words.push_back(word);
                    word.clear();
                }
            }
        }
        if (!word.empty()) {
            words.push_back(word);
        }

        reverse(words.begin(), words.end());

        for (int j=0; j<words.size(); j++){
            output += words[j];
            if (j != words.size()-1){
                output += " ";
            }
        }


        return output;
    }
};