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
    int count;

    void recSearch(TreeNode* root, int max_val) {
        if (root->left) {
            if (root->left->val >= max_val) {
                this->count++;
            }
            this->recSearch(root->left, std::max(max_val, root->left->val));
        }
        if (root->right) {
            if (root->right->val >= max_val) {
                this->count++;
            }
            this->recSearch(root->right, std::max(max_val, root->right->val));
        }
    }

    int goodNodes(TreeNode* root) {
        this->count = 1;
        this->recSearch(root, root->val);
        return this->count;

    }
};