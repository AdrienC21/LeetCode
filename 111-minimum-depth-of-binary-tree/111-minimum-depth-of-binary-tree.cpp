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
    int minDepth(TreeNode* root) {
        if (root) {
            if (root->left and root->right) {
                return min(this->minDepth(root->left), this->minDepth(root->right)) + 1;
            }
            if (root->left) {
                return 1 + this->minDepth(root->left);
            }
            if (root->right) {
                return 1 + this->minDepth(root->right);
            }
            return 1;
        }
        return 0;
    }
};