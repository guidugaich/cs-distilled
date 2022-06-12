def selection_sort(list):
  list_size = len(list)

  for item in range(list_size):
    smallest = item

    for i in range (item + 1, list_size):
      if list[i] < list[smallest]:
        smallest = i

    # swap items
    list[item], list[smallest] = list[smallest], list[item]

  return list

if __name__ == '__main__':
  print(selection_sort([6, 54, 43, 32, 42, 1]))
