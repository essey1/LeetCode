class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        merged.clear(); // reset for every call
        merged.reserve(word1.length() + word2.length()); // avoid multiple memory reallocations

        int i = 0, j = 0;
        int n1 = word1.length(), n2 = word2.length();

        while (i < n1 || j < n2) {
            if (i < n1) merged.push_back(word1[i++]);
            if (j < n2) merged.push_back(word2[j++]);
        }
        return merged;
    }

private:
    string merged;
};