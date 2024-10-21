buildings = ["Rose Library", "King Hall", "D-Hall", "Hartman Hall"]

i = 0
while i < len(buildings):
    print(buildings[i], end=", ")
    i += 2
print(i)

count = 10

while count >= 0:
    count -= 1
    if count == 8 or count == 6:
        continue
    elif count == 4:
        break
    
    print(count, end=" ")
    