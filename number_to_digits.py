# Function to convert single digit or two-digit number into words
def num_to_words(n, suffix=''):
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    if n == 0:
        return ""
    elif n < 10:
        return units[n] + suffix
    elif n < 20:
        return teens[n-11] + suffix
    else:
        return tens[n // 10] + " " + units[n % 10] + suffix

# Function to convert a number (up to billions) into words
def convert_to_words(n):
    if n == 0:
        return "Zero"

    result = ""

    # Billions
    if n // 1_000_000_000 > 0:
        result += num_to_words(n // 1_000_000_000) + " Billion "
        n %= 1_000_000_000

    # Millions
    if n // 1_000_000 > 0:
        result += num_to_words(n // 1_000_000) + " Million "
        n %= 1_000_000

    # Thousands
    if n // 1_000 > 0:
        result += num_to_words(n // 1_000) + " Thousand "
        n %= 1_000

    # Hundreds
    if n // 100 > 0:
        result += num_to_words(n // 100) + " Hundred "
        n %= 100

    # Tens and units
    if n > 0:
        if result != "":
            result += "and "
        result += num_to_words(n)

    return result.strip()

# Testing the function
number = int(input("Enter a number: "))
print(convert_to_words(number))
