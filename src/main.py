import os, glob

print("A simple test python app")
for i in range(200):
    print(f"{i} ", end=" ")
print()

print(os.listdir("."))
print(glob.glob("*.py"))
print(os.getcwd())
print("done.")
