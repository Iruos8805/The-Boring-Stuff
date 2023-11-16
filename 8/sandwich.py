import pyinputplus as pyip

total = 0.0
prices = {
    "wheat": 0.5, "white": 0.25, "sourdough": 0.75,
    "chicken": 0.5, "turkey": 0.45, "ham": 0.3, "tofu": 0.25,
    "cheddar": 0.15, "Swiss": 0.2, "mozzarella": 0.15,
    "mayo": 0.05, "mustard": 0.08, "lettuce": 0.03, "tomato": 0.01
}

order = {}
order["bread"] = pyip.inputMenu(["wheat", "white", "sourdough"], prompt='Preferred bread type?', numbered=True)
order["protein"] = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], prompt='Preferred protein type?', numbered=True)
Cheese = pyip.inputYesNo("Do you want cheese with that?")
if Cheese == "yes":
    order["cheese"] = pyip.inputMenu(["cheddar", "Swiss", "mozzarella"], numbered=True)
Dressing = pyip.inputYesNo("Would you like some dressing? ")
if Dressing == "yes":
    order["side"] = pyip.inputMenu(["mayo", "mustard", "lettuce", "tomato"], numbered=True)
orderNumber = pyip.inputInt("How many of those would you like? ", min=1)

for choice in order:
    if order[choice] in prices.keys():
        total += prices[order[choice]]
# Adjust if more than one
total *= orderNumber

print("Ok, that'll be $" + "{:.2f}".format(total) + " please!")
