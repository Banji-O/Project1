# Queue

# Uses memory buffer to share data. First In First Out: FIFO while stack is Last In First Out: LIFO
# List can work as queue like the example below, but it has problem when dealing with dynamic array


wmt_stock_price_queue = []

wmt_stock_price_queue.insert(0, 131.10)
wmt_stock_price_queue.insert(0, 132.12)
wmt_stock_price_queue.insert(0, 135)

print(wmt_stock_price_queue)
print(wmt_stock_price_queue.pop())
print(wmt_stock_price_queue.pop())

# Deque will be used for such dynamic array

from collections import deque
q = deque()

q.appendleft(5)
q.appendleft(8)
q.appendleft(27)

print(q.pop())

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


pq = Queue()

pq.enqueue({
    "company": "wal Mart",
    "timestamp": "15 apr. 11.01 AM",
    "price": 131.10
})

pq.enqueue({
    "company": "Wal Mart",
    "timestamp": "15 apr, 11:02 AM",
    "price": 132
})

pq.enqueue({
    "company": "Wal Mart",
    "timestamp": "15 apr, 11.03 AM",
    "price": 135
})

print(pq.buffer)
print(pq.dequeue())

# Exercise

"""
Use Queue class  to implement a food ordering system where the python program will run two threads;

1. Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. 
(hint: use time.sleep(0.5) function)

2. Serve Order: This thread will serve the order. pop the order out of the queue and print it. This thread serves an order every 2 seconds. 
Also start this thread 1 second after place order thread is started.

Pass the following list as an argument to place order thread:

orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
"""

import time
import threading
from collections import deque


# Define the custom Queue class
class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


# Define the function for placing orders
def place_order(order_queue, orders):
    for order in orders:
        print(f"Placing order: {order}")
        order_queue.enqueue(order)  # Add order to the queue
        time.sleep(0.5)  # Wait for 0.5 seconds before placing the next order


# Define the function for serving orders
def serve_order(order_queue):
    while True:
        order = order_queue.dequeue()  # Get the next order from the queue
        if order is None:  # If None is received, exit the loop
            break
        print(f"Serving order: {order}")
        time.sleep(2)  # Wait for 2 seconds before serving the next order


# Main function to start the threads
def main():
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']  # List of orders
    order_queue = Queue()  # Create a queue to hold the orders

    # Create the threads for placing and serving orders
    place_order_thread = threading.Thread(target=place_order, args=(order_queue, orders))
    serve_order_thread = threading.Thread(target=serve_order, args=(order_queue,))

    # Start the place order thread
    place_order_thread.start()

    # Wait for 1 second before starting the serve order thread
    time.sleep(1)
    serve_order_thread.start()

    # Wait for the place order thread to finish
    place_order_thread.join()

    # Signal the serve order thread to stop by enqueueing None
    order_queue.enqueue(None)

    # Wait for the serve order thread to finish
    serve_order_thread.join()


# Run the main function
if __name__ == "__main__":
    main()
