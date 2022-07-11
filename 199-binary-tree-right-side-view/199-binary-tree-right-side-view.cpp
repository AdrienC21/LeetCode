/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        deque<TreeNode*> stack1;
        if (root) {  // if not None
            stack1.push_back(root);
        }
        deque<TreeNode*> stack2;
        vector<int> res;  // result

        TreeNode* rightmost;
        while (!stack1.empty()) {
            // rightmost node
            rightmost = stack1.back();
            // bfs from left to right
            while (!stack1.empty()) {
                if (stack1.front()->left) {
                    stack2.push_back(stack1.front()->left);
                }
                if (stack1.front()->right) {
                    stack2.push_back(stack1.front()->right);
                }
                stack1.pop_front();
            }
            // extract rightmost element of stack1 (= to node here!)
            res.push_back(rightmost->val);
            // stack1 is stack2, stack1 become empty
            swap(stack1, stack2);
        }
        return res;
    }
};
