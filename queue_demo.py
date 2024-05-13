import threading
import requests
import re
import queue


# q = queue.Queue()

# # 1. 基础使用 q.put q.get
# for i in range(10):
#     q.put(i)
#
#
# while not q.empty():
#     data = q.get()
#     print(data, end=" ")
#
# print("Program execution completed")


# # 2. 宽度搜索
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def bfs(root):
#     q = queue.Queue()
#     q.put(root)
#     while not q.empty():
#         node = q.get()
#         print(node.data)
#         if node.left:
#             q.put(node.left)
#         if node.right:
#             q.put(node.right)
#
#
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
# bfs(root)


# 3. consumer & producer
import time


def consumer(q):
    time.sleep(1)
    while True:
        item = q.get()  # 阻塞  没有任务就阻塞
        print("consumer: ", item)
        q.task_done()


def producer(q):
    for i in range(10):
        q.put(i)
        print("producer: ", i)


q = queue.Queue(maxsize=3)

t1 = threading.Thread(target=consumer, args=(q,), daemon=True)
t2 = threading.Thread(target=consumer, args=(q,), daemon=True)
t1.start()
t2.start()

producer(q)
q.join()
