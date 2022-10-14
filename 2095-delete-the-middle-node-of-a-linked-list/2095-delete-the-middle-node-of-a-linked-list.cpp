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
    int lenLinkedList(ListNode* head) {
        ListNode* root = head;
        int count = 0;
        while (root) {
            count++;
            root = root->next;
        }
        return count;
    }
    ListNode* deleteMiddle(ListNode* head) {
        int k = this->lenLinkedList(head) / 2;  // k = n // 2
        if (k == 0) {
            return NULL;
        }
        ListNode* root = head;
        while (k > 1) {
            root = root->next;
            k--;
        }
        root->next = root->next->next;
        return head;
    }
};