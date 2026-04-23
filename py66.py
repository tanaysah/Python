class FileEmptyError(Exception):
    pass

class InvalidDataError(Exception):
    pass

try:
    with open("data.txt", "r") as f:
        data = f.read()

        if not data:
            raise FileEmptyError("File is empty!")

        if not data.isdigit():
            raise InvalidDataError("Invalid data in file!")

except FileEmptyError as e:
    print(e)
except InvalidDataError as e:
    print(e)