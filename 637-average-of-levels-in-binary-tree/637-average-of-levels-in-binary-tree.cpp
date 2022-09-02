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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<TreeNode*> to_visit;
        to_visit.push_back(root);
        vector<double> res;  // result
        // initialize values
        double total_sum;
        double count;
        vector<TreeNode*> next_visit;
        TreeNode* node;

        while (!to_visit.empty()) {
            total_sum = 0;
            count = 0;
            next_visit.clear();
            while (!to_visit.empty()) {
                node = to_visit.back();
                to_visit.pop_back();
                count++;
                total_sum += node->val;
                if (node->left) {
                    next_visit.push_back(node->left);
                }
                if (node->right) {
                    next_visit.push_back(node->right);
                }
            }
            to_visit = next_visit;
            res.push_back(total_sum / count);
        }
        return res;
    }
};
