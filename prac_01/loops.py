for i in range(1, 21, 2):
    print(i, end=' ')
print()

# count in 10s from 0 to 100
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# count down from 20 to 1:
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# print n stars. Ask the user for a number, then print that many stars (*)
n = int(input("Number of stars: "))
for i in range(n):
    print("*", end='')
print()

# print n lines of increasing stars
n = int(input("Number of stars: "))
for i in range(1, n+1):
    print(i * "*")
"""
i was stuck on this last loop for a while, and 
suddenly i heard a little whisper in my head 
"make console you friend" so i did
and i was not stuck anymore.
To that voice in my head, may you keep on 
whispering code wisdom to me, when i am stuck.
"""


