class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max_value = *std::max_element(candies.begin(), candies.end());
        vector<bool> result(candies.size());

        for (int i = 0; i < candies.size(); i++) {
            candies[i] += extraCandies;
            if (candies[i] >= max_value) {
                result[i] = true;
            }
        }

        return result;
    }
};
