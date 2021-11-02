import datetime

user_input= input("goal:deadline please \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
# convert date sting to a time type
current_date = datetime.datetime.today()

#now caculate
time_till_deadline = deadline_date - current_date

hours_till = int(time_till_deadline.total_seconds() /60 / 60)

print(f"Dear user, time remining for your goal ({goal}) is: {time_till_deadline.days} days, {hours_till}hours")
