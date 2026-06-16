# Logical Operator 2
is_sunny = True 
temprature = 25
wind_speed = 10 
water_temprature = 22

can_go_hiking = is_sunny and temprature > 15 and wind_speed < 20
can_go_swimming = is_sunny and temprature > 20 and water_temprature > 18
cannot_go_outside = not (is_sunny or temprature < 10) or wind_speed > 30

print("Can go hiking:", can_go_hiking)
print("Can go swimming:", can_go_swimming)
print("Cannot go outside:", cannot_go_outside)