# Resource Monitor GUI

**Overview:**

Resource Monitor GUI is a simple Python application built with Tkinter that provides real-time monitoring of CPU usage, memory usage, and disk usage. Additionally, it includes a feature to delete temporary files from the system's temporary directory.

![Resource Monitor GUI Screenshot](https://ibb.co/Cv5mqXp))

**Features:**

- **CPU Usage:** Displays the current CPU usage percentage.
- **Memory Usage:** Displays the used and total memory with a breakdown.
- **Disk Usage:** Displays the used and total disk space with a breakdown.
- **Clear Cache:** Clears temporary files from the system's temporary directory.

**How It Works:**

1. The application uses the `psutil` library to retrieve real-time information about CPU, memory, and disk usage.
2. Labels are updated every second to reflect the current resource usage.
3. Users can click on specific sections to view detailed breakdowns for CPU, memory, and disk usage.
4. The "Clear Cache" button removes temporary files from the system's temporary directory.

**Usage:**

1. Clone the repository:

    ```bash
    git clone https://github.com/<MuneerRaza19>/RealTimeResourceMonitor.git)
    ```

2. Run the application:

    ```bash
    python script.py
    ```

**Contributing:**

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.



**Author:**

Muneer-Raza 

**Acknowledgments:**

- The application uses the `psutil` library for resource monitoring.
