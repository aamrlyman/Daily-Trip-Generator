

destinations = ['Seattle', 'Tacoma', 'Eatonville', 'Puyallup']
restaurants = ['Melting Pot', 'Novilhaus', 'MacDonalds', 'Applebees']
mode_of_transportations = ['walk', 'bike', 'Uber', 'drive', 'bus']
entertainments = ['a movie', 'mini golfing', 'a hike', 'a walk through Pike Place Market']

import random
def select_mode_of_transportation(list):
    transportation = random.choice(list)
    return transportation

def select_restaurant(list):
    restaurant = random.choice(list)
    return restaurant

def select_destination(list):
    destination = random.choice(list)
    return destination

def select_entertainment(list):
    entertainment = random.choice(list)
    return entertainment

def random_trip_generator():
    mode_of_transportation = select_mode_of_transportation(mode_of_transportations)
    restaurant = select_restaurant(restaurants)
    destination = select_destination(destinations)
    entertainment = select_entertainment(entertainments)
    def trip_plan(): 
        return f'Your itinerary is {mode_of_transportation} to {restaurant} in {destination} followed by {entertainment}.'
    print('')
    print(trip_plan())
    is_user_happy = 'no'
    while is_user_happy == 'no':
        print('')
        is_user_happy = input('Are you happy with this itinerary? yes or no: ')
        if is_user_happy == "yes":
            print('')
            print(f'{trip_plan()} Have Fun!')
            print('')
            break
        print('')
        user_change = input('What would you like to change? select a number: (1)mode of transportation, (2)restaurant, (3) destination, or (4)entertainment: ')
        if user_change == '1':
            mode_of_transportation = select_mode_of_transportation(mode_of_transportations)
        elif user_change == '2':
            restaurant = select_restaurant(restaurants)
        elif user_change == '3':
            destination = select_destination(destinations)
        elif user_change == '4':
            entertainment = select_entertainment(entertainments)
        else:
            print('invalid entry')
            print('')
        print(trip_plan())


random_trip_generator()