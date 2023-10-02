# FILE_NAME = "name.txt"
FILE_NAME = "numbers.txt"
#
# user_name = input("Name:")
# with open(NAME_FILE, "w") as out_file:
#     print(user_name, file=out_file)
# in_file = open(FILE_NAME)
# for line in in_file:
#     print(line)
# # line = in_file.readlines()
# in_file.close()
# # print(line)

# in_file = open(FILE_NAME)
# line = in_file.read()
# first_number = int(line.strip().split()[0])
# second_number = int(line.strip().split()[1])
# add = first_number + second_number
# in_file.close()
# print(add)

INITIAL_TOTAL = 0

in_file = open(FILE_NAME)
# convert file content to list of integers
for line in in_file:
    parts = line.strip().split(',')
    number = int(parts[0])
    INITIAL_TOTAL += number
in_file.close()
print(INITIAL_TOTAL)


