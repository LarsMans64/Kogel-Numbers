import time


def start():
    file_name = "files/" + input("\nFile: ")
    if file_name.lower() == "stop":
        exit()
    try:
        file = open(file_name + ".txt")
    except FileNotFoundError:
        file = open(file_name)

    count = int(input("How many digits? (0 = all) "))
    if count == 0: count = len(file.read())

    filter_digit = int(input("Search for which digit per number? (0 = all, -1 = last) ")) - 1

    start_time = time.time()
    print("\nDigit : Number")
    if filter_digit == -1:
        main(file, count)
    else:
        main_filtered(file, count, filter_digit)
    end_time = time.time()

    fcount = f"{count:,}"
    print("\r" + " " * 33, " " * 2 * len(fcount))
    print(f"[{'#'*30}] {fcount}/{fcount}")
    file_name = file.name.replace("files/", "", 1)
    total_time = round(end_time - start_time, 2)
    print(f"\nChecked {fcount} digits in {file_name} in {total_time} seconds.")
    file.close()
    start()


def main(file, count):
    index = 0
    bar_number = count // 531
    while index <= count:  # Check all digits in file
        if index % bar_number == 0:
            update_progress_bar(index, count)
        length = len(str(index))
        if index + length >= count:
            break
        shift = 0
        while shift < length:  # Check all possible shifts
            index_with_shift = index + shift
            digit = 0
            while digit < length:  # Check all digits of the number
                file.seek(index + digit)
                if int(file.read(1)) != int(str(index_with_shift)[digit]):
                    break
                if digit == length - 1:
                    print("\r" + " " * 33, " " * 2 * len(f"{count:,}"), end="\r")
                    print(f"    {shift + 1} : {index_with_shift}")
                digit += 1
            shift += 1
        index += 1
    return


def main_filtered(file, count, filter_digit):
    index = 0
    bar_number = count // 531
    while index <= count:
        if index % bar_number == 0:
            update_progress_bar(index, count)
        length = len(str(index)) - 1
        if filter_digit == -2: shift = length
        else: shift = filter_digit
        if index + length > count: break
        index_with_shift = index + shift
        digit = 0
        while digit <= length and filter_digit <= length:
            file.seek(index + digit)
            if int(file.read(1)) != int(str(index_with_shift)[digit]):
                break
            if digit == length:
                print("\r" + " " * 33, " " * 2 * len(f"{count:,}"), end="\r")
                print(f"    {shift + 1} : {index_with_shift}")
            digit += 1
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
The file can only contain numbers and nothing else.
Type 'stop' to exit.""")
start()
