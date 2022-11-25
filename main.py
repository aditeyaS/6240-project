#!/usr/bin/env python3
import time
import colorama
import psutil

def system_status():
    color = colorama.Fore.YELLOW
    
    # calculate battery percentage
    battery_percentage = psutil.sensors_battery().percent; 
    print(color + f"Battery: {battery_percentage}%")
    
    # system up time
    up_time = time.time() - psutil.boot_time()
    up_time_hrs = up_time / 60 / 60
    final_up_time = ''
    if up_time_hrs > 1:
        final_up_time = str(f"{up_time_hrs:.2f} hrs")
    else:
        final_up_time = str(f"{up_time/60:.2f} min")
    print(color + f"System up time: {final_up_time}")

    # number of cpu
    print(color + f"Number of CPU: {psutil.cpu_count()}")
    
    print(colorama.Fore.RESET)


def memory_usage_stats():
    color = colorama.Fore.CYAN
    
    disk_usage = psutil.disk_usage('/')
    percentage_used = round(disk_usage.percent)
    bar = '█' * percentage_used + ' ' * (100 - percentage_used)
    total_memory = str(round(disk_usage.total / (1024.0 ** 3))) + 'GB'
    free_memory = str(round(disk_usage.free / (1024.0 ** 3))) + 'GB'
    used_memory = str(round(disk_usage.used / (1024.0 ** 3))) + 'GB'
    print(color + f"Memory Info (Total: {total_memory} Used: {used_memory} Available: {free_memory})")
    print(color + f"[{bar}] {disk_usage.percent}%")
    print(colorama.Fore.RESET)



def cpu_ram_usage():
    UP = "\x1B[3A"
    CLR = "\x1B[0K"
    print("\n\n")  # set up blank lines so cursor moves work
    while True:
        #cpu_usage
        cpu_percentage = psutil.cpu_percent()
        cpu_percentage_used = round(cpu_percentage)
        cpu_bar = '█' * cpu_percentage_used + ' ' * (100 - cpu_percentage_used)
        cpu_color = colorama.Fore.RED

        #ram_usage
        ram_percentage = psutil.virtual_memory().percent
        ram_percentage_used = round(ram_percentage)
        ram_bar = '█' * ram_percentage_used + ' ' * (100 - ram_percentage_used)
        ram_color = colorama.Fore.GREEN

        print(f"{UP}CPU Usage: [{cpu_bar} {cpu_percentage}%]{CLR}\nRAM Usage: [{ram_bar} {ram_percentage}%]{CLR}\n")

        time.sleep(0.1)


system_status()
memory_usage_stats()
cpu_ram_usage()

