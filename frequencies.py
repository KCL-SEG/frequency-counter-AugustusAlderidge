"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if str(item) not in frequencies:
            frequencies[str(item)] = 1
        else:
            frequencies[str(item)] += 1



    return frequencies

#print(frequencies([100, 'Hello', '100', '100', 100]))
