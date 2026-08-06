class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[len(cost)-2], cost[len(cost)-1]
        if len(cost) <= 2:
            return min(one, two)

        for i in range(len(cost)-3, -1, -1):
            temp = one
            if one <= two:
                one += cost[i]
                two = temp
            else:
                one = two + cost[i]
                two = temp
        
        one2, two2 = cost[len(cost)-2], cost[len(cost)-1]

        for i in range(len(cost)-3, 0, -1):
            temp = one2
            if one2 <= two2:
                one2 += cost[i]
                two2 = temp
            else:
                one2 = two2 + cost[i]
                two2 = temp

        return min(one, one2)

