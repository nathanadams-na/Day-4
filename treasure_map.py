row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
tres_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure? e.g. row 2, column 3: 23: \t")
coords = []
for letters in position:
    coords.append(letters)
row = int(coords[0]) - 1
column = int(coords[1]) -1
tres_map[row][column] = "x"
print(f"{row1}\n{row2}\n{row3}")