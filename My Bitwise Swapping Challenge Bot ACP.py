print()

print("=" * 100)
print("MY BITWISE SWAPPING CHALLENGE BOT")
print("=" * 100)

print()

print("-------------------------------------------------------------------------------------------------------")
print("PART 1 : SWAPPING WITHOUT A THIRD VARIABLE")
print("-------------------------------------------------------------------------------------------------------")

first = int(input("\nEnter a number:"))
second = int(input("Enter another number:"))

print(f"\n• Before :-\n-> First number : {first}\n-> Second : {second}")

first += second
second -= first
first -= second

print(f"\n• After :-\n-> First number : {first}\n-> Second : {second}")

print()

print("-------------------------------------------------------------------------------------------------------")
print("PART 2 : XOR SWAP")
print("-------------------------------------------------------------------------------------------------------")

third = int(input("\nEnter a number:"))
fourth = int(input("Enter another number:"))

print(f"\n• Before :-\n-> First number : {third}\n-> Second : {fourth}")

print()

third ^= fourth
fourth ^= third
third ^= fourth

print(f"\n• After :-\n-> First number : {third}\n-> Second : {fourth}")

print()

print("-------------------------------------------------------------------------------------------------------")
print("PART 3 : DOUBLING THE NUMBER USING LEFT SHIFT")
print("-------------------------------------------------------------------------------------------------------")

number = int(input("Enter a number:"))
print(f"Original number : {number}\n")

for i in range(1, 5):
    print(f"‣ {number} << {i} : {number << i}")

print("\n-> Observation : Each left shift multiplies the current number by 2.")

print()

print("-------------------------------------------------------------------------------------------------------")
print("PART 4 : XOR FOR SIGN DETECTION")
print("-------------------------------------------------------------------------------------------------------")

fifth = int(input("Enter a number:"))
sixth = int(input("Enter another number:"))

if (fifth < 0) ^ (sixth < 0):
    print("\n-> Observation : The numbers have different signs.")
else:
    print("\n-> Observation : The numbers have the same signs.")

print()

print("-------------------------------------------------------------------------------------------------------")
print("PART 5 : DIVIDE WITHOUT /")
print("-------------------------------------------------------------------------------------------------------")

dividend = int(input("Enter a dividend:"))
divisor = int(input("Enter a divisor:"))

quotient = 0
remainder = dividend

while remainder >= divisor:
    remainder -= divisor
    quotient += 1

print(f"\n-> Dividend : {dividend}")
print(f"-> Divisor : {divisor}")
print(f"-> Quotient : {quotient}")
print(f"-> Remainder : {remainder}")

print()

print("=" * 100)
print("MY BITWISE SWAPPING CHALLENGE BOT SUMMARY")
print("=" * 100)

print("⇒ Swap without a third variable using addition and subrtaction.")
print("⇒ XOR Swap uses the ^ operator to swap values.")
print("⇒ Left shift doubles a number.")
print("⇒ XOR can help detect different signs.")
print("⇒ Division can be done using repeated subtraction.")

print("=" * 100)