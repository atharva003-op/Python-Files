text = input("Enter some text : ")
print(text)

pattern = input("Enter pattern to replace : ")

if pattern in text:
    new_pattern = input("Enter new string : ")
    text = text.replace(pattern, new_pattern)
    print(f"\nUpdated text : {text}")
else:
    print("\nPattern not found!")
