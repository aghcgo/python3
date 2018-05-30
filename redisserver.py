#! /usr/bin/python3
import redis
import time
import random
r=redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)
def fun():
	i=0
	while i<1000:
		r.set("ID"+str(i),"华能华能呼伦贝尔公司的好人"+str(random.random()))
		i+=1

while True:
	fun()
	time.sleep(1)
