import tkinter as tk
from tkinter import ttk
import random

# Functions
# - Prints selected pizza size
# - Checks if there are toppings, and print which ones are selected
# - If you do strange inputs like only a tip, no pizza size and no toppings there are outputs that address the odd input

# Other Variables
root = tk.Tk()
PizzaSize = 0
SmallPrice = 10
MediumPrice = 15
LargePrice = 20
GlobalPrice = 0
ToppingTable = []
OliveChecked = False
MushroomChecked = False
BellPepperChecked = False
MushroomPrice = 2.5
OlivePrice = 2.5
BellPepperPrice = 2.5
Mushroom_price = 0 
Olive_price = 0 
BellPepper_price = 0
FinalPrice = 0
Toppings = " "
tax = 0.0
withTax = 0.0
Tip = 0

# Create a ttk style for Checkbuttons
style = ttk.Style()
style.configure("TCheckbutton", font=("HELVETICA", 11))

# FINAL LABELS ARE IN "ProceedToCheckout" FUNCTION

# IntVar initializing
PizzaSizeVar = tk.StringVar()
MushroomVar = tk.IntVar()
OliveVar = tk.IntVar()
BellPepperVar = tk.IntVar()

# RadioButton initializing
SmallSizeRadioButton = tk.Radiobutton(root, text="Small", font=("HELVETICA", 11), variable=PizzaSizeVar, value="Small")
MediumSizeRadioButton = tk.Radiobutton(root, text="Medium", font=("HELVETICA", 11), variable=PizzaSizeVar, value="Medium")
LargeSizeRadioButton = tk.Radiobutton(root, text="Large", font=("HELVETICA", 11), variable=PizzaSizeVar, value="Large")


# CheckButton initializing
MushroomCheckButton = ttk.Checkbutton(root, text="Mushroom", variable=MushroomVar, style="TCheckbutton")
OliveCheckButton = ttk.Checkbutton(root, text="Olive", variable=OliveVar, style="TCheckbutton")
BellPepperCheckButton = ttk.Checkbutton(root, text="Bell Pepper", variable=BellPepperVar, style="TCheckbutton")


# Label/Instruction Label initializing
SizeLabel = ttk.Label(root, text="Select a Pizza size: ", font="HELVETICA")
ToppingLabel = ttk.Label(root, text="Select Toppings: ", font="HELVETICA")
OrderSummaryLabel = ttk.Label(root, text="Order Summary: ", font="HELVETICA")
SelectedSizeLabel = ttk.Label(root, text="Size Selected: Nothing Selected", font="HELVETICA")
PriceLabel = ttk.Label(root, text="Total Price:", font="HELVETICA")
AddTipLabel = ttk.Label(root, text="Add a tip?", font="HELVETICA")
TipConfirmButton = tk.Button(root, text="Confirm", font="HELVETICA")
Line = ttk.Label(root, text="==============================", font="HELVETICA")

# Custom Tip Initializing
entry = tk.Entry(root)
entry.grid(row=12, column=0, sticky="w")

# ----------Create all RadioButtons, Checkbuttons, and Labels----------
# PIZZA SIZE SELECTION
SizeLabel.grid(row=0, column=0, sticky="w")
SmallSizeRadioButton.grid(row=1, column=0, sticky="w")
MediumSizeRadioButton.grid(row=2, column=0, sticky="w")
LargeSizeRadioButton.grid(row=3, column=0, sticky="w")

# TOPPINGS SELECTION
ToppingLabel.grid(row=4, column=0, sticky="w")
MushroomCheckButton.grid(row=5, column=0, sticky="w")
OliveCheckButton.grid(row=6, column=0, sticky="w")
BellPepperCheckButton.grid(row=7, column=0, sticky="w")

# ORDER SUMMARY
OrderSummaryLabel.grid(row=8, column=0, sticky="w")
SelectedSizeLabel.grid(row=9, column=0, sticky="w")
PriceLabel.grid(row=10, column=0, sticky="w")
AddTipLabel.grid(row=11, column=0, columnspan=1, sticky="nsew")
TipConfirmButton.grid(row=13, column=0, sticky="w")


def UpdateValues():
    
    global Tip, GlobalPrice, PizzaSize, FinalPrice, PriceLabel, OrderSummaryLabel, Toppings, PizzaSizeVar, OliveVar, MushroomVar, BellPepperVar
    
    FinalPrice = 0
    FinalPrice = GlobalPrice + PizzaSize
    
    if (entry.get() != ""):
        FinalPrice = FinalPrice
        Tip = float(entry.get())
        AddTipLabel.config(text=f"Add a tip? ${float(entry.get()):04.2f}")
    else:
        AddTipLabel.config(text="Add a tip? $0.00")
    
    PriceLabel.config(text=f"Total Price: ${FinalPrice:04.2f}")
    if ((OliveVar.get() == 0) & (MushroomVar.get() == 0) & (BellPepperVar.get() == 0)):
        Toppings = "No Toppings"
    elif (PizzaSizeVar.get() == ""):
        Toppings = "s and ".join(ToppingTable)
    else:
        Toppings = " and ".join(ToppingTable)
        
    OrderSummaryLabel.config(text=" ")
    
    if ((PizzaSizeVar.get() == "") & (Tip == 0)):
        OrderSummaryLabel.config(text=f"Order Summary: Just some {Toppings}s")
    elif ((PizzaSizeVar.get() == "") & (Tip != 0)):
        OrderSummaryLabel.config(text="Order Summary: Nothing")
    else:
        OrderSummaryLabel.config(text=f"Order Summary: {PizzaSizeVar.get()} Pizza with {Toppings}")
    
    print(f"FinalPrice: {FinalPrice}")


def SelectedSize(price): # Checks which size is selected

    global PizzaSize, PizzaSizeVar, GlobalPrice
    PizzaSize = price
    print(f"PizzaPrice: {PizzaSize}")
    SelectedSizeLabel.config(text=f"Size Selected: {PizzaSizeVar.get()} (${PizzaSize:04.2f})")
    
    UpdateValues()


def SelectedToppings():
    
    global MushroomVar, OliveVar, BellPepperVar, ToppingTable, MushroomPrice, OlivePrice, BellPepperPrice, GlobalPrice, MushroomChecked, OliveChecked, BellPepperChecked, Mushroom_price, Olive_price, BellPepper_price
    
    # Everything is set to 0 (table is emptied) so it won't add more once it's ran again
    ToppingTable = [] 
    Mushroom_price = 0
    Olive_price = 0
    BellPepper_price = 0
    
    # Topping Logic
    
    if (MushroomVar.get() == 1):
        ToppingTable.append("Mushroom")
        Mushroom_price = MushroomPrice
        MushroomChecked = True
    elif (MushroomChecked == True):
        Mushroom_price = -Mushroom_price
        MushroomChecked = False
        
    if (OliveVar.get() == 1):
        ToppingTable.append("Olive")
        Olive_price = OlivePrice
        OliveChecked = True
    elif (OliveChecked == True):
        Olive_price = -Olive_price
        OliveChecked = False
    
    if (BellPepperVar.get() == 1):
        ToppingTable.append("Bell Pepper")
        BellPepper_price = BellPepperPrice
        BellPepperChecked = True
    elif (BellPepperChecked == True):
        BellPepper_price = -BellPepper_price
        BellPepperChecked = False
    
    GlobalPrice = Mushroom_price + Olive_price + BellPepper_price
    print(f"Toppings: {GlobalPrice}")
    
    UpdateValues()


def ProceedToCheckout():
    
    global FinalPrice, tax, withTax, Tip
    tax = FinalPrice * 0.08
    withTax = tax + FinalPrice + Tip
    print(f"Price (w/o tax): ${FinalPrice} Total: ${withTax}(${tax} Tax)")
    for widget in root.winfo_children():
        widget.grid_remove()
    
   
    if ((PizzaSizeVar.get() == "") & (Toppings == "No Toppings") & ((Tip > 0) & (Tip < 50))):
        OrderSummaryLabel.config(text="Order Summary: Only a tip..?")
    elif ((PizzaSizeVar.get() == "") & (Toppings == "No Toppings") & (Tip >= 50)):
        OrderSummaryLabel.config(text="Order Summary: Just a big tip??? Thanks")
    elif ((PizzaSizeVar.get() == "") & ((Toppings == " ") or (Toppings == "No Toppings")) & (entry.get() == "")):
        OrderSummaryLabel.config(text="Order Summary: Was nothing appealing?")
    elif ((PizzaSizeVar.get() == "") & (Toppings != "")):
        OrderSummaryLabel.config(text=f"Order Summary: You only wanted {Toppings}s?") 
    else:
        OrderSummaryLabel.config(text=f"Order Summary: {PizzaSizeVar.get()} Pizza with {Toppings}")
    
    # Final Labels
    FinalOrderPrice = ttk.Label(root, text=f"Subtotal: {FinalPrice: 04.2f}")
    OrderWithTax = ttk.Label(root, text=f"Total: ${withTax:04.2f} (Tax: ${tax: 04.2f})")
    
    OrderSummaryLabel.grid(row=1, column=0, sticky="")
    Line.grid(row=2, column=0)
    FinalOrderPrice.grid(row=3, column=0)
    OrderWithTax.grid(row=4, column=0)

#---------------------------------------------------------------------------------
# I had to research these answers since I couldn't figure them out on my own
def update_tip(event=None):
    UpdateValues()
entry.bind("<KeyRelease>", update_tip)
#---------------------------------------------------------------------------------

# CALLING ALL FUNCTIONS
SmallSizeRadioButton.config(command= lambda: SelectedSize(SmallPrice))
MediumSizeRadioButton.config(command= lambda: SelectedSize(MediumPrice))
LargeSizeRadioButton.config(command= lambda: SelectedSize(LargePrice))
MushroomCheckButton.config(command= lambda: SelectedToppings())
OliveCheckButton.config(command= lambda: SelectedToppings())
BellPepperCheckButton.config(command= lambda: SelectedToppings())
TipConfirmButton.config(command= lambda: ProceedToCheckout())


root.mainloop()
