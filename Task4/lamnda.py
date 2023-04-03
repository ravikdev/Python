def operate_on_numbers(numbers, operation):
    result = []
    for num in numbers:
        result.append(operation(num))
    return result

# Example usage:
numbers = [1, 2, 3, 4, 5]
squared_numbers = operate_on_numbers(numbers, lambda x: x**2)
print(squared_numbers) # Output: [1, 4, 9, 16, 25]