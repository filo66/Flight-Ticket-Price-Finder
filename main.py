#                                               +
from datetime import datetime
from amadeus import Client
from customtkinter import *
from tkinter import messagebox

class Invalid(Exception):
    pass    

def main():
    global root
    root = CTk()
    root.geometry("700x500+370+100")
    root.title("Cheapest flight price")
    set_default_color_theme("dark-blue")
    set_appearance_mode("dark")
    input_frame()

def input_frame():

    global input_frm
    input_frm = CTkFrame(root)
    input_frm.pack(fill = BOTH , expand = True)

    origin_lbl = CTkLabel(input_frm , font=("arial" , 26) , text="Origin:")# label
    origin_lbl.place(relx = 0.1 , rely = 0.1)
    global input_origin
    input_origin = CTkEntry(input_frm , font=("arial" , 24))
    input_origin.place(relx = 0.22 , rely = 0.1 , relwidth = 0.4 , relheight = 0.1)

    des_lbl = CTkLabel(input_frm , font=("arial" , 26) , text="Destenation:")# label
    des_lbl.place(relx = 0.1 , rely = 0.3)
    global input_des
    input_des = CTkEntry(input_frm , font=("arial" , 24))
    input_des.place(relx = 0.32 , rely = 0.3 , relwidth = 0.4 , relheight = 0.1)

    departure_lbl = CTkLabel(input_frm , font=("arial" , 26) , text="Departure:")# label
    departure_lbl.place(relx = 0.1 , rely = 0.5)
    global input_departure
    input_departure = CTkEntry(input_frm , font=("arial" , 24))
    input_departure.place(relx = 0.3 , rely = 0.5 , relwidth = 0.4 , relheight = 0.1)

    adults_lbl = CTkLabel(input_frm , font=("arial" , 26) , text="Adults:")# label
    adults_lbl.place(relx = 0.1 , rely = 0.7)
    global input_adults
    input_adults = CTkEntry(input_frm , font=("arial" , 24))
    input_adults.place(relx = 0.3 , rely = 0.7 , relwidth = 0.4 , relheight = 0.1)

    #  find button

    button = CTkButton(input_frm , text="Find" , font = ("arial" , 30)
                    ,command=send_data)
    button.place(relx = 0.75 , rely = 0.84)

    root.mainloop()

def new_frame(o , d , t , a):
    # showing data frame
    global data_frm
    data_frm = CTkFrame(root)
    data_frm.pack(fill = BOTH , expand = True)

    # data labels
    try:
        data = get_data(o , d , t , a)
        price = data["price"]
        airline = data["airline"]
        flight_number = data["flight_number"]
        departure_time = data["departure_time"]
        arrival_time = data["arrival_time"]
    except:
        Exception_lbl = CTkLabel(data_frm , text="sorry cant find the flight \nplease try again"
                ,font=("arial" , 35) , bg_color="#DB7F7F" , text_color="black")
        Exception_lbl.place(relx = 0.1 , rely = 0.1)
        return
    else:
        label_price1 = CTkLabel(data_frm , text="price: ", text_color="black"
                                    , font = ("arial" , 30) , bg_color="#85EB9B")
        label_price1.place(relx = 0.1 , rely = 0.1)
        label_price2 = CTkLabel(data_frm , text=f"{price} USD", font = ("arial" , 30))
        label_price2.place(relx = 0.24 , rely = 0.1)

        label_airline1 = CTkLabel(data_frm , text="airline: ", text_color="black"
                                    , font = ("arial" , 30) , bg_color="#EBA285")
        label_airline1.place(relx = 0.1 , rely = 0.2)
        label_airline2 = CTkLabel(data_frm , text=airline, font = ("arial" , 30))
        label_airline2.place(relx = 0.25 , rely = 0.2)

        label_flight_number1 = CTkLabel(data_frm , text="flight number: ", text_color="black"
                                    , font = ("arial" , 30) , bg_color="#85DCEB")
        label_flight_number1.place(relx = 0.1 , rely = 0.3)
        label_flight_number2 = CTkLabel(data_frm , text=flight_number, font = ("arial" , 30))
        label_flight_number2.place(relx = 0.38 , rely = 0.3)

        label_departure_time1 = CTkLabel(data_frm , text="departure time: "
                                    , font = ("arial" , 30) , bg_color="#8785EB" , text_color="black")
        label_departure_time1.place(relx = 0.1 , rely = 0.4)
        label_departure_time2 = CTkLabel(data_frm , text=departure_time, font = ("arial" , 30))
        label_departure_time2.place(relx = 0.43 , rely = 0.4)

        label_arrival_time1 = CTkLabel(data_frm , text="arrival time: " , text_color="black"
                                    , font = ("arial" , 30) , bg_color="#EB85DE")
        label_arrival_time1.place(relx = 0.1 , rely = 0.5)
        label_arrival_time2 = CTkLabel(data_frm , text=arrival_time, font = ("arial" , 30))
        label_arrival_time2.place(relx = 0.35 , rely = 0.5)

        back_button = CTkButton(data_frm , text="Back" , font=("arial" , 30) , command=Back_button)
        back_button.place(relx = 0.6 , rely = 0.7)

def Back_button():
    data_frm.destroy()
    input_frame()

def send_data():

    origin = input_origin.get().upper()
    destination = input_des.get().upper()
    departure = input_departure.get()
    adults = input_adults.get()
    try:
        check_the_input(origin , destination , departure , adults)
        input_frm.destroy()
        new_frame(origin , destination , departure , adults)
    except Invalid as i:
        messagebox.showerror("error" , i)

def get_data(org , des , time , adlts):
    api = "bkEq51IZGuuNHx2B8KofGBx04mxF5r12"
    api_secret = "znT3COkhHQHuHCv8"
    amadeus = Client(client_id = api , client_secret = api_secret)

    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=org,
            destinationLocationCode=des,
            departureDate=time,
            adults=adlts
        )

        flight = response.data[0]

        price = flight["price"]["total"]
        airline = flight["itineraries"][0]["segments"][0]["carrierCode"]
        flight_number = flight["itineraries"][0]["segments"][0]["number"]
        departure_time = flight["itineraries"][0]["segments"][0]["departure"]["at"]
        arrival_time = flight["itineraries"][0]["segments"][0]["arrival"]["at"]

        flight_details = {"price":price
                        ,"airline":airline
                        ,"flight_number":flight_number
                        ,"departure_time":departure_time
                        ,"arrival_time":arrival_time}
        return flight_details
    
    except:
        raise Invalid("Could not find a flight")


def check_the_input(o , d , t , a):
    airport_codes = []
    with open("airports.csv" , 'r' , encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) > 4:
                airport_code = parts[4].strip('"')
                if airport_code != "\\N":
                    airport_codes.append(airport_code)

    
    if o not in airport_codes:
        raise Invalid(f"{o} code is not an airport code")
    
    if d not in airport_codes:
        raise Invalid(f"{d} code is not an airport code")
    
    try:
        d = datetime.strptime(t , "%Y-%m-%d").date()
    except:
        raise Invalid("wrong date format (yyyy-mm-dd)")
    
    try :
        a = int(a)
    except:
        raise Invalid("invalid adults naumber")

if __name__ == "__main__":
    main()
