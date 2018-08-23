import webbrowser
from Tkinter import *

def check_flights(origins, destinations, flight_date):
  # open new firefox window
  my_firefox = webbrowser.get('firefox')
  # my_firefox.open_new('google');

  # southwest website format
  sw_origin_str = "https://www.southwest.com/air/booking/select.html?originationAirportCode="
  sw_destination_str = "&destinationAirportCode="
  sw_date_str = "&returnAirportCode=&departureDate="
  sw_end_str = "&departureTimeOfDay=ALL_DAY&returnDate=&returnTimeOfDay=ALL_DAY&adultPassengersCount=1&seniorPassengersCount=0&fareType=USD&passengerType=ADULT&tripType=oneway&promoCode=&reset=true&redirectToVision=true&int=HOMEQBOMAIR&leapfrogRequest=true"
  for origin in origins:
    for destination in destinations:

      webpage = sw_origin_str + origin + sw_destination_str + destination + sw_date_str + flight_date + sw_end_str
      my_firefox.open_new_tab(webpage)

  # google website format
  g_start_str = "https://www.google.com/flights#flt="
  g_end_str = ";c:USD;e:1;sd:1;t:f;tt:o"
  g_webpage=g_start_str + ",".join(origins) + "." + ",".join(destinations) + "." + flight_date + g_end_str
  my_firefox.open_new_tab(g_webpage)
def callback(date_textbox, origin_textbox, destination_textbox):
    flight_date = date_textbox.get()
    origin_str = origin_textbox.get()
    destination_str = destination_textbox.get()

    origins = origin_str.split(',')
    destinations = destination_str.split(',')

    check_flights(origins, destinations, flight_date)

# def start_gui():
master = Tk();
Label(master, text="Date (year-month-day)").grid(row=0)
Label(master, text="Origin Airports").grid(row=1)
Label(master, text="Destination Airports").grid(row=2)

date_textbox = Entry(master)
date_textbox.insert(0, "2018-09-12")

origin_textbox = Entry(master)
origin_textbox.insert(0,"SFO,SJC")

destination_textbox = Entry(master)
destination_textbox.insert(0,'LGB,SNA,LAX')

date_textbox.grid(row=0, column=1)
origin_textbox.grid(row=1, column=1)
destination_textbox.grid(row=2, column=1)

b = Button(master, text="search", command=lambda: callback(date_textbox, origin_textbox, destination_textbox))
b.grid(row=3,column=0, columnspan=2)



def main():
    # set departure dates
    outbound_friday = "2018-08-10"
    outbound_saturday= "2018-08-11"

    inbound_sunday = "2018-08-12"
    inbound_monday= "2018-08-13"


       
    # Check outbound flights on friday
    origins = ['SFO','SJC']
    destinations = ['LAX','LGB','SNA']

    check_flights(origins, destinations, outbound_friday)



    # Check outbound flights on saturday
    origins = ['SFO','SJC','OAK']
    destinations = ['LAX','LGB','SNA']
    check_flights(origins, destinations, outbound_saturday)


    # Check return flights on sunday
    origins = ['LAX','LGB','SNA']
    destinations = ['SFO','OAK']

    check_flights(origins, destinations, inbound_sunday)




    # Check return flights on monday
    origins = ['LAX','LGB','SNA']
    destinations = ['SFO','SJC']
    check_flights(origins, destinations, inbound_monday)


# if __name__ == "__main__":
#     main()


