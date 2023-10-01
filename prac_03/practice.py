# FILE = "print_hash_lines.txt"
# in_file = open(FILE)
# print(in_file.read(20))
# in_file.read(34)
# print(in_file.read(20))
# print(in_file.read(10))
# in_file.read(23)
# in_file.close()

"""Write code to read a file like this and print each
part separately with the price formatted like currency"""

with open("data.txt", "r") as in_file:
    # in_file.readline()  # ignore header
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        release_year = parts[1]
        price = parts[2]
        print(f" Guiter {name} is released in {release_year} and has a price of ${price}")
