#  Array Data Structure

exp = [{"January": 2200}, {"February": 2350},
       {"March": 2600}, {"April": 2130},
       {"May": 2190}]

print(exp)

print(type(exp))

#  In Feb, how may dollars spent extra compared to January?
jan_feb = exp[1]["February"] - exp[0]["January"]

print(f"The extra money in february compared to January is: {jan_feb}")

qrt1 = exp[0]["January"] + exp[1]["February"] + exp[2]["March"]

print(f"First quarter total expenses {qrt1}")

exp.append({"June: 1980"})
print(exp)

refund = exp[3]["April"] - 200
print(refund)

exp[3]["April"] = refund

print(exp)
False
exp = [{"January": 2200}, {"February": 2350}, {"March": 2600}, {"April": 2130}, {"May": 2190}]

# Check if 2000 was spent in any month
for month_exp in exp:
       for month, amount in month_exp.items():
              if amount == 2000:
                     print(f"2000 was spent in {month}.")
              else:
                     print('False')