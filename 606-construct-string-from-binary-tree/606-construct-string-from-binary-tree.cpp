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
    string recSearch(TreeNode* root) {
        if ((root->left == NULL) & (root->right == NULL)) {
            return std::to_string(root->val);
        }
        if (root->right == NULL) {
            return std::to_string(root->val) + "(" + this->recSearch(root->left) + ")";
        }
        if (root->left == NULL) {
            return std::to_string(root->val) + "()(" + this->recSearch(root->right) + ")";
        }
        return std::to_string(root->val) + "(" + this->recSearch(root->left) + ")(" + this->recSearch(root->right) + ")";
    }
    string tree2str(TreeNode* root) {            
        return this->recSearch(root);
    }
};
