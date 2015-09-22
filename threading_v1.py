import thread
import threading
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % ( threadName, time.ctime(time.time()))
        
#create two threads
def create_threads():
    try:
        thread.start_new_thread(print_time, ("Thread -1", 2, ))
        thread.start_new_thread(print_time, ("Thread -2", 4, ))
    except:
        print "Unable to start new thread"

def main():
    create_threads()
    print "Number of threads: " + str(threading.activeCount())
    print "Enumerated threads: "
    print threading.enumerate()

if __name__ == "__main__":
    main()