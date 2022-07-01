class Solution {
public:
    static bool comp(vector<int> x, vector<int> y) {
        return (x[1] > y[1]);  // sort descending order by second term (number of units per box)
    }
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(), boxTypes.end(), comp);
        int box_used = 0;
        int units = 0;
        
        // loop variables
        int nb_box;
        int unit_per_box;
        for (int i=0; i<boxTypes.size(); i++) {
            nb_box = boxTypes[i][0];
            unit_per_box = boxTypes[i][1];
            if ((box_used + nb_box) >= truckSize) {
                units += ((truckSize - box_used) * unit_per_box);
                break;
            }
            units += (nb_box * unit_per_box);
            box_used += nb_box;
        }
        return units;
    }
};