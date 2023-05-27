#!/usr/bin/env python3
import sys

filePath = sys.argv[1]

with open(filePath, 'r') as f:
    text = f.read()

chunks = text.split('\n\n')

for i, x in enumerate(chunks):
    with open(f'{i}.md', 'w') as f:
        f.write(x)


