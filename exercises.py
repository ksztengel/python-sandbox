# exercise 1
temperatures = [10,-20,-289,100]
def celsius_to_farhernheit(celsius):
    if celsius < -273.15:
        return "That temp doesn't make sense!"
    else:
        fahrenheit = (celsius*9)/5 + 32
        return fahrenheit
for temp in temperatures:
    print(celsius_to_farhernheit(temp))

# exercise 2
# print 10

money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}

print(money["under_bed"][1])
