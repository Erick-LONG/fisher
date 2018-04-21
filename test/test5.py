# 线程隔离
import threading

import time
from werkzeug.local import Local,LocalStack

my_stack = LocalStack()
my_stack.push(1)

def worker():
    my_stack.push(2)
    print('new thread b is ' + str(my_stack.top)) #2


new_t = threading.Thread(target=worker,name='qq_thread')
new_t.start()
time.sleep(1)

print('main thread b is' + str(my_stack.top))
#1

#使用线程隔离的意义在于：使当前线程能正确的引用到他自己所创建的对象，而不是引用到其他线程所创建的对象