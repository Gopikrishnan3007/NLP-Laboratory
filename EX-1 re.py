import re

def sam (p,t):
    matches = re.findall(p,t)

    if matches :
        print("Word Patterns Detected:")
        for match in matches:
            print(match)
    else:
        print("No Word Patterns Detected:")

sample_input = [
    ("[0-9]+","The price is $25 and the quantiity is 10."),
    ("[A-Z][a-z]+","John and Alice went tto the park."),
    ("[aeiou]+","The quick brown fox jumps over the lazy dog."),
    ("[0-9]{2}-[0-9]{2}-[0-9]{4}","The date is 12-30-2023."),
    ("[A-Za-z]+","12345 is a number"),
]

for pattern,text in sample_input:
    print("Pattern:",pattern)
    print("Text:",text)
    sam(pattern,text)
    print("------------------------END------------------------")
    
