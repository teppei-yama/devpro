#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2023 Summer)
# Week 04
#
# Sample Python code of multi-threads

# May 4, 2023
# Michiharu Takemoto (takemoto.development@gmail.com)

# 
# MIT License
# 
# Copyright (c) 2023 Michiharu Takemoto <takemoto.development@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
# 

import threading
import time
import random

def print_x_and_wait(t_number):
    global x

    head_blank = ' ' * t_number * 10

    y = x 
    print('t%d' %t_number + head_blank + ': x=%d' %x)
    wait_time = random.randint(1, 5)
    print('t%d' %t_number + head_blank  + ':  waiting %d sec.' %wait_time)
    time.sleep(wait_time)

    y = y + 1

    x = y
    print('t%d' %t_number + head_blank  + ":   ->x=%d" %x)

    wait_time = random.randint(1, 5)
    print('t%d' %t_number + head_blank  + ':    waiting %d sec.' %wait_time)
    time.sleep(wait_time)

def single_thread_test():
    global x
    x = 10
    print_x_and_wait(0)
    print_x_and_wait(0)
    print_x_and_wait(0)
    print_x_and_wait(0)


def multithread_test1():
    global x
    x = 10

    t1 = threading.Thread(target=print_x_and_wait, args=(1, ))
    t1.start()
    time.sleep(1)

    t2 = threading.Thread(target=print_x_and_wait, args=(2, ))
    t2.start()
    time.sleep(1)

    t3 = threading.Thread(target=print_x_and_wait, args=(3, ))
    t3.start()
    time.sleep(1)

    t4 = threading.Thread(target=print_x_and_wait, args=(4, ))
    t4.start()

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    print("single (1) thread")
    single_thread_test()

    print("-------------")
    print("OK?")
    print("four (4)-threads")
    multithread_test1()
    



