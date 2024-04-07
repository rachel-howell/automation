import random
import string

print("hi")

letters = string.ascii_lowercase
random_string = ''.join(random.choice(letters) for i in range(1,5))
print(random_string)

# with ("./new_file.txt", "w") as my_f:

