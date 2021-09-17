print("Name: Kushagra Patidar\nScholar Number: 30665")
import re
num = "07987549836" 
print("Initial number:",num)
pattern = r"9"
num = re.sub(pattern, "0",num) 
print("Number after substituion:",num)