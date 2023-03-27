command = "import os; print(open('flag.txt', 'r').read())"
chr_cmd = ""

for i in command:
    chr_cmd += f"chr({ord(i)})+"

print(chr_cmd)
