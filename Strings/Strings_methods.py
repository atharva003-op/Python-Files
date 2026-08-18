# Usefull String methods!!

name = "Atharva abc"

print(len(name)) # Returns the length of the string
print(name.capitalize()) # Returns the first character of string to Capital
print(name.upper()) # Returns the entire string to Upper-case
print(name.lower()) # Returns the entire string to Lower-case
print(name.title()) # Retunrs the first character to capital of all strings
print(name.endswith("abc")) # Returns true
print(name.endswith("rva")) # Returns false
print(name.startswith("Ath")) # Returns true
print(name.startswith("ath")) # Returns false (case-sensetive)
print(name.count("a")) # Returns the number of letter "a" present in string
print(name.find("va")) # Returns the index number from where "va" starts
print(name.replace("abc", "xyz")) # Replaces abc to xyz
