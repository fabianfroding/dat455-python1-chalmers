import wordfreq
import sys
import urllib.request

# strip() to remove \n ...?

def main():
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    urlInput = False

    if arg2.startswith("http://") or arg2.startswith("https://"):
        urlInput = True
    
    inp_file1 = open(arg1)
    if urlInput:
        response = urllib.request.urlopen(arg2)
        inp_file2 = response.read().decode("utf8").splitlines()
    else:
        inp_file2 = open(arg2)
    
    numPrints = int(sys.argv[3])

    tokenizedLines = wordfreq.tokenize(inp_file2)
    tokenizedStopWords = wordfreq.tokenize(inp_file1)

    inp_file1.close()
    if not urlInput:
        inp_file2.close()
        
    frequencies = wordfreq.countWords(tokenizedLines, tokenizedStopWords)
    wordfreq.printTopMost(frequencies, numPrints)



main()