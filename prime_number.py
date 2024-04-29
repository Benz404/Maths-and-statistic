def is_prime(num):
    if num<2:
        return False
    else:
        for i in range(2,num):
            if num%i==0:
                return False
            else:
                return True
while True:            
    print("Please enter a value");
    x=int(input())
    if is_prime(x):
        print (x," is a prime number");
        print(" ");
        print(" ");
    else:
        print (x," is not a prime number")
        print(" ");
        print(" ");
