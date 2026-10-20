print()
print("=" * 100)
print("BINARY CLUE INVESTIGATOR")
print("=" * 100)

print()

first = int(input("Enter the first number:"))
second = int(input("Enter the second number:"))

print()

print("--------------------------------------------------------------------------")
print("PART 1 : XOR IDENTITY AND EQUALITY")
print("--------------------------------------------------------------------------")
print(f"First Value : {first}")
print(f"Second Value : {second}")

print(f"\nThe value of {first} ^ {first} is : {first ^ first}")
print(f"The value of {first} ^ 0 is : {first ^ 0}")

if (first ^ second) == 0:
    print("\nBoth Numbers entered are equal.")

else:
    print("\nBoth Numbers entered are different.")

print()

print("--------------------------------------------------------------------------")
print("PART 2 : XOR CALCULATION")
print("--------------------------------------------------------------------------")
cluebox = [1, 3, 1, 3, 4, 2, 4, 2, 5, 6, 7, 6, 7]

xor = 0

for clue in cluebox:
    xor ^= clue

print(f"Clues : {cluebox}")
print(f"Final XOR Result : {cluebox}")
print(f"Repeated Clues cancel out, so the remaining clue is : {xor}")

print()

print("--------------------------------------------------------------------------")
print("PART 3 : ONE ODD OCCURING NUMBER")
print("--------------------------------------------------------------------------")
numbers = [1, 2, 1, 2, 3, 4 ,3 , 4,  7, 8, 9, 8, 9]

print(f"Numbers : {numbers}")

odd = 0

for number in numbers:
    odd ^= number

print(f"Odd Number : {odd}")

print()

print("--------------------------------------------------------------------------")
print(f"PART 4 : XOR OF TWO ODD OCCURRING NUMBERS")
print("--------------------------------------------------------------------------")

pairs = [1, 2, 1, 2, 4, 3, 5, 3, 5, 7, 6, 8, 6, 8]
print(f"Numbers : {pairs}")

xorers = 0

for number in pairs:
    xorers ^= number

print(f"XOR of Two Odd Occurring Numbers : {xorers}")

print()

print("--------------------------------------------------------------------------")
print("PART 5 : SPLITTING BY THE RIGHTMOST SET BIT")
print("--------------------------------------------------------------------------")

rightmost = xorers & xorers

odder = 0
oddest = 0

for number in pairs:
    if number & rightmost:
        odder ^= number

    else:
        oddest ^= number

print(f"Rightmost Set Bit : {rightmost}")
print(f"First Odd Occurring Number : {odder}")
print(f"Second Odd Occurring Number : {oddest}")

print()

print("=" * 100)
print("BINARY CLUE INVESTIGATOR SUMMARY SCRIPT")
print("=" * 100)

print(f"XOR Identity - [Number ^ Number = 0]")
print("XOR with Zero - [Number ^ 0 = Number]")
print("XOR - Cancellation Removes Repeated Pairs")

print(f"\nOne Odd Occuring Number Extracted : {odd}")
print(f"Two Odd Occuring Numbers Extracted : {odder} and {oddest}")
print("=" * 100)