import time


def start():
    file_name = input("File: ")
    try:
        file = open(file_name + ".txt")
    except FileNotFoundError:
        file = open(file_name)
    count = int(input("How many digits? (0 = all) "))
    if count == 0:
        count = len(file.read())
    print()
    print("Digit : Number")
    start_time = time.time()
    main(file, count)
    end_time = time.time()
    print(f"Checked {count:,} digits in {file.name} in {round(end_time - start_time, 2)} seconds.")
    print()
    start()


def main(file, count):
    index = 0
    while index <= count:  # Check all digits
        length = len(str(index))
        if index + length >= count: break
        shift = 0
        while shift < length:  # Check all possible shifts
            index2 = index + shift
            digit = 0
            while digit < length:  # Check all digits of the number
                temp_index = index + digit
                file.seek(temp_index)
                if int(file.read(1)) != int(str(index2)[digit]):
                    break
                if digit + 1 == length:
                    print(shift + 1, ":", index2)
                digit += 1
            shift += 1
        index += 1
    return


print("""
Kogel Numbers
-------------
Put your files in the same folder as the script.
""")
start()
