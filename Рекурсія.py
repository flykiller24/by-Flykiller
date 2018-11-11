def a(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + a(numbers[1:])
print(a([1, 2, 4, 8, 16]))
