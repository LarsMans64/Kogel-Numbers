import time


def start():
    file_name = "files/" + input("\nFile: ")
    try:
        file = open(file_name + ".txt")
    except FileNotFoundError:
        file = open(file_name)
    count = int(input("How many digits? (0 = all) "))
    if count == 0: count = len(file.read())
    print("\nDigit : Number")
    start_time = time.time()
    main(file, count)
    end_time = time.time()
    print("\r" + " " * 33, " " * 2 * len(f"{count:,}"))
    print(f"[{'#'*30}] {count:,}/{count:,}")
    file_name = file.name.replace('files/', '', 1)
    total_time = round(end_time - start_time, 2)
    print(f"\nChecked {count:,} digits in {file_name} in {total_time} seconds.")
    file.close()
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
                file.seek(index + digit)
                if int(file.read(1)) != int(str(index2)[digit]):
                    break
                if digit + 1 == length:
                    print("\r" + " " * 33, " " * 2 * len(f"{count:,}"), end="\r")
                    print(f"    {shift + 1} : {index2}")
                digit += 1
            shift += 1
        update_progress_bar(index, count)
        index += 1
    return


def update_progress_bar(value, total):
    a = "#" * int(value / total * 30)
    b = "." * (30 - len(a))
    print(f"\r[{a + b}] {value:,}/{total:,}", end="")


print("""
Kogel Numbers
-------------
Put your files in the /files/ folder.
The file can only contain numbers and nothing else.""")
start()
