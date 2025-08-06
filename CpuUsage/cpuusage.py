import psutil
import time

THRESHOLD = 80
print("Monitoring CPU usage... Press Ctrl+C to stop.\n")
try:
    while True:
        usage = psutil.cpu_percent(interval=1)
        if usage > THRESHOLD:
            print(f"Alert! CPU usage exceeds threshold: {usage}%")
        time.sleep(5)
except KeyboardInterrupt:
    print("Monitoring stopped.")  
