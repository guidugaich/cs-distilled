import math

def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result

def merge_sort(list):
  list_length = len(list)

  if list_length == 1:
    return list

  left = list[:math.ceil(list_length/2)]
  right = list[math.ceil(list_length/2):]

  return merge(merge_sort(left), merge_sort(right))

if __name__ == '__main__':
  print(merge_sort([5, 3, 7, 9, 1]))