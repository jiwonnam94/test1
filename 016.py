fr = open('test.txt', 'r')
r = fr.readlines()


for s in r:
    print(s.strip())

fr.close()




'''
with open("test.txt", 'r') as fr:
    for line in fr:
        print(line.strip())
'''

