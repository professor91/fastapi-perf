import threading
import requests
import time

URL = "http://127.0.0.1:8000"
NUM_REQUESTS = 2000  # total requests
CONCURRENT_THREADS = 10

success = 0
fail = 0

def make_request():
    global success, fail
    try:
        response = requests.get(URL)
        if response.status_code == 200:
                success += 1
        else:
            fail += 1
    except:
        fail += 1

def run_test():
    global success, fail
    threads = []
    start_time = time.time()

    for _ in range(NUM_REQUESTS):
        t = threading.Thread(target=make_request)
        threads.append(t)
        t.start()

        # Limit concurrency
        while threading.active_count() > CONCURRENT_THREADS:
            pass

    for t in threads:
        t.join()

    duration = time.time() - start_time
    print(f"Completed {NUM_REQUESTS} requests in {duration:.2f} seconds")
    print(f"Success: {success}, Fail: {fail}")
    print(f"Requests per second: {success / duration:.2f}")

if __name__ == "__main__":
    run_test()
