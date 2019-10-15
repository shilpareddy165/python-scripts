import time

print("Hello, from Python Script!")

#-----------------------------------------------------
# Displays the current time 
# -----------------------------------------------------   
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print("Current Time: ", current_time)
#-----------------------------------------------------

# --------------------------------------------------------------------------------
# Uncomment the below print statement for trigger exercise 
# --------------------------------------------------------------------------------
# print("When someone shares something of value with you that benefits you, then you are morally obligated to share it with others!")
# --------------------------------------------------------------------------------
