letter = '''Hello |name|
You are |age| years old
greetings from |abc| company!'''

name = input("Enter your name : ")
letter = letter.replace("|name|", name)

age = (input("Enter age : "))
letter = letter.replace("|age|", age)

company = input("Enter company name : ")
letter = letter.replace("|abc|", company)

print(f"\n{letter}")
