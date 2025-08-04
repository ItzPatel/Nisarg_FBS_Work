#Convert the time entered in hh,min and sec into seconds.
hrs = int(input("Enter hours: "))
mins = int(input("Enter minutes: " ))
seconds = int(input("Enter seconds: "))

total_seconds = (hrs * 3600) + (mins * 60) + seconds

print(f"\nTotal time in seconds: {total_seconds} seconds")