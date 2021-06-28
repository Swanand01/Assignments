from tkinter import *
from tkinter import messagebox
from calculate_cost import calculate_cost

app = Tk()

location_frame = LabelFrame(app, text="Location", padx=10, pady=10)
location_frame.grid(row=0, column=1, sticky='we')

location = StringVar()
location.set("Cliffs of Moher")
Radiobutton(location_frame, variable=location,
            value="Cliffs of Moher", text="Cliffs of Moher").pack()
Radiobutton(location_frame, variable=location,
            value="Kylemore Abbey", text="Kylemore Abbey").pack()
Radiobutton(location_frame, variable=location,
            value="Bunratty Castle", text="Bunratty Castle").pack()
Radiobutton(location_frame, variable=location,
            value="The Burren", text="The Burren").pack()
Radiobutton(location_frame, variable=location,
            value="Connemara", text="Connemara").pack()
Radiobutton(location_frame, variable=location,
            value="Belmullet", text="Belmullet").pack()

time_frame = LabelFrame(app, text="Time", padx=10, pady=10)
time_frame.grid(row=0, column=0, sticky='we')

time = StringVar()
time.set("7.00")
Radiobutton(time_frame, variable=time,
            value="7.00", text="7.00").pack()
Radiobutton(time_frame, variable=time,
            value="8.00", text="8.00").pack()
Radiobutton(time_frame, variable=time,
            value="9.00", text="9.00").pack()
Radiobutton(time_frame, variable=time,
            value="10.00", text="10.00").pack()
Radiobutton(time_frame, variable=time,
            value="11.00", text="11.00").pack()
Radiobutton(time_frame, variable=time,
            value="13.00", text="13.00").pack()

booking_frame = LabelFrame(app, text="Bookings", padx=10, pady=10)
booking_frame.grid(row=3, column=0, sticky='we', columnspan=2)

booking_list = Listbox(booking_frame, width=115)
booking_list.pack(side=LEFT)

scrollbar = Scrollbar(booking_frame, orient="vertical")
scrollbar.config(command=booking_list.yview)
scrollbar.pack(side=RIGHT, fill="y")
booking_list.config(yscrollcommand=scrollbar.set)

guest_frame = LabelFrame(app, text="Guests", padx=10, pady=10)
guest_frame.grid(row=1, column=0, sticky='we')
guests = IntVar()
guest_entry = Entry(guest_frame, textvariable=guests).pack()

lunch_frame = LabelFrame(app, text="Lunch", padx=10)
lunch_frame.grid(row=1, column=1, sticky='we')
Lunchbutton = IntVar()
Button1 = Checkbutton(lunch_frame, text="Pack Lunch",
                      variable=Lunchbutton,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      width=10).pack()

hotel_frame = LabelFrame(app, text="Hotel", padx=10)
hotel_frame.grid(row=2, column=0, sticky='we')

hotel_type = StringVar()
hotel_type.set("3 Star")
h1 = Radiobutton(hotel_frame, variable=hotel_type,
                 value="3 Star", text="3 Star")
h2 = Radiobutton(hotel_frame, variable=hotel_type,
                 value="4 Star", text="4 Star")
h3 = Radiobutton(hotel_frame, variable=hotel_type,
                 value="5 Star", text="5 Star")


def hotel_list():
    if Hotelbutton.get() == 1:
        h1.pack()
        h2.pack()
        h3.pack()
    elif Hotelbutton.get() == 0:
        h1.pack_forget()
        h2.pack_forget()
        h3.pack_forget()


Hotelbutton = IntVar()
Button1 = Checkbutton(hotel_frame, text="Hotel",
                      variable=Hotelbutton,
                      command=hotel_list,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      width=10).pack()

button_frame = LabelFrame(app, text="Actions", padx=40)
button_frame.grid(row=2, column=1, sticky='nswe')


def show_quote():
    if guests.get() != 0:
        quote_info, total_cost = calculate_cost(guests=guests.get(), location=location.get(), time=time.get(
        ), choose_hotel=Hotelbutton.get(), hotel_type=hotel_type.get(), pack_lunch=Lunchbutton.get())
        messagebox.showinfo(
            "Quote", quote_info)
        return quote_info, total_cost
    else:
        messagebox.showerror("Error", "No. of guests cannot be 0")


app.total_booking_revenue = 0


def book():
    if guests.get() != 0:
        booking, booking_revenue = show_quote()
        app.total_booking_revenue += booking_revenue
        booking_list.insert(END, booking)
    else:
        messagebox.showerror("Error", "No. of guests cannot be 0")


def summary():
    if booking_list.size() != 0:
        average_revenue = round(
            app.total_booking_revenue / booking_list.size(), 2)
        messagebox.showinfo(
            "Summary", f"Total bookings: {booking_list.size()}\nTotal revenue: {app.total_booking_revenue}\nAverage revenue per booking: {average_revenue}")


def clear():
    booking_list.delete(0, END)
    app.total_booking_revenue = 0


Button(button_frame, text='Display', width=10,
       command=show_quote).pack(side=LEFT, padx=10)
Button(button_frame, text='Book', width=10,
       command=book).pack(side=LEFT, padx=10)
Button(button_frame, text='Summary', width=10,
       command=summary).pack(side=LEFT, padx=10)
Button(button_frame, text='Clear', width=10,
       command=clear).pack(side=LEFT, padx=10)
Button(button_frame, text="Exit", width=10,
       command=app.destroy).pack(side=LEFT, padx=10)

app.title('Booking Manager')
app.resizable(False, False)
app.mainloop()
