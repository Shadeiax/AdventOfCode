import re

string = "(10x8)(5x3)ABCDEFGHIJ"



def find_marker(string):
    return re.search(r"\((\d+)x(\d+)\)", string)

def find_all_markers(string):
    markers = []
    x = find_marker(string)
    if x:
        markers.append(x)
        print(x.end())
        return markers + find_all_markers(string[x.end():])
    else:
        print("done")
        return markers


x = find_all_markers(string)
print(x)