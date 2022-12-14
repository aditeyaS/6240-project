from tkinter import *
from tkinter.ttk import *
import psutil
import time
from threading import Thread
import sys

import utils as Utils
import const.color as Colors
import const.dimensions as Dimensions
import const.config as Config

window = Tk()
window.title(Config.APP_NAME_SHORT)
window.geometry(f"{Dimensions.SCREEN_WIDTH}x{Dimensions.SCREEN_HEIGHT}")
window.resizable(False, False)

icon = PhotoImage(file="img/icon.gif")
window.iconphoto(False, icon)

window.grid_columnconfigure(0, weight=1)

# <-- ROW 0 - START -->

row_0 = Frame(window)
row_0.grid(row=0, column=0, sticky="nsew")
row_0.grid_columnconfigure(0, weight=1)
row_0.grid_columnconfigure(1, weight=3)

# row 0 col 0 (General)
sys_info_frame = LabelFrame(row_0, text="General", padding=Dimensions.PADDING_L)
sys_info_frame.grid(row=0, column=0, sticky="nsew")

sys_info_frame.battery_label = Label(sys_info_frame)
sys_info_frame.battery_label.grid(row=0, sticky=W)
sys_info_frame.uptime_label = Label(sys_info_frame)
sys_info_frame.uptime_label.grid(row=1, sticky=W)
sys_info_frame.cpu_cores_label = Label(sys_info_frame)
sys_info_frame.cpu_cores_label.grid(row=2,sticky=W)

# row 0 col 1 (Memory)
memory_info_frame = LabelFrame(row_0, text="Memory", padding=Dimensions.PADDING_L)
memory_info_frame.grid(row=0, column=1, sticky="nsew")
memory_info_frame.grid_columnconfigure(0, weight=1)
memory_info_frame.grid_columnconfigure(1, weight=1)

memory_info_frame.mem_total = Label(memory_info_frame, font='Arial 12', foreground=Colors.GRAY)
memory_info_frame.mem_total.grid(row=0, column=0, sticky=W)
memory_info_frame.mem_used = Label(memory_info_frame, font='Arial 12', foreground=Colors.BLUE)
memory_info_frame.mem_used.grid(row=0, column=1, sticky=W)
memory_info_frame.mem_free = Label(memory_info_frame, font='Arial 12', foreground=Colors.BLACK)
memory_info_frame.mem_free.grid(row=0, column=2, sticky=W)
memory_info_frame.status_bar = Progressbar(memory_info_frame, orient=HORIZONTAL, mode="determinate", length=100)
memory_info_frame.status_bar.grid(row=1, columnspan=3, sticky=W+E)

# <-- ROW 0 - END -->


# <-- ROW 1 - START -->

row_1 = Frame(window)
row_1.grid(row=1, column=0, sticky="nsew")
row_1.grid_columnconfigure(0, weight=1)
row_1.grid_columnconfigure(1, weight=1)

# row 1 col 0 (RAM Usage)
ram_usage_frame = LabelFrame(row_1, text="RAM Usage", padding=Dimensions.PADDING_L)
ram_usage_frame.grid(row=0, column=0, sticky="nsew")
ram_usage_frame.grid_columnconfigure(0, weight=1)

ram_usage_frame.status_bar = Progressbar(ram_usage_frame, orient=HORIZONTAL, mode="determinate", length=100)
ram_usage_frame.status_bar.grid(row=0, sticky=W+E)
ram_usage_frame.status = Label(ram_usage_frame, font="Arial 15")
ram_usage_frame.status.grid(row=1, sticky=W+E)

# row 1 col 1 (CPU Usage)
cpu_usage_frame = LabelFrame(row_1, text="CPU Usage", padding=Dimensions.PADDING_L)
cpu_usage_frame.grid(row=0, column=1, sticky="nsew")
cpu_usage_frame.grid_columnconfigure(0, weight=1)

cpu_usage_frame.status_bar = Progressbar(cpu_usage_frame, orient=HORIZONTAL, mode="determinate", length=100)
cpu_usage_frame.status_bar.grid(row=0, sticky=W+E)
cpu_usage_frame.status = Label(cpu_usage_frame, font="Arial 15")
cpu_usage_frame.status.grid(row=1, sticky=W+E)

# <-- ROW 1 - END -->


# <-- ROW 2 - START -->

row_2 = Frame(window)
row_2.grid(row=2, column=0, sticky="nswe")
row_2.grid_columnconfigure(0, weight=1)

# row 2 col 0 (Tasks)
tasks_count_frame = LabelFrame(row_2, text="Tasks")
tasks_count_frame.grid(sticky="nswe")
tasks_count_frame.grid_columnconfigure(0, weight=1)
tasks_count_frame.grid_columnconfigure(1, weight=1)
tasks_count_frame.grid_columnconfigure(2, weight=1)
tasks_count_frame.grid_columnconfigure(3, weight=1)
tasks_count_frame.grid_columnconfigure(4, weight=1)

tasks_count_frame.total = Label(tasks_count_frame, font="Arial 12", padding=Dimensions.PADDING_S)
tasks_count_frame.total.grid(row=0, column=0, sticky="nsew")
tasks_count_frame.running = Label(tasks_count_frame, font="Arial 12", padding=Dimensions.PADDING_S)
tasks_count_frame.running.grid(row=0, column=1, sticky="nsew")
tasks_count_frame.sleeping = Label(tasks_count_frame, font="Arial 12", padding=Dimensions.PADDING_S)
tasks_count_frame.sleeping.grid(row=0, column=2, sticky="nsew")
tasks_count_frame.stopped = Label(tasks_count_frame, font="Arial 12", padding=Dimensions.PADDING_S)
tasks_count_frame.stopped.grid(row=0, column=3, sticky="nsew")
tasks_count_frame.zombie = Label(tasks_count_frame, font="Arial 12", padding=Dimensions.PADDING_S)
tasks_count_frame.zombie.grid(row=0, column=4, sticky="nsew")

# <-- ROW 2 - END -->


# <-- ROW 3 - START -->

row_3 = Frame(window)
row_3.grid(row=3, column=0, sticky="nswe")
row_3.grid_columnconfigure(0, weight=1)
row_3.grid_columnconfigure(1, weight=1)


# row 3 col 0 (Network)
network_frame = LabelFrame(row_3, text="Network", padding=Dimensions.PADDING_L)
network_frame.grid(row=0, column=0, sticky="nswe")
network_frame.grid_columnconfigure(0, weight=1)
network_frame.grid_columnconfigure(1, weight=1)
network_frame.grid_rowconfigure(0, weight=1)
network_frame.grid_rowconfigure(1, weight=1)

c00 = Frame(network_frame)
c00.grid(row=0, column=0, sticky="nswe")
c00.title = Label(c00, text="Download")
c00.title.grid(row=0, sticky=W)
c00.val = Label(c00, font='Arial 18')
c00.val.grid(row=1, sticky=W)

c01 = Frame(network_frame)
c01.grid(row=0, column=1, sticky="nswe")
c01.title = Label(c01, text="Download Speed")
c01.title.grid(row=0, sticky=W)
c01.val = Label(c01, foreground=Colors.GREEN, font='Arial 18')
c01.val.grid(row=1, sticky=W)


c10 = Frame(network_frame)
c10.grid(row=1, column=0, sticky="nswe")
c10.title = Label(c10, text="Upload")
c10.title.grid(row=0, sticky=W)
c10.val = Label(c10, font='Arial 18')
c10.val.grid(row=1, sticky=W)

c11 = Frame(network_frame)
c11.grid(row=1, column=1, sticky="nswe")
c11.title = Label(c11, text="Upload Speed")
c11.title.grid(row=0, sticky=W)
c11.val = Label(c11, foreground=Colors.RED, font='Arial 18')
c11.val.grid(row=1, sticky=W)

# row 3 col 1 (Top Precess)
top_process_frame = LabelFrame(row_3, text="Top process")
top_process_frame.grid(row=0, column=1, sticky="nswe")
top_process_frame.grid_columnconfigure(0, weight=1)
top_process_frame.grid_columnconfigure(1, weight=1)
top_process_frame.grid_columnconfigure(2, weight=1)
top_process_frame.grid_columnconfigure(3, weight=1)
top_process_frame.grid_columnconfigure(4, weight=1)


# table header starts
top_process_frame.c00 = Label(top_process_frame, text="pid", padding=Dimensions.PADDING_S, font='bold')
top_process_frame.c00.grid(row=0, column=0, sticky="w")
top_process_frame.c01 = Label(top_process_frame, text="Name", padding=Dimensions.PADDING_S, font='bold')
top_process_frame.c01.grid(row=0, column=1, sticky="w")
top_process_frame.c02 = Label(top_process_frame, text="Usage", padding=Dimensions.PADDING_S, font='bold')
top_process_frame.c02.grid(row=0, column=2, sticky="w")
top_process_frame.c03 = Label(top_process_frame, text="Status", padding=Dimensions.PADDING_S, font='bold')
top_process_frame.c03.grid(row=0, column=3, sticky="w")
top_process_frame.c04 = Label(top_process_frame, text="Threads", padding=Dimensions.PADDING_S, font='bold')
top_process_frame.c04.grid(row=0, column=4, sticky="w")
# table header ends

# table row 1 starts
top_process_frame.c10 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c10.grid(row=1, column=0, sticky="w")
top_process_frame.c11 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c11.grid(row=1, column=1, sticky="w")
top_process_frame.c12 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c12.grid(row=1, column=2, sticky="w")
top_process_frame.c13 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c13.grid(row=1, column=3, sticky="w")
top_process_frame.c14 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c14.grid(row=1, column=4, sticky="w")
# table row 1 ends

# table row 2 starts
top_process_frame.c20 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c20.grid(row=2, column=0, sticky="w")
top_process_frame.c21 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c21.grid(row=2, column=1, sticky="w")
top_process_frame.c22 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c22.grid(row=2, column=2, sticky="w")
top_process_frame.c23 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c23.grid(row=2, column=3, sticky="w")
top_process_frame.c24 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c24.grid(row=2, column=4, sticky="w")
# table row 2 ends

# table row 3 starts
top_process_frame.c30 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c30.grid(row=3, column=0, sticky="w")
top_process_frame.c31 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c31.grid(row=3, column=1, sticky="w")
top_process_frame.c32 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c32.grid(row=3, column=2, sticky="w")
top_process_frame.c33 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c33.grid(row=3, column=3, sticky="w")
top_process_frame.c34 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c34.grid(row=3, column=4, sticky="w")
# table row 3 ends

# table row 4 starts
top_process_frame.c40 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c40.grid(row=4, column=0, sticky="w")
top_process_frame.c41 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c41.grid(row=4, column=1, sticky="w")
top_process_frame.c42 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c42.grid(row=4, column=2, sticky="w")
top_process_frame.c43 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c43.grid(row=4, column=3, sticky="w")
top_process_frame.c44 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c44.grid(row=4, column=4, sticky="w")
# table row 4 ends

# table row 5 starts
top_process_frame.c50 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c50.grid(row=5, column=0, sticky="w")
top_process_frame.c51 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c51.grid(row=5, column=1, sticky="w")
top_process_frame.c52 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c52.grid(row=5, column=2, sticky="w")
top_process_frame.c53 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c53.grid(row=5, column=3, sticky="w")
top_process_frame.c54 = Label(top_process_frame, padding=Dimensions.PADDING_S)
top_process_frame.c54.grid(row=5, column=4, sticky="w")
# table row 5 ends

# <-- ROW 3 - END -->


# <-- ROW 4 - START -->

info_frame = Frame(window, padding=Dimensions.PADDING_L, relief=SUNKEN)
info_frame.grid(row=4, sticky="nswe")
info_frame.grid_columnconfigure(0, weight=1)

info_frame.title = Label(info_frame, text=Config.APP_NAME_LONG)
info_frame.title.grid(row=0)
auth_list = f"{Config.AUTH_AS} | {Config.AUTH_DF} | {Config.AUTH_SB} | {Config.AUTH_TP}"
info_frame.creators = Label(info_frame, text=auth_list)
info_frame.creators.grid(row=1)

# <-- ROW 4 - END -->

# NETWORK INFO CALCULATION - START
net_info_up = ""
net_info_dl = ""
net_info_up_speed = ""
net_info_dl_speed = ""

def network_info_stats():
    UPDATE_DELAY = 1
    io = psutil.net_io_counters()
    bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv
    while True:
        time.sleep(UPDATE_DELAY)
        io_2 = psutil.net_io_counters()
        us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv
        global net_info_up
        net_info_up = Utils.get_size(io_2.bytes_sent)
        global net_info_dl
        net_info_dl = Utils.get_size(io_2.bytes_recv)
        global net_info_up_speed
        net_info_up_speed = Utils.get_size(us / UPDATE_DELAY)
        global net_info_dl_speed
        net_info_dl_speed = Utils.get_size(ds / UPDATE_DELAY)
        bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv

# a thread to find the network information
network_info_thread = Thread(target=network_info_stats)
network_info_thread.start()
# NETWORK INFO CALCULATION - START

app_running = True

while app_running:
    
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

    total_proc_no = 0
    running_proc_no = 0
    sleeping_proc_no = 0
    zombie_proc_no = 0
    stopped_proc_no = 0
    process_list = []
    for proc in psutil.process_iter():
        mem_p = round(proc.memory_percent(),2)
        process_list.append([
            proc.pid,
            proc.name(),
            f"{mem_p}%",
            proc.status(),
            proc.num_threads()
        ])
        total_proc_no += 1
        if (proc.status() == psutil.STATUS_RUNNING):
            running_proc_no += 1
        elif (proc.status() == psutil.STATUS_SLEEPING):
            sleeping_proc_no += 1
        elif (proc.status() == psutil.STATUS_ZOMBIE):
            zombie_proc_no += 1
        elif proc.status() == psutil.STATUS_STOPPED:
            stopped_proc_no += 1
    
    process_list.sort(key=lambda x:x[2], reverse=True)

    tasks_count_frame.total.config(text=f"Total:{total_proc_no}")
    tasks_count_frame.running.config(text=f"Running:{running_proc_no}")
    tasks_count_frame.sleeping.config(text=f"Sleeping:{sleeping_proc_no}")
    tasks_count_frame.stopped.config(text=f"Stopped:{stopped_proc_no}")
    tasks_count_frame.zombie.config(text=f"Zombie:{zombie_proc_no}")

    c00.val.config(text=net_info_up)
    c01.val.config(text=f"{net_info_up_speed}/s")
    c10.val.config(text=net_info_dl)
    c11.val.config(text=f"{net_info_dl_speed}/s")

    top_process_frame.c10.config(text=process_list[0][0])
    top_process_frame.c11.config(text=process_list[0][1])
    top_process_frame.c12.config(text=process_list[0][2])
    top_process_frame.c13.config(text=process_list[0][3])
    top_process_frame.c14.config(text=process_list[0][4])

    top_process_frame.c20.config(text=process_list[1][0])
    top_process_frame.c21.config(text=process_list[1][1])
    top_process_frame.c22.config(text=process_list[1][2])
    top_process_frame.c23.config(text=process_list[1][3])
    top_process_frame.c24.config(text=process_list[1][4])

    top_process_frame.c30.config(text=process_list[2][0])
    top_process_frame.c31.config(text=process_list[2][1])
    top_process_frame.c32.config(text=process_list[2][2])
    top_process_frame.c33.config(text=process_list[2][3])
    top_process_frame.c34.config(text=process_list[2][4])

    top_process_frame.c40.config(text=process_list[3][0])
    top_process_frame.c41.config(text=process_list[3][1])
    top_process_frame.c42.config(text=process_list[3][2])
    top_process_frame.c43.config(text=process_list[3][3])
    top_process_frame.c44.config(text=process_list[3][4])

    top_process_frame.c50.config(text=process_list[4][0])
    top_process_frame.c51.config(text=process_list[4][1])
    top_process_frame.c52.config(text=process_list[4][2])
    top_process_frame.c53.config(text=process_list[4][3])
    top_process_frame.c54.config(text=process_list[4][4])

    time.sleep(0.1)
    window.update()

window.mainloop()

def disable_event():
    network_info_thread.join()
    window.quit()
    window.destroy()
    sys.exit()
    
window.protocol("WM_DELETE_WINDOW", disable_event)