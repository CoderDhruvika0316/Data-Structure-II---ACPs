print()

print("=" * 100)
print("MY POWER OF TWO SCANNER")
print("=" * 100)

number = int(input("Enter a number:"))

print()

print("----------------------------------------------------------------------------")
print("PART 1 : THE [Number & (Number - 1)] TRICK")
print("----------------------------------------------------------------------------")

print(f"-> Number : {number}\n-> Binary : {bin(number)[2:]}")
print(f"\n-> [Number - 1] : {number - 1}\n-> Binary : {bin(number - 1)[2:]}")
print(f"\n-> [Number & (Number - 1)] : {number & (number - 1)}\n-> Binary : {bin(number & (number - 1))[2:]}")

print("\nOBSERVATION : This Trick removes the rightmost set bit of a number.")

print()

print("----------------------------------------------------------------------------")
print("PART 2 : POWER OF 2 CHECK")
print("----------------------------------------------------------------------------")

def power(digit):
    if digit > 0 and (digit & (digit - 1)) == 0:
        return "YES! ✅"
    else:
        return "NO! ❌"

numbers = [1, 2, 4, 6, 8, 12, 16, 18, 32]

for digit in numbers:
    print(f"-> Digit : {digit}\n-> Binary : {bin(digit)[2:]}\n-> Is Power of 2 : {power(digit)}\n")

print("----------------------------------------------------------------------------")
print("PART 3 : POWER OF 4 CHECK")
print("----------------------------------------------------------------------------")

def powerer(digit):
    if digit <= 0 or (digit & (digit - 1)) != 0:
        False

    position = 0
    while digit > 1:
        digit >>= 1
        position += 1

    if position % 2 == 0:
        return "YES! ✅"
    else:
        return "NO! ❌"

for digit in numbers:
    print(f"-> Number : {digit}\n-> Binary : {bin(digit)[2:]}\n-> Is Power of 4 : {powerer(digit)}\n")

print("----------------------------------------------------------------------------")
print("PART 4 : POWER OF 8 CHECK")
print("----------------------------------------------------------------------------")

def powering(digit):
    if not power(digit):
        return False

    position = 0

    while digit > 1:
        digit >>= 1
        position += 1

    if position % 3 == 0:
        return "YES! ✅"
    else:
        return "NO! ❌"

for digit in numbers:
    print(f"-> Number : {digit}\n-> Binary : {bin(digit)[2:]}\n-> Is Power of 8 : {powering(digit)}\n")

print("----------------------------------------------------------------------------")
print("PART 5 : BINARY EXPONENTIATON")
print("----------------------------------------------------------------------------")

def binary(base, exponent):
    answer = 1

    while exponent > 0:
        if exponent & 1:
            answer = answer * base

        base *= base
        exponent >>= 1
    
    return answer

print(f"The answer to 2 ^ 5 is : {binary(2, 5)}")
print(f"The answer to 3 ^ 4 is : {binary(3, 4)}")
print(f"The answer to 5 ^ 3 is : {binary(5, 3)}")

print()

print("=" * 100)
print("MY POWER OF TWO SCANNER SUMMARY SCRIPT")
print("=" * 100)

print("-> Power of 2 - Only one bit is a set bit.")
print("-> Power of 4 - The Set Bit Postion is even.")
print("-> Power of 8 - The Set Bit Postion is divisible by 3.")
print("-> Binary Exponentiation - Calculates powers quickly.")

print("=" * 100)