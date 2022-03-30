#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
b = float(input("What was the total bill? $"))
t = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
(t / 100)
s = int(input("How many people to split the bill? "))
aa = (b / s)
new_aa = (aa * t)/ 100 + aa
limited_c = "{:.2f}".format(new_aa)
print(f"Each person should pay: ${limited_c}")