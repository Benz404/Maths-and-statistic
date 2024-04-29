print("welcome To AstronX Finance Company");
print("please verify yourself");
print("please enter your name");
name=input();
print("please enter your password :");
password=input();
if name=="BANAJIT" and password=="EST19XXB":
    data=[]
    print("Welcome Banajit");
    print("please enter tadays date");
    print("format --  dd.mm.yy")
    date=input();
    print("enter your income :\n(if nothing then please enter 0.00)");
    income=int(input());
    print("enter your spending :\n(if nothing then please enter 0.00)");
    spend=int(input());
    profit=income-spend;
    net_date="date :",date;
    net_income="income :",income;
    net_spend="spend :",spend;
    net_profit="profit",profit;
    print("would you like to save it ?\n(yes --> y or no --> n )");
    choice=input();
    if choice=='y' or choice=='Y' :
        data.append(net_date);
        data.append(net_income);
        data.append(net_spend);
        data.append(net_profit);
        data.append("\n");
        with open('data.txt','a') as x:
            x.write(str(data));
        print("your data is stored successfully");
    elif choice=='n' or choice=='N':
        print("thank you so much !")
    else:
        print("invalid output!!!!!!!!!!")
        
else:
    print("Sorry! you enter wrong name or password");
