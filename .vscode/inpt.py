text = input("Input your favorite language")

try:
    with open("favorite.txt", 'w') as fl:
        fl.write(text)
except Exception as e:
    print("There is a problem", str(e))

try:
    with open("favorite.txt", 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")