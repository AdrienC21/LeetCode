class Solution {
public:
    static bool comp(const vector<int>& vec1, const vector<int>& vec2) {
        return vec1[1] < vec2[1];
    }
    int scheduleCourse(vector<vector<int>>& courses) {
        sort(courses.begin(), courses.end(), comp);  // sort by duration
        priority_queue<int> heap;  // it's by default a max heap!
        int total = 0;  // sum of courses length
        // iterate elements of courses
        int duration;
        int lastDay;
        for (int i=0; i<courses.size(); i++) {
            duration = courses[i][0];
            lastDay = courses[i][1];
            if ((total + duration) <= lastDay) {  // we can add this course
                total += duration;
                heap.push(duration);
            }
            else {
                if (heap.size() != 0) {
                    if (heap.top() > duration) {
                        total += (-heap.top() + duration);
                        heap.pop();
                        heap.push(duration);
                    }
                }
            }
        }
        return heap.size();
    }
};
