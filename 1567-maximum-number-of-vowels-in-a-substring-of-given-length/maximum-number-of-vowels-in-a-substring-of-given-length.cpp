class Solution {
public:
    int maxVowels(string s, int k) {
        vector<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        vector<int> counters{};
        int counter = 0;
        for (int i=0; i<k; i++){
            auto it = find(vowels.begin(), vowels.end(), s[i]);
            if (it != vowels.end()) {
                counter ++;
                cout << counter << endl;
            }
            counters.push_back(counter);
        }
        for (int i=k; i<s.size(); i++){
            auto start = find(vowels.begin(), vowels.end(), s[i-k]);
            if (start != vowels.end()) {
                counter --;
                cout << counter << endl;
            }
            auto end = find(vowels.begin(), vowels.end(), s[i]);
            if (end != vowels.end()) {
                counter ++;
                cout << counter << endl;
            }
            counters.push_back(counter);

        }
        int maxVal = *max_element(counters.begin(), counters.end());
        return maxVal; 
    }
    
};