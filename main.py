def start():
    file = open(input("File: ") + ".txt")
    count = int(input("How many digits? (0 = all) "))
    print("")
    print("Shift : Number")
    if count == 0: count = len(file.read())
    main(file, count)


def main(file, count):
    index = 0
    while index <= count:   # Check all digits
        length = len(str(index))
        if index + length >= count: break
        shift = 0
        while shift < length:   # Check all possible shifts
            index2 = index + shift
            digit = 0
            while digit < length:   # Check all digits of the number
                temp_index = index + digit
                file.seek(temp_index)
                if int(file.read(1)) != int(str(index2)[digit]):
                    break
                if digit + 1 == length:
                    print(shift, ":", index2)
                digit += 1
            shift += 1
        index += 1
    print()
    start()


print("""
Kogel Numbers
-------------
Put your files in the same folder as the script
""")
start()
