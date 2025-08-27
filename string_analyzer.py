# String Analyzer Program
# Counts uppercase, lowercase, digits, and special characters

def analyze_string(input_string):
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    special_count = 0

    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1

    print("Uppercase letters:", uppercase_count)
    print("Lowercase letters:", lowercase_count)
    print("Digits:", digit_count)
    print("Special characters:", special_count)


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    analyze_string(user_input)
