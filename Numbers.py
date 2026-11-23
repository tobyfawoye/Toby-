
numbers = [10, 20, 30, 20]

def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def calculate_median_mode(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2

    mode = max(set(numbers), key=numbers.count)

    return median, mode

print("Sum:", calculate_sum(numbers))
print("Average:", calculate_average(numbers))

median, mode = calculate_median_mode(numbers)

print("Median:", median)
print("Mode:", mode)
