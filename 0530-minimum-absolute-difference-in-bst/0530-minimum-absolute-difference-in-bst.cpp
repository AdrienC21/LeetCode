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
    void rec_search(TreeNode* root, vector<int>* values) {
        if (root != NULL) {
            values->push_back(root->val);
            Solution::rec_search(root->left, values);
            Solution::rec_search(root->right, values);
        }
    }

    int getMinimumDifference(TreeNode* root) {
        vector<int> values;

        Solution::rec_search(root, &values);
        sort(values.begin(), values.end());

        int res = INT_MAX;
        for (int i=0; i<(values.size()-1); i++) {
            if ((values[i+1] - values[i]) < res) {
                res = values[i+1] - values[i];
            }
        }
        return res;
    }
};
