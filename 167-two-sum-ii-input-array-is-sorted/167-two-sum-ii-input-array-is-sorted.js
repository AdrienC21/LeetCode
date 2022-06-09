/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    // let's use two pointers
    var pleft = 0;
    var pright = numbers.length - 1;
    var nbleft = numbers[pleft];
    var nbright = numbers[pright];
    var s;
    var res = new Array();
    while (pleft < pright) {
        s = nbleft + nbright;
        if (s < target) {
            pleft++;
            nbleft = numbers[pleft];
        }
        else if (s > target) {
            pright--;
            nbright = numbers[pright];
        }
        else {
            res[0] = pleft + 1;
            res[1] = pright + 1;
            return res;
        }
    }
    res[0] = -1;
    res[1] = -1;
    return res;
};