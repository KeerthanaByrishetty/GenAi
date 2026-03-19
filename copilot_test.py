import os
import platform
from datetime import datetime, timedelta

def get_system_uptime():
    """
    Print the system uptime in a human-readable format.
    Works on Windows, macOS, and Linux.
    """
    
    if platform.system() == "Windows":
        # Windows: Use wmic to get boot time
        try:
            import subprocess
            result = subprocess.run(
                ["wmic", "os", "get", "lastbootuptime"],
                capture_output=True,
                text=True,
                check=True
            )
            boot_time_str = result.stdout.split('\n')[1].split('.')[0]
            boot_time = datetime.strptime(boot_time_str, "%Y%m%d%H%M%S")
        except Exception as e:
            print(f"Error getting uptime: {e}")
            return
    else:
        # Linux/macOS: Use /proc/uptime or uptime command
        try:
            if os.path.exists('/proc/uptime'):
                with open('/proc/uptime', 'r') as f:
                    uptime_seconds = float(f.readline().split()[0])
                boot_time = datetime.now() - timedelta(seconds=uptime_seconds)
            else:
                # Fallback for macOS
                import subprocess
                result = subprocess.run(
                    ["uptime", "-p"],
                    capture_output=True,
                    text=True,
                    check=True
                )
                print(f"System Uptime: {result.stdout.strip()}")
                return
        except Exception as e:
            print(f"Error getting uptime: {e}")
            return
    
    # Calculate uptime
    current_time = datetime.now()
    uptime_delta = current_time - boot_time
    
    # Format uptime
    total_seconds = int(uptime_delta.total_seconds())
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    print(f"System Boot Time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"System Uptime: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

if __name__ == "__main__":
    get_system_uptime()