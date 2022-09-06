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
    bool recSearch(TreeNode* root) {
        if ((root->left == NULL) and (root->right == NULL)) {
            return (root->val == 1);
        }
        bool res_left = false;
        bool res_right = false;
        if (root->left) {
            res_left = this->recSearch(root->left);
            if (not(res_left)) {
                root->left = NULL;
            }
        }
        if (root->right) {
            res_right = this->recSearch(root->right);
            if (not(res_right)) {
                root->right = NULL;
            }
        }
        return (res_left or res_right or (root->val == 1));
    }

    TreeNode* pruneTree(TreeNode* root) {
        bool res = this->recSearch(root);
        if (res) {
            return root;
        }
        return NULL;
    }
};