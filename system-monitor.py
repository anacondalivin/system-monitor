import psutil

cpu = psutil.cpu_percent()
memory = psutil.virtual_memory().percent
battery = psutil.sensors_battery().percent

print(f"CPU Usage:    {cpu}%")
print(f"Memory Used:  {memory}%")
print(f"Battery:      {battery}%")
