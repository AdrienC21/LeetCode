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
    void flatten(TreeNode* root) {
        if (root != NULL) {
            if (root->left != NULL) {
                TreeNode* right = root->right;
                TreeNode* left = root->left;
                while (left->right != NULL) {
                    left = left->right;
                }
                left->right = right;
                root->right = root->left;
                root->left = NULL;
            }

            this->flatten(root->right);
        }
    }
};