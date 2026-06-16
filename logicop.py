# initializing the variables 
has_licence = True 
has_experience = False 
has_clean_record = True

# Applying conditions 
can_drive_car = has_licence and has_clean_record
can_drive_truck = has_licence and has_experience and has_clean_record
cannot_drive_any = not (has_licence or has_clean_record)

# output 
print("Can drive car:", can_drive_car)
print("Can drive truck:", can_drive_truck)
print("Cannot drive any:", cannot_drive_any)
