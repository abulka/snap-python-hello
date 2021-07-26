import os, glob
import requests

print("A simple test python app")
for i in range(200):
    print(f"{i} ", end=" ")
print()

print(os.listdir("."))
print(glob.glob("*.py"))
print(os.getcwd())

print(requests.get('http://www.google.com').status_code)

print("done.")
