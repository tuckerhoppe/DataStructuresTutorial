# Stacks

## overview
A stack is a Last in First out data structure. (LIFO: Last in - First Out)When you take a piece of data from the stack it was the last in. Imagine a pile of papers. The last piece of paper you put onto the stack will be the first one you pick up, because it is on top.

## Common Operations
All of these operations are 0(1). This means all of these operations are incredibly efficient
Adding a value to the stack. This operation adds it to the top of the stack.
```python
stack1.append(value)
```

Removing a value from the stack. This removes a value from the top of the stack.
```python
stack1.pop()
```

Find the size of the stack.
```python
length = len(stack1)
```

Finding if a stack is empty
```python
if len(stack1) == 0:
  return True
```
## advantages
A stack can help you keep track of order of when items were put in the data. Imagine a program to help someone stay productive by helping keep track of what they were doing.

```python
things_done = []

things_done.append("Shower")
things_done.append("go to class")
things_done.append("work on HW")
things_done.append("go on phone")
things_done.append("watch YouTube")
things_done.append("Nap")
things_done.append("Go to Park")

pondering_day = "y"

Print("The last thing you were doing was...")
While pondering_day == "y":
  print(things_done.pop())
  
  pondering_day = input("Still looking back? (y or no): ")
  print("before that was")
  
```

This program will help the user see what the last thing they were doing was, and where they might have lost focus. Notice the append method: it adds something to the top of the stack. Also take note of the pop method: it takes from the top of the stack.

## disadvantages
If data items need to be used sooner rather than later it might not be a great data structure. For example a grocery store system might not benefit form a stack. Every time a shipment of milk was brought in it would be the first shippment used and put on the shelves. The very first shippment would most likely get very old.
## Practice
Stacks can be useful for undo functions, notes apps, strings, and internet browsers. Write a program that allows the user to write a message and undo words from the message as it goes. Here is the starting code:

```python
# Starting Code

# Create a stack


letter = "o"
print("enter (undo) to remove the last thing entered from the stack")
print("enter x to exit and print you stack")

while letter != "x"
  letter = input()
  # Add Your code here
    
print(letters)

  
```

