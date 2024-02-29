function mergeSort(arr) {
    if (arr.length <= 1) {
      return arr; // Base case: if the array has 1 or 0 elements, it is already sorted
    }
  
   const [arr1 , arr2] = splitList(arr)
    
    const sortedLeft = mergeSort(arr1);
    const sortedRight = mergeSort(arr2);
  
    return merge(sortedLeft, sortedRight);
  }

  
  function splitList(arr){
     const middle = Math.floor(arr.length / 2);
    const leftHalf = arr.slice(0, middle);
    const rightHalf = arr.slice(middle);
    return [leftHalf, rightHalf]
  }
  
  function merge(left, right) {
    let result = [];
    let leftIndex = 0;
    let rightIndex = 0;
  
    // Compare elements and merge them in sorted order
    while (leftIndex < left.length && rightIndex < right.length) {
      if (left[leftIndex] < right[rightIndex]) {
        result.push(left[leftIndex]);
        leftIndex++;
      } else {
        result.push(right[rightIndex]);
        rightIndex++;
      }
    }
  
    // Add any remaining elements from both arrays
    return result.concat(left.slice(leftIndex), right.slice(rightIndex));
  }
  
  // Example usage:
  const unsortedArray = [64, 34, 25, 12, 22, 11, 90];
  const sortedArray = mergeSort(unsortedArray);
  console.log(sortedArray);
  