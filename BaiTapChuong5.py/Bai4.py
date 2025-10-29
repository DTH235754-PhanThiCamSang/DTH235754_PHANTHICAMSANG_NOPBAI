import re

s = "  Hello, Python 3!  "
print(len(s))                # 19
print(s.strip())             # "Hello, Python 3!"
print(s.lower())             # "  hello, python 3!  "
print(s.replace("Python", "World"))
parts = s.strip().split(",") # ["Hello", " Python 3!"]
print(parts[1].strip())      # "Python 3!"
print(" - ".join(["a","b","c"]))  # "a - b - c"
print(s.find("Python"))      # 8
print(s.count("o"))          # 2
print(s.startswith("  He"))  # True
print("123".isdigit())       # True
name = "nguyen"
print(name.title())          # "Nguyen"
print(f"Len={len(s)}")       # f-string

# ordinal / encoding
print(ord("A"), chr(65))
print("á".encode("utf-8"))   # bytes

# regex example
m = re.findall(r"\d+", s)    # ['3']