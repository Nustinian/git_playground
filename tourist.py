destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

attractions = [[] for destination in destinations]

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
    except ValueError:
        return
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return

def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for attraction in attractions_in_city:
        for interest in interests:
            if interest in attraction[1]:
                attractions_with_interest.append(attraction[0])
    return attractions_with_interest

def get_attraction_for_traveler(traveler):
    attractions_for_traveler = find_attractions(traveler[1], traveler[2])
    recommendation_message = "Hi {name}, we think you'll like these places around {destination}:".format(name=traveler[0], destination=traveler[1])
    if len(attractions_for_traveler) == 2:
        recommendation_message += " the {attraction1} and the {attraction2}.".format(attraction1 = attractions_for_traveler[0], attraction2 = attractions_for_traveler[1])
    elif len(attractions_for_traveler) > 1:
        i = 1
        while i < len(attractions_for_traveler):
            recommendation_message += " the {attraction},".format(attraction=attractions_for_traveler[i - 1])
            i += 1
        recommendation_message += " and the {attraction}.".format(attraction=attractions_for_traveler[-1])
    elif len(attractions_for_traveler) == 1:
        recommendation_message = "Hi {name}, we think you'll like this place in {destination}: the {attraction}.".format(name=traveler[0], destination=traveler[1], attraction=attractions_for_traveler[0])
    else:
        recommendation_message = "Hi {name}, we're sorry to say that our database doesn't have any attractions in your destination city that we feel you'll like. We are always adding new attractions, so check back later!"
    print(recommendation_message)
    return

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

get_attraction_for_traveler(['Dereck Smill', 'Shanghai, China', ['garden', 'art', 'skyscraper']])
