import os
import psutil
import shutil
import tempfile
import tkinter as tk
from tkinter import ttk, messagebox

class ResourceMonitorGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Resource Monitor")
        self.geometry("350x200")

        # Create a style using ttk
        self.style = ttk.Style()
        self.style.configure("Title.TLabel", font=("Helvetica", 16, "bold"))
        self.style.configure("Data.TLabel", font=("Helvetica", 12))
        self.style.configure("TButton", font=("Helvetica", 12))

        # Labels for resource monitoring
        self.label_cpu = ttk.Label(self, text="CPU Usage:", style="Title.TLabel")
        self.label_cpu.pack(pady=5)
        self.label_cpu.bind("<Button-1>", self.show_cpu_breakdown)

        self.label_memory = ttk.Label(self, text="Memory Usage:", style="Title.TLabel")
        self.label_memory.pack(pady=5)
        self.label_memory.bind("<Button-1>", self.show_memory_breakdown)

        self.label_disk = ttk.Label(self, text="Disk Usage:", style="Title.TLabel")
        self.label_disk.pack(pady=5)
        self.label_disk.bind("<Button-1>", self.show_disk_breakdown)

        # Button to clear cache
        self.clear_cache_button = ttk.Button(self, text="Clear Cache", command=self.clear_cache, style="TButton")
        self.clear_cache_button.pack(pady=10)

        # Define the path for the cache directory
        self.cache_directory = "cache"

        self.update_labels()

    def update_labels(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')

        self.label_cpu.config(text=f"CPU Usage: {cpu_percent}%", style="Data.TLabel")
        self.label_memory.config(text=f"Memory Usage: {memory_info.percent:.2f} GB / {memory_info.total / (1024 ** 3):.2f} GB", style="Data.TLabel")
        self.label_disk.config(text=f"Disk Usage: {disk_usage.percent:.2f} GB / {disk_usage.total / (1024 ** 3):.2f} GB", style="Data.TLabel")

        self.after(1000, self.update_labels)

    def show_cpu_breakdown(self, event):
        cpu_breakdown = psutil.cpu_percent(interval=1, percpu=True)
        breakdown_str = "\n".join([f"Core {i + 1}: {percent}%" for i, percent in enumerate(cpu_breakdown)])
        messagebox.showinfo("CPU Breakdown", breakdown_str)

    def show_memory_breakdown(self, event):
        memory_info = psutil.virtual_memory()
        breakdown_str = f"Total: {memory_info.total / (1024 ** 3):.2f} GB\nUsed: {memory_info.used / (1024 ** 3):.2f} GB\nFree: {memory_info.free / (1024 ** 3):.2f} GB"
        messagebox.showinfo("Memory Breakdown", breakdown_str)

    def show_disk_breakdown(self, event):
        disk_usage = psutil.disk_usage('/')
        breakdown_str = f"Total: {disk_usage.total / (1024 ** 3):.2f} GB\nUsed: {disk_usage.used / (1024 ** 3):.2f} GB\nFree: {disk_usage.free / (1024 ** 3):.2f} GB"
        messagebox.showinfo("Disk Breakdown", breakdown_str)

    def clear_cache(self):
        try:
            # Create the cache directory if it doesn't exist
            if not os.path.exists(self.cache_directory):
                os.makedirs(self.cache_directory)

            # Clear the cache by removing only temporary files in the directory
            for file_name in os.listdir(self.cache_directory):
                file_path = os.path.join(self.cache_directory, file_name)
                try:
                    # Check if the file is a temporary file
                    if tempfile.gettempdir() in os.path.abspath(file_path):
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}. Error: {e}")

            messagebox.showinfo("Clear Cache", "Temporary files in the cache cleared successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to clear cache. Error: {e}")

if __name__ == "__main__":
    app = ResourceMonitorGUI()
    app.mainloop()
