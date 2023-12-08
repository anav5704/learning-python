# Read
f = open("names.txt", "r")

for line in f:
    print(line)

f.close()

# Append
f = open("names.txt", "a")

f.write("\nNomi")

f.close()

# Write
f = open("names.txt", "w")

f.write("JasBean")

f.close()
