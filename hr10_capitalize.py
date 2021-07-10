#first word should have to be in Caps
s = input()
for i in s[:].split():
	s = s.replace(i,i.capitalize())
print(s)



