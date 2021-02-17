

cost = int(input("Enter the cost of the item: "))
amount_paid = int(input("Enter the amount paid by the customer: "))

#logic for finding number of denominations required
change = amount_paid-cost
twenty = change//20
r = change % 20

ten = r//10
r = r % 10

five = r//5
r = r % 5

two = r//2
r = r % 2

one = r//1
r = r % 1

print("Change denominations: ")
print("&20 : ",twenty)
print("&10 : ",ten)
print("&5 : ",five)
print("&2 : ",two)
print("&1 : ",one)
print("Total change given = ", (twenty*20)+(ten*10)+(five*5)+(two*2)+(one*1),"$")
















