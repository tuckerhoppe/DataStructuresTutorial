
#Solution Code

items_shipped = input("Enter Number of Items shipped: ")
items_carried = set()
for i in range(items_shipped):
  item = input("Enter Item")
  items_carried.add(item)

mystery_item = input("What item would you like to check? ")

if mystery_item in items_carried:
  print("Yes we offer", mystery_item, "at this store")
else:
  print("We do not currently offer", mystery_item)

