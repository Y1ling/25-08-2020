# open a local file
f = open(r"C:\Users\shouy\Desktop\abc.txt", 'w')

#write the content into the file
num = f.write( "sfdsdfsadfs" )

#print the returned string number
print(num)
# close the file
f.close()

#open the file again
d = open(r"C:\Users\shouy\Desktop\abc.txt", 'r')

#read and display the content in the file
print(d.read())

#close the file
d.close()
