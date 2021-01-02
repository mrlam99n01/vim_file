import time
import concurrent.futures
start = time.perf_counter()


def do_something(seconds):
    print('Sleeping 1 second...')
    time.sleep(seconds)
    return 'Done something ... ' 

with concurrent.futures.ThreadPoolExecutor() as executor:
    results  = [executor.submit(do_something,1) for _ in range(10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something,args=[1.5])
#     t.start()
#     threads.append(t)
# for thread in threads:
#     thread.join()
finish = time.perf_counter()

print(f'Finish in {round(finish-start,2)} second(s)')
