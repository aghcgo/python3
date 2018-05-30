#! /usr/bin/python3
import redis
import time
import random
r=redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)
def fun():
	i=0
	while i<1000:
		print("ID"+str(i)+":   ",r.get("ID"+str(i)))
		i+=1

while True:
	fun()
	time.sleep(1)
