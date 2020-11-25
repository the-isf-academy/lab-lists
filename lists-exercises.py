# Unit 0 Lab 2
# Author: Your Name

from turtle import *

#VARIABLES
my_name = "Eva"
friend_name = "Wall-E"

meme_list = ["creeper?","aw man"]
cs1_dessert_list = ["ice cream", "brownies", "mochi", "timtams", "creme brulee", "mango sago", "pumpkin pie", "tiramisu", "cheesecake"]

# LIST EXPERIMENTS (A)
print("help! I am trapped inside the computer!")

# LOOPING THROUGH A LIST
# YOUR CODE HERE (B)
print("Mr. Wolf, Ms. Brown, and Mr. Chau go to the store for dessert. They decide to buy...")
for thing in cs1_dessert_list:
    print(thing)

# LOOPING THROUGH PART OF A LIST
# YOUR CODE HERE (B)
print("But then they realized they ran out of money, so they can only buy 4 desserts. They decide to buy...")
for i in range(5, 8):
    print(cs1_dessert_list[i])

