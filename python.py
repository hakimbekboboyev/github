n = input("N=")
l = len(n)
k = 0
t = int(n)
q = ""
m=0
try:
    for i in range(l):
        if n[i]=="1":
            k = i
            while n[k]=="1":
                k = k+1
                q=n[k::]
                
            break

        if n[i]=="0":
            continue

    

    for i in range(len(q)):
            
        if q[i]=="0":
            continue
        if  q[i]=="1":
            m = m+1

    if m==0:
        print("YES")
    else:
        print("NO")
except IndexError:
    print("YES")

