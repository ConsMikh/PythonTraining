'''
Futures provide distinct boundaries between the different threads or processes. Similar to
the multiprocessing pool, they are useful for call and answer type interactions, in which
processing can happen in another thread and then at some point in the future (they are
aptly named, after all), you can ask it for the result. It's really just a wrapper around
multiprocessing pools and thread pools, but it provides a cleaner API and encourages nicer
code.

A future is an object that wraps a function call. That function call is run in the background, in
a thread or process. The  future  object has methods the main thread can use to check
whether the future has completed and to get the results after it has completed.
'''

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from os.path import sep as pathsep
from collections import deque


def find_files(path, query_string):
    subdirs = []
    for p in path.iterdir():
        full_path = str(p.absolute())
        if p.is_dir() and not p.is_symlink():
            subdirs.append(p)
        if query_string in full_path:
                print(full_path)
    return subdirs


query = '.py'
futures = deque()
basedir = Path(pathsep).absolute()
print(f"basedir: {basedir}")
with ThreadPoolExecutor(max_workers=10) as executor:
    futures.append(
        executor.submit(find_files, basedir, query))
    while futures:
        future = futures.popleft()
        if future.exception():
            continue
        elif future.done():
            subdirs = future.result()
            for subdir in subdirs:
                futures.append(executor.submit(
                    find_files, subdir, query))
        else:
            futures.append(future)

'''
The meat of the program is known as an event loop. We can construct a
ThreadPoolExecutor  as a context manager so that it is automatically cleaned up and
closes its threads when it is done. It requires a  max_workers  argument to indicate the
number of threads running at a time. If more than this many jobs are submitted, it queues
up the rest until a worker thread becomes available. When using  ProcessPoolExecutor ,
this is normally constrained to the number of CPUs on the machine, but with threads, it can
be much higher, depending how many are waiting on I/O at a time. Each thread takes up a
certain amount of memory, so it shouldn't be too high. It doesn't take all that many threads
before the speed of the disk, rather than the number of parallel requests, is the bottleneck.

Once the executor has been constructed, we submit a job to it using the root directory. The
submit()  method immediately returns a  Future  object, which promises to give us a result
eventually. The future is placed in the queue. The loop then repeatedly removes the first
future from the queue and inspects it. If it is still running, it gets added back to the end of
the queue. Otherwise, we check whether the function raised an exception with a call to
future.exception() . If it did, we just ignore it (it's usually a permission error, although
a real app would need to be more careful about what the exception was). If we didn't check
this exception here, it would be raised when we called  result()  and could be handled
through the normal  try...except  mechanism.
'''