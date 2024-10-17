numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
k = numbers.index (None)
numbers.remove (None)
sum = sum(numbers)/(len(numbers)+1)
numbers.insert (k, sum)
print("Измененный список:", numbers)
