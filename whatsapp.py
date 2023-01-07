import pywhatkit

phone_number = input("Enter phone number: ")

# Phonenumber where to send the msg, Message, Time_Hours, Time_Mins, Wait time in secs, Closing tab, How many secs until tab closes
pywhatkit.sendwhatmsg(phone_number, "Test", 15, 33, 15, True, 2)

# Group message
group_id = input("Enter group id: ")

# Group id, message, time_hours, time_mins
pywhatkit.sendwhatmsg_to_group(group_id, "Test Group", 15, 33)



