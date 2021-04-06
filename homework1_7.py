M = [1,9, 4,1, 1,3, 5,3]
val = [i for i in M if M.index(i)%2!=0]
key = [i for i in M if M.index(i)%2==0]
worder = {k:v for k,v in zip(key, val)}
print(worder)