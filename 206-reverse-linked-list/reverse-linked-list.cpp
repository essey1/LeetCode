/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        vector<int> vectorList;
        ListNode* current =  head;
        ListNode* current2 =  head;
        while(current){
            vectorList.push_back(current->val);
            current = current->next;
        }
        while (!vectorList.empty()) {
            current2->val = vectorList.back();
            vectorList.pop_back();  
            current2 = current2->next;   
        }
        return head;
    }
};