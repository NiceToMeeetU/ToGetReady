# coding   : utf-8 
# @Time    : 21/02/25 9:10
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : data_structure.py
# @Software: PyCharm


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 1:
            return self.stack[-1]
        else:
            return None


class Queue:
    """
    环形队列
    - 创建时应该指定长度
    - 指针的移动不要直接加1，应该加一后模长度，可实现环形指针移动
    """

    def __init__(self, size=100):
        self.queue = [0] * size
        self.size = size
        self.rear = 0  # 队尾指针
        self.front = 0  # 队首指针

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is filled.")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty.")

    def is_empty(self):
        return self.rear == self.front

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front


# 造个轮子试一下即可，实际多使用官方模块
from collections import deque

q = deque()


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_linklist_head(li):
    """
    头插法创建链表
    :param li:
    :return:
    """
    res = Node(li[0])


def create_linklist_tail(li):
    """
    尾插法创建链表
    :param li:
    :return:
    """