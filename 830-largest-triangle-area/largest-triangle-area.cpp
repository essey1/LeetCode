#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

class Solution {
public:
    double largestTriangleArea(vector<vector<int>>& points) {
        int N = points.size();
        double ans = 0.0;

        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                for (int k = j + 1; k < N; k++) {
                    // Each point is a vector<int> of size 2
                    const vector<int>& P = points[i];
                    const vector<int>& Q = points[j];
                    const vector<int>& R = points[k];

                    // Shoelace / cross-product formula for triangle area:
                    // area = |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)| / 2
                    double area = fabs(
                        P[0] * (Q[1] - R[1]) +
                        Q[0] * (R[1] - P[1]) +
                        R[0] * (P[1] - Q[1])
                    ) / 2.0;

                    ans = max(ans, area);
                }
            }
        }
        return ans;
    }
};
