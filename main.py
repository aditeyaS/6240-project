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


def cpu_usage():
    print("CPU Usage:")
    while True:
        cpu_percentage = psutil.cpu_percent()
        percentage_used = round(cpu_percentage)
        bar = '█' * percentage_used + ' ' * (100 - percentage_used)
        color = colorama.Fore.RED
        print(color + f"\r[{bar} {cpu_percentage}%]", end="\r")
        time.sleep(0.1)

def ram_usage():
    print("RAM Usage:")
    while True:
        ram_percentage = psutil.virtual_memory().percent
        percentage_used = round(ram_percentage)
        bar = '█' * percentage_used + ' ' * (100 - percentage_used)
        color = colorama.Fore.GREEN
        print(color + f"\r[{bar} {ram_percentage}%]", end="\r")
        time.sleep(0.1)


system_status()
memory_usage_stats()
cpu_usage()
ram_usage()