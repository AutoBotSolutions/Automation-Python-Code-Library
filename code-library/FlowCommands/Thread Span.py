## Me
thread span example

## AI Assistant
``` python
import threading
import time


# A task function to be executed in the thread
def task_function(span_name):
    print(f"Thread {span_name} started.")
    time.sleep(2)  # Simulating some work
    print(f"Thread {span_name} completed.")


# Creating threads
thread1 = threading.Thread(target=task_function, args=("Span-1",))
thread2 = threading.Thread(target=task_function, args=("Span-2",))

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to finish (Thread Join - ensure completion of the span)
thread1.join()
thread2.join()

# Completion message
print("All threads (spans) are complete.")
```
``` 
Thread Span-1 started.
Thread Span-2 started.
Thread Span-1 completed.
Thread Span-2 completed.
All threads (spans) are complete.
```


