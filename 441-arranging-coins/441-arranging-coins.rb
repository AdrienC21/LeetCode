# @param {Integer} n
# @return {Integer}
def arrange_coins(n)
    res = (-1 + Math.sqrt(1 + 8 * n)) / 2;
    return res.floor();
end