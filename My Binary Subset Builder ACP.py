print("=" * 100)
print("MY BINARY SUBSET BUILDER SUMMARY")
print("=" * 100)

items = ["A", "B", "C", "D", "E"]
number = len(items)
total = 2 ** number

print(f"Items : {items}")
print(f"Number of items : {number}")
print(f"Total subsets : 2 ^ {number} -> {total}")

print()

print("---------------------------------------------------------------------------------------")
print("PART 1: POWER SET")
print("---------------------------------------------------------------------------------------")
print(f"For {number} items, we can create {total} subsets.")

print()

print("---------------------------------------------------------------------------------------")
print("PART 2: BINARY MASK TABLE")
print("---------------------------------------------------------------------------------------")

mask = 0

while mask < total:
    first = (mask >> 2) & 1
    second = (mask >> 1) & 1
    third = mask & 1

    print(f"Mask : {mask} -> [C][B][A] : {first, second, third}")

    mask += 1

print()

print("---------------------------------------------------------------------------------------")
print("PART 3: BIT PROBE")
print("---------------------------------------------------------------------------------------")

sample = 5

print(f"Sample Mask: {sample}")
print(f"Binary : {bin(sample)[2:]}")

digit = 0

while digit < number:
    probe = 1 << digit

    if sample & probe:
        print(f"Bit {digit} is set, so item {items[digit]} is selected.")
    else:
        print("Bit", digit, "is not set, so item", items[digit], "is not selected.")

    digit = digit + 1

print()

print("---------------------------------------------------------------------------------------")
print("PART 4: ALL SUBSETS")
print("---------------------------------------------------------------------------------------")

mask = 0

while mask < total:
    subset = []

    digit = 0
    while digit < number:
        probe = 1 << digit

        if mask & probe:
            subset.append(items[digit])

        digit = digit + 1

    print("Mask", mask, "->", subset)

    mask = mask + 1

def bitdifference(fourth , fifth):
    difference = 0

    while fourth > 0 or fifth > 0:
        lastfourth = fourth & 1
        lastfifth = fifth & 1

        if lastfourth != lastfifth:
            difference += 1

        fourth >>= 1
        fifth >>= 1

    return difference


print()

print("---------------------------------------------------------------------------------------")
print("PART 5: BIT DIFFERENCE")
print("---------------------------------------------------------------------------------------")
print(f"Difference between 12 and 15: {bitdifference(12, 15)}")
print(f"12 : {bin(12)[2:]} 15 : bin(15)[2:]")

print(f"Difference between 21 and 24: {bitdifference(21, 24)}")
print(f"21 : {bin(21)[2:]} 24 : {bin(24)[2:]}")

print(f"Difference between 8 and 8 : {bitdifference(8, 8)}")
print(f"8 : {bin(8)[2:]} 8 : {bin(8)[2:]}")

print()

print("=" * 100)
print("MY BINARY SUBSET BUILDER SUMMARY")
print("=" * 100)
print("Power Set: All possible subsets of a set.")
print("Binary Mask: A number that selects items using bits.")
print("Bit Probe: Uses 1 << digit to check a specific bit.")
print("Two Loops: One loop for masks, one loop for items.")
print("Bit Difference: Counts different bit positions.")
print("=" * 100)