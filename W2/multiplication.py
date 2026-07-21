#打印99乘法表，行打印
for i in range(1,10):#外层控制第二个数
    for j in range(1,i+1):#内层控制第一个数
        print(f"{j}*{i}={i*j}",end="\t")
    print()        