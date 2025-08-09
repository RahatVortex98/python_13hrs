# Implement an exponential backoff stratedy that doubles the wait time between retries starting from 1sec, but stops after 5 retries


import time

wait_time = 1  # start with 1 second

for attempt in range(1, 6):  # 5 retries
    print(f"Attempt {attempt}...")
    # Simulate a failure
    print(f"Failed! Waiting {wait_time} seconds before retrying...")
    time.sleep(wait_time)
    wait_time *= 2  # double the wait time
