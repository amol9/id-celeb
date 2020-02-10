import json
import sys

list_fn = sys.argv[1]

celeb_list = None

with open(list_fn, "r") as f:
    celeb_list = f.read().splitlines()

c = 0
d = {}

for celeb in sorted(celeb_list):
    d[c] = celeb
    c += 1

print(json.dumps(d, indent=0))