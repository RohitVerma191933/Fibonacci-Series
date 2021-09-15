import time
n=int(input("ENTER NUMBER UPTO YOU WANT FIBONACCI SERIES : "))
x=0
y=1
z=0
start=time.time()
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y

end=time.time()
execution_time=end-start
print("THE EXECUTION TIME IS  : ",execution_time)
