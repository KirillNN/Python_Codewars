# speed of aircrafts is given in *knots*
# travelTime is in *minutes*
# travel distance should be returned in *kilometers*

def travel_distance(avg_speed, travel_time):
    KM_PER_MILE = 0.869 / 1.609344
    travel_hours = travel_time / 60
    travel_miles = avg_speed * travel_hours
    travel_kms = travel_miles / KM_PER_MILE
    return travel_kms


print(travel_distance(0, 0))
print(travel_distance(600, 60))
print(travel_distance(800, 60))
