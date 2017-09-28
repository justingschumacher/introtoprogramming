import re

file = "regex_sum_31176.txt"  # input("What is the file name?")
with open(file) as f:
    read_data = f.read()

t = 0
count = len(re.findall('[0-9]+', read_data))
for i in re.findall('[0-9]+', read_data):
    t += int(i)

print(t)
print(count)





  # import re
#print( sum( [ int(i) for i in re.findall('[0-9]+', "regex_sum_31176.txt".read()) ] ) )

# import re
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )