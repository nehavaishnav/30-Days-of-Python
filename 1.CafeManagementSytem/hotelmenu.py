menu={
    'Onion Pizza':80,
    'Cold Coffee':50,
    'Pasta':60,
    'Burger':80,
    'Aloo Parantha':30,
    'Vanilla Shake':60,
    'Hot Coffee':30
    
}
print ("Welcome to our Cafe!\n")
print ("Here's our Menu:\nOnion Pizza:80\nCold Coffee:50\nPasta:60\nBurger:80\nAloo Parantha:30\nVanilla Shake:60\nHot Coffee:30")
order_total = 0
item_1=input("Enter the name of the item you want to order= \n")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your order of {item_1} has been added.")
else:
    print(f"Ordered item {item_1} is not available yet")
another_order = input("Do you want to add another order? (Yes/No)")

if another_order=="Yes":
 item_2=input("Enter the second item to be ordered = ")
 if item_2 in menu:
    order_total +=menu[item_2] 
    print(f"Item {item_2} has been added to your order")
 else:
   print(f"Ordered item {item_2} is not available yet")

print(f"The total amount of items to pay is {order_total}")

