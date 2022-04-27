/**
 * @param {number} num1
 * @param {number} num2
 * @return {number}
 */
var sum = function(num1, num2) {
    /**
    Bitwise sum
    */
    while (num2) {
        carry = num1 & num2;
        num1 = num1 ^ num2;
        num2 = carry << 1;
    };
    return num1
};