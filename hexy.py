DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_decimal(number_str, base_from):
    """Convert a number from any base (2-36) to decimal (int)."""
    number_str = number_str.upper()
    value = 0
    for char in number_str:
        digit = DIGITS.index(char)
        if digit >= base_from:
            raise ValueError(f"invalid digit '{char}' for {base_from}")
        value = value * base_from + digit
    return value

def from_decimal(decimal_value, base_to):
    """convert a decimal number to any base (2-36)."""
    if decimal_value == 0:
        return "0"
    result = ""
    while decimal_value > 0:
        result = DIGITS[decimal_value % base_to] + result
        decimal_value //= base_to
    return result

def convert_base(number_str, base_from, base_to):
    """Convert a number strong from one base to another."""
    if not (2 <= base_from <= 36 and 2 <= base_to <+ 36):
        raise ValueError("Bases must be between 2 and 36.")
    decimal_value = to_decimal(number_str, base_from)
    return from_decimal(decimal_value, base_to)

if __name__ == "__main__":
    print("Universal Base Converter (2-36)")
    num = input("Enter the nymber: ").strip()
    base_from = int(input("Enter the base you're converting from (2-36) :"))
    base_to = int(input("Enter the base you want to convert to (2-36: "))

    try:
        converted = convert_base(num, base_from, base_to)
        print(f"\n {num} (base {base_from}) = {converted} (base {base_to})")
    except ValueError as e:
        print(f"Error: {e}")