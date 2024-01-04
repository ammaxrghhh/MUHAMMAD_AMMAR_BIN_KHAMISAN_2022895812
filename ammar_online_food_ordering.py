import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector

# Food and drink prices
food_prices = {'Basic Burger': 3.0, 'Special Burger': 5.0, 'King Burger': 7.0, 'Giant Burger': 10.0,
               'Gigantic Burger': 15.0, 'Luxury Golden Burger': 18.0, 'Demon Spicy Burger': 20.0}

drink_prices = {'Mineral Water': 1.0, 'Coke': 2.0, 'Sprite': 2.0, 'Orange Juice': 3.0,
                'Lemon Tea': 3.0, 'Sparkling Grape': 5.0, 'Mountain Dew': 6.0}

# Cart lists
food_cart = []
drink_cart = []


def update_cart(action, item=None, cart=None, text_var=None, listbox=None):
    global food_items, drink_items, total_price, delivery_time_hours_combobox, delivery_time_minutes_combobox

    if action == 'add':
        cart.append(item)
        listbox.insert(tk.END, item)
        calculate_total_price(text_var)
    elif action == 'cancel':
        selected_indices = listbox.curselection()
        canceled_items = [cart[index] for index in selected_indices if index < len(cart)]

        for index in reversed(selected_indices):
            if index < len(cart):
                del cart[index]

        listbox.delete(0, tk.END)
        for item in cart:
            listbox.insert(tk.END, item)

        # Subtract the price of canceled items from the total price
        canceled_price = sum(food_prices.get(item, 0) + drink_prices.get(item, 0) for item in canceled_items)
        new_total_price = max(float(Total_price.get().split('RM')[1]) - canceled_price, 0)
        Total_price.set(f'Total Price: RM{new_total_price:.2f}')
    elif action == 'submit':
        
        if not (customer_name_entry.get() and phone_number_entry.get() and delivery_location_entry.get() and
                delivery_date_entry.get() and delivery_time_hours_combobox.get() and delivery_time_minutes_combobox.get()):
            messagebox.showerror('Error', 'Please fill in all required fields.')
            return

        food_items = ', '.join(food_cart)
        drink_items = ', '.join(drink_cart)
        total_price = sum(food_prices.get(item, 0) for item in food_cart) + sum(drink_prices.get(item, 0) for item in drink_cart)

        customer_name = customer_name_entry.get()
        phone_number = phone_number_entry.get()
        Cart = ', '.join([cart_listbox.get(i) for i in range(cart_listbox.size())])
        delivery_location = delivery_location_entry.get()
        delivery_date = delivery_date_entry.get()
        delivery_time_hours = delivery_time_hours_combobox.get()
        delivery_time_minutes = delivery_time_minutes_combobox.get()
        additional_notes = additional_notes_entry.get()

        # Connect with the mysql database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="online_food_ordering"
        )

        mycursor = mydb.cursor()

        # Insert order informations into the database
        sql = "INSERT INTO customer_order (customer_name, phone_number, Cart, delivery_location, delivery_date, delivery_time_hours, delivery_time_minutes, additional_notes, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (customer_name, phone_number, Cart, delivery_location, delivery_date, delivery_time_hours,
               delivery_time_minutes, additional_notes, total_price)
        mycursor.execute(sql, val)
        mydb.commit()

        # Display a messagebox with the confirmation message
        confirmation_message = f'Your order has been received! Thank you for ordering with us!\n\n' \
                               f'Menu Ordered: {food_items}, {drink_items}\n' \
                               f'Total Price: RM{total_price:.2f}\n' \
                               f'Delivery Date: {delivery_date_entry.get()}\n' \
                               f'Delivery Time: {delivery_time_hours_combobox.get()}:{delivery_time_minutes_combobox.get()}\n' \
                               f'Delivery Location: {delivery_location_entry.get()}\n\n' \
                               f'Additional Notes: {additional_notes_entry.get()}\n\n' \
                               f'Please get ready the amount, we will call you before delivery to make sure you able to pickup the order.'
        messagebox.showinfo('Order Confirmation', confirmation_message)

        # Reset the cart and clear the entries for insert new order of another customers
        cart.clear()
        listbox.delete(0, tk.END)
        customer_name_entry.delete(0, tk.END)
        phone_number_entry.delete(0, tk.END)
        delivery_location_entry.delete(0, tk.END)
        delivery_date_entry.delete(0, tk.END)
        delivery_time_hours_combobox.set('')
        delivery_time_minutes_combobox.set('')
        additional_notes_entry.delete(0, tk.END)
        Total_price.set('Total Price: RM0.00')  # Reset total price

def calculate_total_price(text_var):
    food_total = sum(food_prices[item] for item in food_cart)
    drink_total = sum(drink_prices[item] for item in drink_cart)
    new_total_price = food_total + drink_total
    text_var.set(f'Total Price: RM{new_total_price:.2f}')


# The GUI setup
root = tk.Tk()
root.title('ONLINE FOOD ORDERING AND DELIVERY')
root.configure(bg='light green')
root.geometry('700x600')  # This the GUI size

# The Canvas of GUI
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# The vertical scrollbar to scroll the GUI
scrollbar = ttk.Scrollbar(root, orient='vertical', command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the Canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

# The Frame inside the Canvas
frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')

# The giant title of my burgershop (BOB BURGER SURRR )
title_label = ttk.Label(frame, text="   Bob Burger Surrr   ", font=('Matura MT Script Capitals', 28, 'bold'),
                        background=('light blue'))
title_label.grid(row=0, column=0, padx=40, pady=20, sticky='n')

# Customer Information Section
customer_frame = ttk.LabelFrame(frame, text='Customer Information', labelanchor='n')
customer_frame.grid(row=1, column=0, padx=10, pady=10, sticky='n')

# customer name
customer_name = ttk.Label(customer_frame, text='Name:')
customer_name.grid(row=0, column=0, sticky='e', padx=5)
customer_name_entry = ttk.Entry(customer_frame)
customer_name_entry.grid(row=0, column=1, padx=5)

# customer phone numbers
phone_number = ttk.Label(customer_frame, text='Phone Number:')
phone_number.grid(row=1, column=0, sticky='e', padx=5)
phone_number_entry = ttk.Entry(customer_frame)
phone_number_entry.grid(row=1, column=1, padx=5)

# Food and Drink Sections
food_frame = ttk.LabelFrame(frame, text='Food Options', labelanchor='n')
food_frame.grid(row=3, column=0, padx=10, pady=10, sticky='n')

food_dropdown = ttk.Combobox(food_frame, values=list(food_prices.keys()), state='readonly')
food_dropdown.grid(row=0, column=0, pady=5)

add_food_button = ttk.Button(food_frame, text='Add Food to Cart',
                             command=lambda: update_cart('add', food_dropdown.get(), food_cart, Total_price,
                                                        cart_listbox))
add_food_button.grid(row=1, column=0, pady=5)

drink_frame = ttk.LabelFrame(frame, text='Drink Options', labelanchor='n')
drink_frame.grid(row=3, column=1, padx=10, pady=10, sticky='n')

drink_dropdown = ttk.Combobox(drink_frame, values=list(drink_prices.keys()), state='readonly')
drink_dropdown.grid(row=0, column=0, pady=5)

add_drink_button = ttk.Button(drink_frame, text='Add Drink to Cart',
                              command=lambda: update_cart('add', drink_dropdown.get(), drink_cart, Total_price,
                                                         cart_listbox))
add_drink_button.grid(row=1, column=0, pady=5)

# Display the Food and Drink Prices list
prices_text = scrolledtext.ScrolledText(frame, width=30, height=5, wrap=tk.WORD)
prices_text.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
prices_text.insert(tk.INSERT, "Food Prices:\n")
for food, price in food_prices.items():
    prices_text.insert(tk.INSERT, f"{food}: RM{price:.2f}\n")

prices_text.insert(tk.INSERT, "\nDrink Prices:\n")
for drink, price in drink_prices.items():
    prices_text.insert(tk.INSERT, f"{drink}: RM{price:.2f}\n")

# Make the prices_text widget non-editable 
prices_text.config(state=tk.DISABLED)

# Cart Section
Cart = ttk.LabelFrame(frame, text='Cart', labelanchor='n')
Cart.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky='n')
cart_listbox = tk.Listbox(Cart, selectmode=tk.MULTIPLE, height=5)
cart_listbox.grid(row=0, column=0, pady=5)

cancel_cart_button = ttk.Button(Cart, text='Cancel Cart',
                                command=lambda: update_cart('cancel', None, food_cart + drink_cart, Total_price,
                                                           cart_listbox))
cancel_cart_button.grid(row=1, column=0, pady=5)

Total_price = tk.StringVar()  # Variable to store the total price
confirmation_label = ttk.Label(Cart, text='', font=('Helvetica', 12), textvariable=Total_price)
confirmation_label.grid(row=2, column=0, pady=5)

# Delivery Information Section
delivery_information = ttk.LabelFrame(frame, text='Delivery Information', labelanchor='n')
delivery_information.grid(row=5, column=0, padx=10, pady=10, columnspan=2, sticky='n')

# delivery location 
delivery_location = ttk.Label(delivery_information, text='Delivery Location:')
delivery_location.grid(row=0, column=0, sticky='e', padx=5)
delivery_location_entry = ttk.Entry(delivery_information)
delivery_location_entry.grid(row=0, column=1, padx=5)

# delivery date
delivery_date = ttk.Label(delivery_information, text='Delivery Date:')
delivery_date.grid(row=1, column=0, sticky='e', padx=5)
delivery_date_entry = DateEntry(delivery_information, width=17, background='darkblue', foreground='white',
                                borderwidth=2)
delivery_date_entry.grid(row=1, column=1, padx=5, rowspan=2)  # Spanning multiple rows of the calender

# For time I using the 24hours formats
delivery_time = ttk.Label(delivery_information, text='Delivery Time:')
delivery_time.grid(row=1, column=2, sticky='e', padx=5)

# Time Entry (Hour)
delivery_time_hours_combobox = ttk.Combobox(delivery_information, values=[f"{hour:02d}" for hour in range(10, 22)],
                                            state='readonly', width=3)
delivery_time_hours_combobox.grid(row=1, column=3, padx=2)

# Time Entry (Minute)
delivery_time_minutes_combobox = ttk.Combobox(delivery_information,
                                              values=[f"{minute:02d}" for minute in range(0, 60, 5)],
                                              state='readonly', width=3)
delivery_time_minutes_combobox.grid(row=1, column=4, padx=2)

# Additional Notes for customers to add any additional request before proceed order
additional_notes = ttk.Label(delivery_information, text='Additional Notes:')
additional_notes.grid(row=3, column=0, sticky='e', padx=5)
additional_notes_entry = ttk.Entry(delivery_information)
additional_notes_entry.grid(row=3, column=0, columnspan=4, padx=5, pady=10)

# Submit Order Section
submit_frame = ttk.Frame(frame)
submit_frame.grid(row=6, column=0, padx=10, pady=10, columnspan=2, sticky='n')

submit_button = ttk.Button(submit_frame, text='Submit Order', command=lambda: update_cart('submit'))
submit_button.grid(row=0, column=0, pady=10)

root.mainloop()
