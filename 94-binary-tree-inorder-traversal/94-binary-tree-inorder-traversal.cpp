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
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == NULL) {
            vector<int> res;
            return res;
        }
        if ((root->left == NULL) & (root->right == NULL)) {
            vector<int> res;
            res.push_back(root->val);
            return res;
        }
        if (root->left == NULL) {
            vector<int> res;
            res.push_back(root->val);
            vector<int> sub_res = this->inorderTraversal(root->right);
            for (auto &n : sub_res) {
                res.push_back(n);
            }
            return res;
        }
        if (root->right == NULL) {
            vector<int> res = this->inorderTraversal(root->left);
            res.push_back(root->val);
            return res;
        }
        vector<int> res = this->inorderTraversal(root->left);
        res.push_back(root->val);
        vector<int> sub_res = this->inorderTraversal(root->right);
        for (auto &n : sub_res) {
            res.push_back(n);
        }
        return res;
    }
};