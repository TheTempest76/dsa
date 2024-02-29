// 66. Plus One
// Solved
// Easy
// Topics
// Companies

// You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

// Increment the large integer by one and return the resulting array of digits.

 

// Example 1:

// Input: digits = [1,2,3]
// Output: [1,2,4]
// Explanation: The array represents the integer 123.
// Incrementing by one gives 123 + 1 = 124.
// Thus, the result should be [1,2,4].

// Example 2:

// Input: digits = [4,3,2,1]
// Output: [4,3,2,2]
// Explanation: The array represents the integer 4321.
// Incrementing by one gives 4321 + 1 = 4322.
// Thus, the result should be [4,3,2,2].

// Example 3:

// Input: digits = [9]
// Output: [1,0]
// Explanation: The array represents the integer 9.
// Incrementing by one gives 9 + 1 = 10.
// Thus, the result should be [1,0].

const plusOne = (digits) =>{
    for(i = digits.length-1 ;i>=0 ; i-- ){// traverses the list in reverse order 
        if(digits[i]<9){                // if last one is less than 9 then just add one to it
            digits[i]++;
            return digits   // and return
        }
        digits[i] = 0       //if it is equal to 9 then make it 0 . then go the next one i.e the last but one 
    }
    //now for the test case where every digit is 9 then this loop would have made everything 0 
    //simple sol make the first digit one and then add 0 in the last
    // very nice solution not mine tho :(
    digits[0] = 1;
    digits[digits.length] = 0
     
    return digits


}
console.log(plusOne([9]))
console.log(plusOne([9 ,9,9,9]))