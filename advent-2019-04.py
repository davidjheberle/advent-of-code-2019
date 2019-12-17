raw_input = '137683-596253'

def all_digits_increasing(digits):
    return digits == sorted(digits)

def repeated_digits_adjacent(digits):
    last_digit = digits[0]
    for digit in digits[1:]:
        if last_digit == digit:
            return True
        last_digit = digit
    return False

def more_than_two_adjacent(num):
    adjacent_digits = {}
    adjacent_digit_count = 1
    digits = [int(i) for i in str(num)]
    last_digit = digits[0]
    for i in range(1, len(digits)):
        if last_digit == digits[i]:
            adjacent_digit_count += 1
        else:
            adjacent_digit_count = 1
        adjacent_digits[digits[i]] = adjacent_digit_count
        last_digit = digits[i]
    return 2 in adjacent_digits.values()

def part1(start, end):
    print("Part 1")
    valid_passwords = []
    for password in range(start, end + 1):
        digits = [int(i) for i in str(password)]
        if all_digits_increasing(digits):
            if repeated_digits_adjacent(digits):
                valid_passwords.append(password)
    return len(valid_passwords), valid_passwords

def part2(passwords):
    print("Part 2")
    valid_passwords = []
    for password in passwords:
        if more_than_two_adjacent(password):
            valid_passwords.append(password)
    return len(valid_passwords)


input_range = raw_input.split('-')
print(input_range) 
start, end = int(input_range[0]), int(input_range[1])

p1_results, valid_passwords = part1(start, end)
print(p1_results)
print(part2(valid_passwords))