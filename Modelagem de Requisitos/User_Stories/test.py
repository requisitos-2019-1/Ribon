f = open('test.txt', 'a')

for i in range(0, 1000000):
    f.write(str(i)+'\n')

f.close()