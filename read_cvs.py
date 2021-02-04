data=list("0123456789abcdefghijklmnopqrstuvwxyz")

def addtostring(mystring):
  for y in data:
    output.append(mystring+y)

output=[]
for x in data:
  addtostring(x)

print (output)
