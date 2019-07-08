with open('test.txt','r') as fr:
    with open('test2.txt','w') as fw:
        for line in fr:
            fw.write(line)
