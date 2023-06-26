import math

#degrees to radian
###########################################################################################################
def degtorad():
    val = None
    while val != float:
        try:
            val = float(input("Enter a value in degrees:"))
        except:
            continue
        else:
            break
    
    deg = val
    if deg >=0:
        while deg>360:
            deg= deg -360
    elif deg<0:
        while deg<-360:
            deg= deg + 360
    rad = deg*math.pi/180
    print (round(deg,2),"degrees is equal to", round(rad,2), "radians")

#radian to degree
############################################################################################################
def radtodeg():
    val = None
    while val != float:
        try:
            val = float(input("Enter a value in radian:"))
        except:
            continue
        else:
            break
    rad = val
    if rad >=0:
        while rad>math.pi:
            rad= rad - math.pi
    elif rad<0:
        while rad<-math.pi:
            rad= rad + math.pi
    deg = rad/math.pi*180
    print (round(rad,2),"radian is equal to", round(deg,2), "degrees")

#conversion selector and input value
############################################################################################################


print ("Enter 1 for degree to radian conversion\nEnter 2 for radian to degrees conversion")
unit="0"
while not (unit == "1") or (unit =="2"):
    unit=input()
    if unit == "1":
        print ("Degree to radian is chosen")
        degtorad ()
        
    elif unit == "2":
        print("Radian to degree is chosen")
        radtodeg()
        break
    else:
        print ("Invalid input")
############################################################################################################

print("Note: input value has been simplified")


    

