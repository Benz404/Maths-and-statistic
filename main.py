import math
def statistic(list):
    list.sort()
    largest=0
    smallest=list[0]
    size=len(list)
    median=mid(list)
    mode1=mode(list)
    sum=0
    for i in list:
        sum=sum+i
        if i>largest:
            largest=i
    for i in list:
        if i<smallest:
            smallest=i
    mean=sum/size


    print("sum :",sum)
    print("total item :",size)
    print("median :",median)
    print("mode :",mode1)
    print("mean :",mean)
    print("smallest item :",smallest)
    print("largest item :",largest)
    print("The quartiles are :",quart(list))
def mid(list):
    median=0
    size=len(list)
    if size%2!=0:
        x=list[int(((size+1)/2)-1)]
        median=x;
    else:
        x=list[int(((size)/2)-1)]
        y=list[int(size/2)]
        z=((x+y)/2)
        median=z;
    return median
def mode(list):
    return max(set(list), key=list.count)
def quart(list):
    list.sort()
    N=len(list)
    Q1_term=((N+1)/4)
    q1num1=math.floor(Q1_term)
    q1num2=math.ceil(Q1_term)
    rem1=Q1_term-q1num1
    Q1=list[int(q1num1-1)]+rem1*(list[int(q1num2-1)]-list[int(q1num1-1)])
    
    Q2_term=((N+1)/2)
    q2num1=math.floor(Q2_term)
    q2num2=math.ceil(Q2_term)
    rem2=Q2_term-q2num1
    Q2=list[int(q2num1-1)]+rem2*(list[int(q2num2-1)]-list[int(q2num1-1)])
    
    Q3_term=(3*(N+1)/4)
    q3num1=math.floor(Q3_term)
    q3num2=math.ceil(Q3_term)
    rem3=Q3_term-q3num1
    Q3=list[int(q3num1-1)]+rem3*(list[int(q3num2-1)]-list[int(q3num1-1)])
    
    return(Q1,Q2,Q3)
def factorial(n):
	i=1
	result=1
	while(i<=n):
		result=result*i
		i=i+1
	return result
        