omega_hour=0.5 #0.5 degrees per minute
omega_minute=6 #6 degrees per minute

time_in_hours=0 #time in hours

#Question: when do the minute and hour hands of a clock have the same angular displacement?
#theta_hour = omega_hour * time
#theta_minute = omega_minute * time
#Answer: when theta_hour and theta_minute are equal

hour_blocks = list(range(0, 12))
for block in hour_blocks:
    block_in_minutes = block * 60
    degrees_hour=block_in_minutes*omega_hour
    minutes=degrees_hour/(omega_minute-omega_hour)
    print(f"The meeting time is: {block} hours and {minutes} minutes")

