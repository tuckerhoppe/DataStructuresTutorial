# overview
In sets order doesn't matter. It doesn't make a difference if an item was added first or last. There are also no duplicates. If an item is added multiple times, it will add it the first time and then ignore subsequent times where it is added. Very good performance on most operations

# advantages
Fast performance for adding, removing and finding. As mentioned earlier there are no duplicates and no order. This can be a huge advantage depending on the problem. Imagine a database that keeps track of students that are able to run a mile under 7 minutes:

```python
number_of_miles_ran = 7
student_name = input("Enter Student Name:  ")

# Create a set
7_minute_mile = set()

for i in range(number_of_miles_ran):
  mile_time = input("Enter mile time:  ")

  if mile_time <= 7:
    #add an item to the set
    7_minute_mile.add(student_name)
 
 print("These students are able to run a 7 minute mile:")
 print(7_minute_mile)
```

In this example once a mile time that is less than 7 minutes is entered the student is added to the set. If a student has multiple mile times that are less than 7 minutes it will still only add their name once. It will also not keep track of the order in which students met the goal of running a mile less than 7 minutes. It will only show a list of each student that has ran a 7 minute mile regardless of when it was done.

# disadvantages
Now Having no order and no duplicates could be a disadvantage depending on the problem. For example if there was a program keeping track of how many blue shirts were in stock at a clothing store, everytime a blue shirt was added, nothing would change. The shirt set would only have one blue shirt listed, regardless of the amount of times entered.

# Practice problem
Use sets to keep track of what items are offered at a grocery store
(Note: We don't care how many of each item, just if it is offered. We also don't care what order it was added to the inventory)

```python
#starting Code

items_shipped = input("Enter Number of Items shipped: ")

# Add any variables

for i in range(items_shipped):
  #enter code here


# Implement a way to see if an item is offered at the store


```


