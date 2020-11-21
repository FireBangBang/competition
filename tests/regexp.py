import re

line = "em+-f+n,-.9230vi8-/8"
one = re.sub(r"[^0-9+-]*", "", line, re.M | re.I)
print(one)
two = re.search(r"[+|-]?[1-9][0-9]*", one, re.M | re.I)
print(two)
