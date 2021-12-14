

def fun1():
    p = open("clean_pos.csv",'r')
    n = open("clean_neg.csv",'r')

    new = open('final.csv','w')

    pos = p.readlines()
    neg = n.readlines()

    print(len(pos))
    print(len(neg))
    print(type(pos))
    print(pos[:5])
    cnt=0
    for i in range(49840):
        cnt+=1
        pp = str(cnt)+','+pos[i].strip()
        cnt+=1
        nn = str(cnt) + ',' + neg[i].strip()

        new.write(pp)
        new.write('\n')
        new.write(nn)
        new.write('\n')

    p.close()
    n.close()


def fun2():
    fp=open('newtrainingdata.csv','r')
    data = fp.readlines()
    print(data[:10])

# fun2()

