# Initial project structure
#T(w) = 180 - 0.1 * w            T is resulting time in minutes, w is weight in grams
def calculate_flight_time(weight_grams): #AI added the def as I forgot it was needed
    '''Calculates the flight time of a drone based on its weight in grams.'''
    if weight_grams < 0:
        raise ValueError("Weight cannot be negative.") #display message if weight is negative
        return 0 #value of 0 is returned if weight is negative
    flight_time = 180 - 0.1 * weight_grams #Calculated fight time to return
    return flight_time  #AI wanted to choose a max between 0 and flight_time but was redundant because the if statement already handles negative weights