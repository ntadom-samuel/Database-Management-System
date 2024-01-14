import random
from functions import delay

print("Welcome, master Samuel🙇")
delay(0.5)
admin_name = input("Who would you like to add as an admin?\n").strip()
arr = "2tsvwu5quhg%#^styqiw%&*$u4w6rwu8twgy9w7uwgxdtysrtdiy7strsy5#$%^@%^JY"
password = ""

for i in range(0, 10):
    password += arr[random.randint(1, len(arr)-1)]

file = open("admin_login.txt", "a")
file.write(f"USERNAME: {admin_name}. PASSWORD: {password}.\n")


print("Generating password...")
delay(0.7)
print(f"{admin_name} is a new admin. Their password is {password}")
