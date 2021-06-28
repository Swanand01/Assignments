def calculate_cost(guests, location, time, choose_hotel=0, hotel_type=None, pack_lunch=0):
    quote_info = f""
    if location == "Cliffs of Moher":
        travel_cost = 55
    elif location == "Kylemore Abbey":
        travel_cost = 50
    elif location == "Bunratty Castle":
        travel_cost = 75
    elif location == "The Burren":
        travel_cost = 45
    elif location == "Connemara":
        travel_cost = 75
    elif location == "Belmullet":
        travel_cost = 99
    travel_cost *= int(guests)
    quote_info += f"Guests: {guests}, "
    quote_info += f"\nDestination: {location}, cost: {travel_cost}. "

    if time == '7.00':
        discount = 0.2
    elif time == '8.00':
        discount = 0.1
    elif time == '9.00':
        discount = 0.05
    elif time == '13.00':
        discount = 0.25
    else:
        discount = 0
    quote_info += f"\nDeparture: {time}. "

    if choose_hotel == 1:
        if hotel_type == '3 Star':
            hotel_cost = 55
        elif hotel_type == '4 Star':
            hotel_cost = 75
        elif hotel_type == '5 Star':
            hotel_cost = 100
        hotel_cost *= int(guests)
        quote_info += f"\nHotel: {hotel_type}, cost: {hotel_cost}. "
    else:
        hotel_cost = 0

    if pack_lunch == 1:
        lunch_cost = 11.50
        lunch_cost *= int(guests)
        quote_info += f"\nLunch packed for {int(guests)}, cost: {lunch_cost}. "
    else:
        lunch_cost = 0

    total_cost = travel_cost + hotel_cost + lunch_cost
    total_cost = total_cost - total_cost * discount

    if int(guests) >= 3 and choose_hotel == 1 and pack_lunch == 1:
        total_cost = total_cost - total_cost * 0.075
    total_cost = round(total_cost, 2)
    quote_info += f"\nTotal: {total_cost}"
    return quote_info, total_cost
