alarm_time = input("Set the alarm time (HH:MM): ")

now = input("Enter the current time (HH:MM): ")

if now == alarm_time:
    print("Alarm! Time to wake up!")
else:
    print("Not time yet. Keep sleeping!")