#import modules
from tkinter import *
import random

#GUI for random food generator
app = Tk()
app.option_add("*Font", "roboto 20")
app.title("Random Food Generator")
app.geometry('1000x500') 


#logo
photo = PhotoImage(file='applogo.png')
labelphoto = Label(app, image = photo)
labelphoto.pack()

#click button to get random food
def clickfood():
    myLabel = Label(app, text= food_random, font='Roboto 40 bold', bg= "#f2ebec", fg="#705d5f" )
    myLabel.pack()

def reset():
    app.destroy()
    
    
myButton = Button(app, text="Click to random", command=clickfood).pack()
myButton2 = Button(app, text= "Exit", command= reset).pack()


#create food list
food_list=['Pad Thai', 'Cheeseburger', 'Ramen', 'Pepperoni Pizza', 'Fried Chicken',
'Omelet', 'Caesar Salad', 'Pumpkin Soup', 'Onion Soup', 'Spaghetti', 'Papaya Salad', 'Tuna Salad',
'Burrito', 'Taco', 'Kimchi Fried Rice', 'Tokpokki', 'Kimchi Soup', 'Poke bowl', 'French fries',
'Dim Sum', 'Lahpet', 'Pho', 'Fish & Chips', 'Japanese Curry', 'Bulgogi', 'Meat pie', 'Chicken Tikka',
'Chicken Boneless Strips', 'Sashimi', 'Fajitas', 'Green Curry', 'Thai Egg Stew', 'Macaroni', 'Lasagna',
'Grilled Chicken', 'Greek Salad', 'Salmon with Lemon', 'Bibimbap', 'Gyoza', 'Cheese Grilled Sandwich',
'Thai Fish Cakes', 'Prawn Spring Rolls' ]

food_random = random.choice(food_list)

#start the program
app.mainloop()
