print("What is your name?",end=' ')
Name = input()
print("How many hours did you work this week?", end=' ')
h = int(input())
print("What is your hourly pay rate?", end =' ')
payRate = float(input())
grossPay = int(h)*float(payRate)
bonus = 500
grossPay=grossPay+bonus
print ("Hello " + Name)
print("Your gross pay is $", grossPay)