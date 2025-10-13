class Solution {
public:
    int maxArea(vector<int>& height) {
        int j = height.size() - 1;
        int new_area = 1;
        int area = 0;
        int i = 0;

        while (i < j) {
            if (height[i] <= height[j]) {
                new_area = height[i] * (j - i);
            } else {
                new_area = height[j] * (j - i);
            }

            if (new_area > area) {
                area = new_area;
            }

            if (height[i] <= height[j]) {
                i++;
            } else {
                j--;
            }
        }

        return area;        
    }
};
