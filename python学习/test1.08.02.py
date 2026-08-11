"""
.read() count()
f = open("D:/ai-agent-journey/python学习/word.txt","r",encoding="UTF-8")
content = f.read()
count = content.count("itheima")
print(count)
"""
#读取内容一行行读取 
f = open("D:/ai-agent-journey/python学习/word.txt","r",encoding="UTF-8")
for line in f :
    line = line.strip( )
    words = line.split(" ")
    print(words)
