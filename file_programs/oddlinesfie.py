lines=[]
with open(r'C:\Users\cacet\OneDrive\Desktop\subi\s1-Python\file_programs\text1.txt',"r") as txt1:
    all_lines=txt1.readlines()
    for line in all_lines:
        lines.append(line)
    
with open('file_programs/text2.txt',"a") as txt2:
    for i in lines:
        if (lines.index(i)%2)!=0:
            txt2.write(i)