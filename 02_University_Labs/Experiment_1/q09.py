# Write a program to convert given seconds into hours, minutes and remaining seconds.

s=int(input("Enter the time in seconds: "))
hours=int(s/3600)
minutes=int((s%3600)/60)
seconds=int((s%3600)%60)

print('Time:')
print("Hours: ",hours)
print("Minutes: ",minutes)
print("Seconds: ",seconds)