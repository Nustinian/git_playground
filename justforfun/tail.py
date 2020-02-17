import os
from time import time
start = time()
def tail(filename, lines):
    with open(filename, 'r') as f:
        f.seek(0, 2)
        last_ten_lines = []
        cake = 0
        try:
            f.seek(f.tell() - 1, os.SEEK_SET)
            last_char = f.read(1)
            if last_char == "\n":
                last_ten_lines.insert(0, last_char)
                f.seek(f.tell() - 1, os.SEEK_SET)
        except ValueError:
            return "empty file"
        buffer = ""
        while len(last_ten_lines) < lines:
            try:
                f.seek(f.tell() - 2, os.SEEK_SET)
                previous_char = f.read(1)
                if previous_char == "\n":
                    if len(buffer) == 0:
                        last_ten_lines.insert(0, "\n")
                    else:
                        last_ten_lines.insert(0, buffer)
                    buffer = "\n"
                    f.seek(f.tell() - 1, os.SEEK_SET)
                else:
                    buffer = previous_char + buffer
            except ValueError:
                last_ten_lines.insert(0, buffer)
                return last_ten_lines
        return last_ten_lines


print("".join(tail('equals.py', 23)))
print(time() - start)