import urllib.request, urllib.parse, urllib.error
import re
filehandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()

for line in filehandle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
# for line in filehandle:
#     print(line.decode().strip())
