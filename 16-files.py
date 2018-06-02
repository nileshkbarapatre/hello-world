#f = open("C:\Users\Nilesh\github\hello-world\demofile.txt","r")
f=open("c:\\Users\\Nilesh\\github\\hello-world\\demofile.txt")
print(f.read())

f=open("c:\\Users\\Nilesh\\github\\hello-world\\demofile.txt")
print(f.read(10))

print(f.readline())


#f=open("c:\\Users\\Nilesh\\github\\hello-world\\demofile.txt")
for x in f:
  print(x)
