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
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* curr = head->next;
        if (head->next == NULL)
            return head;
        ListNode* prev = head;
        while (curr) {
            prev->next = new ListNode(gcd(prev->val, curr->val));
            prev->next->next = curr;

            prev = curr;
            curr = curr->next;
        }
        return head;
    }
};