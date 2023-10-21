bill=float(input("What was the total bill? Rs."))
tip_percent=int(input("What percentage tip would ypu like to give? 10, 12 or 15? "))
ppl=int(input("How many people to split the bill? "))
total=bill+bill*tip_percent/100
amt_per_person=round(total/ppl,2)
print("Each person should pay: Rs",amt_per_person)