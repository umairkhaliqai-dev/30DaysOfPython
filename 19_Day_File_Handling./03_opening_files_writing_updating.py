#"w" write (overwrites)

# "a" append

# "r+" read + write
with open("example.txt", "a") as f:
    f.write("\nNew line")
    
