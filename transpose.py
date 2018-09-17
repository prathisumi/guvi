def trans(x):
 n=x
 for i in range(len(x)):
   for j in range(len(x)):
     n[i][j]=x[j][i]
 print(n)
