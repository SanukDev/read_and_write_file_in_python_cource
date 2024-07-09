# Opening the file and save in a variable
# file = open("my_file.txt") or use
with open("my_file.txt") as file:
    # Reading the content in the file that was opened
    content = file.read()
    print(content)

# Writing in the file. To write you need add a "mode", because by pattern the mode is only "r" read. So add mode "w"
# write, but this will clear the other text,
# then add the  mode "a" of append that work of the  same form that "list.append"
with open("my_file.txt", mode="a") as file:
    file.write("\nI am 22 years old, and you?")

# To create a new file
with open("new_file.txt", mode="w",) as new_file:
    new_file.write("New text.")

    