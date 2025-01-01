txt1=open("file_programs/text1.txt","r")
txt2=open("file_programs/text2.txt","a+")
str1=" "
count=1
while str1:
    str1=txt1.readline()
    if count%2!=0:
        txt2.write(str1)
    count+=1
txt2.seek(0)
str1=" "
while str1:
    str1=txt2.readline()
    print(str1)
txt1.close()
txt2.close()