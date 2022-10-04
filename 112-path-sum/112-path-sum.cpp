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
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (root == NULL) {
            return false;
        }
        if ((root->left == NULL) & (root->right == NULL)) {
            return root->val == targetSum;
        }
        if (root->left == NULL) {
            return this->hasPathSum(root->right, targetSum - root->val);
        }
        if (root->right == NULL) {
            return this->hasPathSum(root->left, targetSum - root->val);
        }
        return (this->hasPathSum(root->left, targetSum - root->val) || this->hasPathSum(root->right, targetSum - root->val));
    }
};
