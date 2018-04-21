# 线程隔离
import threading

import time
from werkzeug.local import Local

my_obj = Local()
my_obj.b = 1

def worker():
    my_obj.b = 2
    print('new thread b is ' + str(my_obj.b)) #2


new_t = threading.Thread(target=worker,name='qq_thread')
new_t.start()
time.sleep(1)

print('main thread b is' + str(my_obj.b))
#1