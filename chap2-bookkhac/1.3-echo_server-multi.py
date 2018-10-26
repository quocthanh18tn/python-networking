#!/usr/bin/env python3

import tincanchat
import threading, queue

send_queues={}
q = queue.Queue()
p = queue.Queue()

send_queues[1]=q
send_queues[2]=p

p.put('t')
q.put('t')

