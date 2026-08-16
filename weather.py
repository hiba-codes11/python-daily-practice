distance_mi = 7
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = False

 # NOT/not flips the truth value; it turns a falsy value into True so the block can run.
 # x = True  → True
 # x = not True  → False

 # AND/and means: BOTH conditions must be True.
 # OR/or means: at least ONE condition must be True.

if not distance_mi:
    print(False)                

elif distance_mi <= 1:
    print(not is_raining)       


elif distance_mi <= 6:
    print(has_bike and not is_raining)  

else: 
    print(has_car or has_ride_share_app)    

# Comparisons produce True or False
# When you write:
# distance_mi <= 6
# Python asks:
# Is 7 less than or equal to 6?
# No.
# Therefore:
# distance_mi <= 6
# becomes:
# False