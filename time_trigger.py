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
# For git trigger exercise follow the below steps - 
# git checkout develop
# Modify quote variable with your favourite quote
# git add --all
# git commit -m "Your Message"
# git push
# --------------------------------------------------------------------------------
quote = "Good Morning!!!!!!!!!!!!!!!!!!"
print(quote)
# --------------------------------------------------------------------------------
