path = input().split("\\")
filename_and_extension = path[-1]
filename, extension = filename_and_extension.split(".")
print(f"File Name: {filename}")
print(f"File Extension: {extension}")