def bits(number):
    return bin(number)[2:]

print()

print("=" * 100)
print("MY SECRET CODE BIT SCANNER")
print("=" * 100)

secret = int(input("Enter the secret number:"))
access = int(input("Enter the access number:"))

print()

print("------------------------------------------------------------------------------")
print("PART 1 : BITS AND BINARY")
print("------------------------------------------------------------------------------")
print(f"\nBinary Value of the secret number {secret}: {bits(secret)}")
print(f"Binary Value of access number {access}: {bits(access)}")

print()

print("------------------------------------------------------------------------------")
print("PART 2 : 'AND' and 'OR'")
print("------------------------------------------------------------------------------")
and_value = secret & access
print(f"\nThe value of {secret} & {access} is : {and_value}\nThe Binary value of the answer is : {bin(and_value)[2:]}")

or_value = secret | access
print(f"\nThe value of {secret} | {access} is : {or_value}\nThe Binary value of the answer is : {bin(or_value)[2:]}")

print()

print("------------------------------------------------------------------------------")
print("PART 3 : 'NOT' and 'XOR'")
print("------------------------------------------------------------------------------")

not_value = ~ secret & 0b1111
print(f"\nThe value of  'NOT' {secret} is : {not_value}\nThe Binary value of the answer is : {bin(not_value)[2:]}")

xor_value = secret ^ access
print(f"\nThe value of {secret} ^ {access} is : {xor_value}\nThe Binary value of the answer is : {bin(xor_value)[2:]}")

print()

print("------------------------------------------------------------------------------")
print("PART 4 : 'LEFT SHIFT' and 'RIGHT SHIFT'")
print("------------------------------------------------------------------------------")

left_shift = secret << 1
print(f"\nThe value of {secret} << 1 is : {left_shift}\nThe Binary value of the answer is : {bin(left_shift)[2:]}")

right_shift = secret >> 1
print(f"\nThe value of {secret} >> 1 is : {right_shift}\nThe Binary value of the answer is : {bin(right_shift)[2:]}")

print()

print("------------------------------------------------------------------------------")
print("PART 5 : CHECK ODD /EVEN WITH XOR")
print("------------------------------------------------------------------------------")

xor_checker = secret ^ 1
print(f"Secret Number XOR 1 : {xor_checker}")

if xor_checker == secret - 1:
    print("Secret Number is Odd.")

else:
    print("Secret Code is Even.")

print()

print("------------------------------------------------------------------------------")
print("PART 6 : COUNTING BITS")
print("------------------------------------------------------------------------------")

bit_counter = secret.bit_count()
print("Number of bits in Secret Number : {bit_counter}")

print()

print("=" * 100)
print("SECRET CODE SCANNER SUMMARY")
print("=" * 100)

print(f"Secret Number : {secret} | Secret Number in Binary : {bits(secret)}")
print(f"Access Number : {access} | Secret Number in Binary : {bits(access)}")

print(f"\nAND Result : {and_value}")
print(f"OR Result : {or_value}")
print(f"NOT (within 4 bits) Result : {not_value}")
print(f"XOR Result : {xor_value}")
print(f"LEFT SHIFT Result : {left_shift}")
print(f"RIGHT SHIFT Result : {right_shift}")

print(f"\nSecret Number Bits Count : {bit_counter}")
print("=" * 100)