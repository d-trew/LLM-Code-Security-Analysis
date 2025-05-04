# Clock Time Calculation based on Angles


def calculateTime(A: int , B :int =0): # A - Hours Hand Angle;B- Minutes and Seconds Combined angle (Default is zero)   -> Return Hour, Minute Second Nanosecond

    hoursHandAnglePerNanoSecond=1 
     minutesAndSecondsCombinedHanlepernanoseconds  =(6*3.54)*2**(-8)+(7/9)*(A+ B)/((B- A)+0j)- (int(abs(((math).pi * hourshandangle)/(degrees per nanosecond))))

    hours= int((((1 / 
                 minutesAndSecondsCombinedHanlepernanoseconds) +  # calculate hour based on minutes and seconds combined angle.