/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let currSum = 0
    let res = -Infinity
    for(let x of nums){
        currSum+= x
        res = Math.max(res,currSum)
        if (currSum<0){
            currSum = 0
        }
    }
    return res
};