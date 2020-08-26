def readDict(filename):
    lines = open(filename, 'r', encoding='utf8').readlines()
    dict = {}

    for i in range(len(lines)):
        s = lines[i].split("; ")
        dict[s[0]] = s[1]
    
    print(dict)
    return dict



readDict("ord.txt")