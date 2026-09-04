# Initial project structure
#T(w) = 180 - 0.1 * w            T is resulting time in minutes, w is weight in grams
def calculate_flight_time(weight_grams): #AI added the def as I forgot it was needed
    '''Calculates the flight time of a drone based on its weight in grams.'''
    if weight_grams < 0:
        raise ValueError("Weight cannot be negative.") #display message if weight is negative
        return 0 #value of 0 is returned if weight is negative
    flight_time = 180 - 0.1 * weight_grams #Calculated fight time to return
    return flight_time  #AI wanted to choose a max between 0 and flight_time but was redundant because the if statement
def flight_time_table(max_weight_grams, step_grams): #AI wanted to create a table only inserting the weights
    '''Generates a table of flight times for weights from 0 to max_weight_grams in increments of step_grams.'''
    if max_weight_grams < 0 or step_grams <= 0:
        raise ValueError("Max weight must be non-negative and step must be positive.") #AI added display message if max weight is negative or step is not positive
    table = [] #Added a list to store the table
    for weight in range(0, max_weight_grams + 1, step_grams):
        flight_time = calculate_flight_time(weight) #rejected initial AI suggestion in order to call the function calculate_flight_time
        table.append((weight, flight_time))
    return table # returns the table of weights and their flight times