
# Method 1:
#Python program to count the number of coin combinations totaling up to one dollar
'''
coins include :
Silver dollar: 100 cents
Half dollar: 50 cents
quarter dollar: 25 cents
Dime: 10 cents
Nickel: 5 cents
Pennies: 1 cent
'''

pennie = 1
nickel = 5
dime = 10
quarter = 25
half = 50
silver = 100
combination = 0

for s in range(2):
    for h in range(3):
        for q in range(5):
            for d in range(11):
                for n in range(21):
                    for p in range(101):
                        if (s*silver)+(h*half)+(q*quarter)+(d*dime)+(n*nickel)+(p*pennie) == 100:
                            combination = combination + 1
                            break

print("Total combinations : " , combination)































