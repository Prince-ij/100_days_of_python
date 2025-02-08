with open("file1.txt") as file:
    file_1 = file.readlines()

with open("file2.txt") as file:
    file_2 = file.readlines()

result = [int(num) for num in file_1 if num in file_2]
print(result)
