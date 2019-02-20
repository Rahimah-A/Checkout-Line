'''
Created on Feb 14, 2019

@author: Rahimah Abdul-Karim
'''
import random, threading, time, os
from threading import Thread


cust_queue = []
class Customer(Thread):
    def __init__(self):
        Thread.__init__(self, name = "thread1")
    #add a new customer to the queue if the number of customers waiting is less than 5
    def enter(self):
        time1 = 0
        while time1 < 120:            
            if len(cust_queue) <5:
                cust_queue.append(random.randint(5,60))
                os.system('cls')
                print("customer is entering the queue\n", cust_queue)
            elif len(cust_queue)<1:
                break
            elif time1 > 120:
                break
            time1 = time1+1
            time.sleep(1.0)

class Process_Cust(Thread):
    def __init__(self):
        Thread.__init__(self, name = "thread2")        
    #decrement the amount of time for the customer to be processed    
    def proc_cust(self):
        time2 = 0
        while time2 < 120:            
            if cust_queue[0]>0:
                temp = cust_queue[0]
                temp = temp-1
                cust_queue[0] = temp                
            elif cust_queue[0] == 0:
                del cust_queue[0]              
            else:
                print("the queue is empty")
                break
            os.system('cls')
            print(cust_queue)
            time.sleep(1.0)
            time2 = time2 +1

if __name__=="__main__":
    thread1, thread2 = Customer(), Process_Cust() 
    threading.Timer(0.5, thread1.enter).start()
    threading.Timer(1.0, thread2.proc_cust).start()
        