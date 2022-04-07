p = 5
count = 0
n=1

while count <p:
    ele = 5*n+3
    if((ele%7)==0):
        continue
    else:
        count+=1
        n+=1
        print(ele)
        