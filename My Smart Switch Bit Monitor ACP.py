print()

print("=" * 100)
print("MY SMART SWITCH BIT MONITOR")
print("=" * 100)

switch = 50 #110010

def show_bits(number):
    return bin(number)[2:]

print(f"Value of the Switch : {switch}")
print(f"Switch Value in Binary : {show_bits(switch)}")

print()

print("---------------------------------------------------------------------------------")
print("PART 1 : ZERO BITS AND SET BITS")
print("---------------------------------------------------------------------------------")

binary = show_bits(switch)

sets = binary.count("1")
zeros = binary.count("0")

print(f"Set Bits / ON Switches : {sets}")
print(f"Zero Bits / OFF Switches : {zeros}")

print()

print("---------------------------------------------------------------------------------")
print("PART 2 : COUNTING THE SET BITS")
print("---------------------------------------------------------------------------------")

counter = 0
temporary = switch

while temporary > 0:
    if temporary & 1:
        counter += 1

    temporary >>= 1

print(f"Number of ON Switches : {counter}")

print()

print("---------------------------------------------------------------------------------")
print("PART 3 : THE FIRST SET BIT")
print("---------------------------------------------------------------------------------")

position = 1
temporary = switch

while temporary > 0:
    if temporary & 1:
        break

    position += 1
    temporary >>= 1

print(f"The First Set Bit / ON Switch is at Position : {position}")

print()

print("---------------------------------------------------------------------------------")
print("PART 4 : BUILDING A BIT MASK")
print("---------------------------------------------------------------------------------")

for digit in range(6):
    mask = 1 << digit
    print(f"Bit : {digit}\nMask : {mask}\nBinary : {show_bits(mask)}\n")

print("---------------------------------------------------------------------------------")
print("PART 5 : CHECK IF THE Nth BIT IS SET")
print("---------------------------------------------------------------------------------")

switcheroos = ["Fan", "Cooler", "Refrigerator", "Television", "Bedside Lamp", "Gaming Room Speakers"]

for digit in range(6):
    mask = 1 << digit

    if switch & mask:
        print(f"Bit {digit} - {switcheroos[digit]} is ON.")

    else:
        print(f"Bit {digit} - {switcheroos[digit]} is OFF.")

print()

print("=" * 100)
print("MY SMART SWITCH BIT MONITOR SUMMARY")
print("=" * 100)

print(f"Switch Value : {switch}")
print(f"Binary of Switch Value : {show_bits(switch)}")
print(f"Total ON Switches : {counter}")
print(f"First ON Switch Position : {position}")

print("=" * 100)