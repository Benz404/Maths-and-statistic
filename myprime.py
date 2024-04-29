def isprime(num):
    if num<2:
        return False
    else:
        for i in range(2,num):
            if num%i==0:
                return ("no")
            else:
                return ("yes")
