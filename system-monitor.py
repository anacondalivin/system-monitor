import psutil

cpu = psutil.cpu_percent()
memory = psutil.virtual_memory().percent
battery = psutil.sensors_battery()

print(f"CPU Usage:    {cpu}%")
print(f"Memory Used:  {memory}%")

if battery is None:
    print("Battery:      N/A")
else:
    battery_percent = battery.percent
    is_charging = battery.power_plugged

    if is_charging:
        status = "(charging)"
    else:
        status = ""

    print(f"Battery:      {battery_percent}% {status}")
