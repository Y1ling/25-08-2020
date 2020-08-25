# 打开一个文件
f = open(r"C:\Users\shouy\Desktop\abc.txt", 'w')

#将内容写入并覆盖进目标文件
num = f.write( "sfdsdfsadfs" )

#返回写入的字符数
print(num)
# 关闭打开的文件
f.close()

#重新打开该文件
d = open(r"C:\Users\shouy\Desktop\abc.txt", 'r')

#将文件里的内容显示出来
print(d.read())

#关闭文件
d.close()
