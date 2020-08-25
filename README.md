输入与输出 
# 打开一个文件(文档的地址要改成自己电脑的）打开模式为只写入
f = open(r"C:\Users\shouy\Desktop\abc.txt", 'w')

#将内容写入并覆盖进目标文件
s = f.write( "sfdsdfsadfs" )

#返回写入的字符数
print(s)

# 关闭打开的文件
f.close()

#重新打开该文件
d = open(r"C:\Users\shouy\Desktop\abc.txt", 'r')

#将文件里的读取并显示出来
print(d.read())

#关闭文件
d.close()
