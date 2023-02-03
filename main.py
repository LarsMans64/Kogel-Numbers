import sys
import time


def start():
    file_name = input("File: ")
    try:
        file = open(file_name + ".txt")
    except FileNotFoundError:
        file = open(file_name)
    count = int(input("How many digits? (0 = all) "))
    progress_bar = bool_input("Progress bar?")
    if count == 0: count = len(file.read())
    print()
    if not progress_bar: print("Digit : Number")
    start_time = time.time()
    main(file, count, progress_bar)
    end_time = time.time()
    if progress_bar:
        sys.stdout.write(f"\r[{'#'*30}] {count:,}/{count:,}")
        f = open("output.txt")
        print("\n\nDigit : Number\n" + f.read())
    else: print()
    print(f"Checked {count:,} digits in {file.name} in {round(end_time - start_time, 2)} seconds.\n")
    start()


def main(file, count, progress_bar):
    if progress_bar:
        f = open("output.txt", "w")
    index = 0
    while index <= count:  # Check all digits
        length = len(str(index))
        if index + length >= count: break
        shift = 0
        while shift < length:  # Check all possible shifts
            index2 = index + shift
            digit = 0
            while digit < length:  # Check all digits of the number
                file.seek(index + digit)
                if int(file.read(1)) != int(str(index2)[digit]):
                    break
                if digit + 1 == length:
                    if progress_bar:
                        f.write(f"    {shift + 1} : {index2}\n")
                    else:
                        print(f"    {shift + 1} : {index2}")
                digit += 1
            shift += 1
        if progress_bar:
            p = "#" * int(index / count * 30)
            sys.stdout.write(f"\r[{p}{'.' * (30 - len(p))}] {index:,}/{count:,}")
        index += 1
    return


def bool_input(text):
    if input(text + " y/n ").lower() == "y":
        return True
    else:
        return False


print("""
Kogel Numbers
-------------
Put your files in the same folder as the script.
The file must contain only numbers and nothing else.
Disable the progress bar to get live answers.
""")
start()
