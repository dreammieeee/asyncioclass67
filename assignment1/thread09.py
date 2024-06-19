#Basic Synchonization Using Lock
import concurrent.futures
import logging
import threading 


class FakeDatabase:
    def init(self):
        self.value = 0
        self.lock = threading.Lock()

    def lockedupdate(self,name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread $s about to lock", name)
        with self.lock:
            logging.debug("thread %s has lock", name)
            localcopy =+1
            time.sleep(0.1)
            self.value = localcopy
            logging.dubug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)

if __name__ == "__main":
    format ="%s(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")
    #logging.getLogger().setLevel(logging.debug)

    database = FakeDatabase()
    logging.info(
        "Testing locked update. Starting value  is %d.",database.value
    )
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    logging.info("TEst locked update. ENding Value is%d", database.value)