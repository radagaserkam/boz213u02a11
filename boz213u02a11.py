
start_hour = int(input("Enter start hour: "))
start_minute = int(input("Enter start minute: "))
duration = int(input("Enter duration in minutes: "))

total_minutes = start_hour * 60 + start_minute + duration

end_hour = (total_minutes // 60) % 24
end_minute = total_minutes % 60

print("End time:", end_hour, ":", end_minute)
