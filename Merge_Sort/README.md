# Merge Sort

## Algorithm Pseudo-Code

```
function Mergesort(array):
  n = length(array)
  if n == 1:
    return array
  first_half = array[0]...array[n/2]
  second_half = array[(n/2)+1]...array[n]
  first_half = Mergesort(first_half)
  second_half = Mergesort(second_half)
  return merge(first_half, second_half)
  
function merge(arr1, arr2):
  arr3 = []
  while length(arr1) > 0 and length(arr2) > 0:
    if arr1[0] > arr2[0]:
      arr3.add(arr2[0])
      arr2 remove element in position 0
    else:
      Do the reverse (i.e. arr1 instead of arr2)
  while length(arr1) > 0:
    arr3.add(arr1[0])
    arr1 remove element in position 0
  while length(arr2) > 0:
    arr3.add(arr2[0])
    arr2 remove element in position 0
```

## Time complexity

<strong>Worst case</strong>: O(n log(n))
<strong>Average case</strong>: O(n log(n))
<strong>Best case</strong>: O(n log(n))

## Space complexity

O(n)
