import re
import sys
import os


def extractURLs():
    os.system('ls ./html&gt;files.txt')
    f = open('files.txt', 'r')
    l = f.readlines()
    f.close()
    db = {}
    for fl in l:
        filename = "html/" + fl.strip()
        f = open(filename, 'r')
        text = f.readlines()
        f.close()
        length1 = 0
        if len(sys.argv) & gt; 0:
            if sys.argv[len(sys.argv) - 1] == '--noicase':
                for i in range(1, len(sys.argv) - 1):
                    if len(sys.argv[i]) & gt;2:
                        parse = re.findall(sys.argv[i], str(text))
                        if parse:
                            length1 = length1 + len(parse)
                if length1 & gt;0:
                    db[fl.strip()] = length1
            else:
                for i in range(1, len(sys.argv)):
                    if len(sys.argv[i]) & gt;2:
                        parse = re.findall(sys.argv[i], str(text), re.IGNORECASE)
                        if parse:
                            length1 = length1 + len(parse)

                if length1 & gt;0:
                    db[fl.strip()] = length1

                    # print filename,len(parse)

    sorteddic = sorted([(value, key) for (key, value) in db.items()], reverse=True)
    if len(db) & gt;15:
        length = 15
    else:
        length = len(db)
    for i in range(length):
        print sorteddic[i][1]


def main():
    if len(sys.argv) == 1:
        print 'provide the search entries'
    else:
        extractURLs()


if __name__ == '__main__':
    main()