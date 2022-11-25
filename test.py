from tkinter import *
from tkinter.ttk import *
import psutil
import time

window = Tk()
window.title("SysC")
window.geometry("1080x720")
window.resizable(False, False)

# window.grid_columnconfigure(0, weight=1)
# window.grid_columnconfigure(1, weight=1)

window.grid_columnconfigure(0, weight=1)

# row 0
row_0 = Frame(window)
row_0.grid(row=0, column=0, sticky="nsew")
row_0.grid_columnconfigure(0, weight=1)
row_0.grid_columnconfigure(1, weight=3)
# col 0
sys_info_frame = LabelFrame(row_0, text="General", padding=10)
sys_info_frame.grid(row=0, column=0, sticky="nsew")

sys_info_frame.battery_label = Label(sys_info_frame)
sys_info_frame.battery_label.grid(row=0, sticky=W)
sys_info_frame.uptime_label = Label(sys_info_frame)
sys_info_frame.uptime_label.grid(row=1, sticky=W)
sys_info_frame.cpu_cores_label = Label(sys_info_frame)
sys_info_frame.cpu_cores_label.grid(row=2,sticky=W)

# col 1
memory_info_frame = LabelFrame(row_0, text="Memory", padding=10)
memory_info_frame.grid(row=0, column=1, sticky="nsew")

memory_info_frame.grid_columnconfigure(0, weight=1)
memory_info_frame.grid_columnconfigure(1, weight=1)

memory_info_frame.mem_total = Label(memory_info_frame)
memory_info_frame.mem_total.grid(row=0, column=0, sticky=W)
memory_info_frame.mem_used = Label(memory_info_frame)
memory_info_frame.mem_used.grid(row=0, column=1, sticky=W)
memory_info_frame.mem_free = Label(memory_info_frame)
memory_info_frame.mem_free.grid(row=0, column=2, sticky=W)
memory_info_frame.status_bar = Progressbar(memory_info_frame, orient=HORIZONTAL, mode="determinate")
memory_info_frame.status_bar.grid(row=1, columnspan=3, sticky=W+E)

# row 1
row_1 = Frame(window)
row_1.grid(row=1, column=0, sticky="nsew")
row_1.grid_columnconfigure(0, weight=1)
row_1.grid_columnconfigure(1, weight=1)
# col 1
ram_usage_frame = LabelFrame(row_1, text="RAM Usage", padding=10)
ram_usage_frame.grid(row=0, column=0, sticky="nsew")
ram_usage_frame.grid_columnconfigure(0, weight=1)

ram_usage_frame.status_bar = Progressbar(ram_usage_frame, orient=HORIZONTAL, mode="determinate")
ram_usage_frame.status_bar.grid(row=0, sticky=W+E)
ram_usage_frame.status = Label(ram_usage_frame)
ram_usage_frame.status.grid(row=1, sticky=W+E)

# col 2
cpu_usage_frame = LabelFrame(row_1, text="CPU Usage", padding=10)
cpu_usage_frame.grid(row=0, column=1, sticky="nsew")
cpu_usage_frame.grid_columnconfigure(0, weight=1)

cpu_usage_frame.status_bar = Progressbar(cpu_usage_frame, orient=HORIZONTAL, mode="determinate")
cpu_usage_frame.status_bar.grid(row=0, sticky=W+E)
cpu_usage_frame.status = Label(cpu_usage_frame)
cpu_usage_frame.status.grid(row=1, sticky=W+E)

info_frame = Frame(window)
info_frame.grid(row=2, sticky="nswe")
info_frame.grid_columnconfigure(0, weight=1)
info_frame.title = Label(info_frame, text="SysC: System Monitor")
info_frame.title.grid(row=0)
info_frame.description = Label(info_frame, text="CPSC 6240 Project")
info_frame.description.grid(row=1)
info_frame.creators = Label(info_frame, text="Aditeya Srivastava | David Fernandez | Sejal Banal | Tarun Prathipati")
info_frame.creators.grid(row=2)


running = True

while running:
    
    battery_percentage = psutil.sensors_battery().percent
    sys_info_frame.battery_label.config(text=f"Battery: {battery_percentage:.2f}%")

    up_time = time.time() - psutil.boot_time()
    up_time_hrs = up_time / 60 / 60
    final_up_time = ''
    if up_time_hrs > 1:
        final_up_time = str(f"{up_time_hrs:.2f} hrs")
    else:
        final_up_time = str(f"{up_time/60:.2f} min")
    sys_info_frame.uptime_label.config(text=f"Up Time: {final_up_time}")

    sys_info_frame.cpu_cores_label.config(text=f"CPU cores: {psutil.cpu_count()}")
    
    disk_usage = psutil.disk_usage('/')
    percentage_used = round(disk_usage.percent)
    total_memory = str(round(disk_usage.total / (1024.0 ** 3))) + 'GB'
    free_memory = str(round(disk_usage.free / (1024.0 ** 3))) + 'GB'
    used_memory = str(round(disk_usage.used / (1024.0 ** 3))) + 'GB'

    memory_info_frame.mem_total.config(text=f"Total: {total_memory}")
    memory_info_frame.mem_used.config(text=f"Used: {used_memory}")
    memory_info_frame.mem_free.config(text=f"Free: {free_memory}")

    disk_usage = psutil.disk_usage('/')
    percentage_used = round(disk_usage.percent)
    memory_info_frame.status_bar.config(value=percentage_used)

    ram_percentage = psutil.virtual_memory().percent
    percentage_used = round(ram_percentage)
    ram_usage_frame.status_bar.config(value=percentage_used)
    ram_usage_frame.status.config(text=f"{ram_percentage}%")

    cpu_percentage = psutil.cpu_percent()
    percentage_used = round(cpu_percentage)
    cpu_usage_frame.status_bar.config(value=percentage_used)
    cpu_usage_frame.status.config(text=f"{cpu_percentage}%")
    
    time.sleep(0.1)
    window.update()

window.mainloop()