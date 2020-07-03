def printTopMost(frequencies, n):
    sorted_freq = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    count = 0
    for i in sorted_freq:
        if count < n:
            print(i[0].ljust(20), str(i[1]).rjust(5))
            count += 1



def countWords(words, stopWords):
    frequencies = {}
    for word in words:

        if word in frequencies:
            frequencies[word] = frequencies[word] + 1
        else:
            inStopWords = False
            for stopWord in stopWords:
                if word == stopWord:
                    inStopWords = True
            if not inStopWords:
                frequencies[word] = 1

    return frequencies



def tokenize(lines): 
    words = []

    for line in lines:
        start = 0
        while start < len(line):
            while start < len(line) and line[start].isspace():
                start = start + 1
            
            end = start
            if end < len(line):
                if line[end].isalpha():
                    while end < len(line) and line[end].isalpha():
                        end = end + 1
                    words.append(line[start:end].lower())

                elif line[end].isdigit():
                    while end < len(line) and line[end].isdigit():
                        end = end + 1
                    words.append(line[start:end])

                else:
                    words.append(line[end])
                    end = end + 1

            start = end

    return words