#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import random


class TimeRand:
	_day_h = 0
	_day_l = 0
	_sec_h = 0
	_sec_l = 0

	#input: "yyyy:mm:dd", "yyyy:mm:dd", "hh:mm:ss", "hh:mm:ss"
	def __init__(self, day_l, day_h, sec_l, sec_h):
		self._day_h = self.get_day(day_h)
		self._day_l = self.get_day(day_l)
		self._sec_h = self.get_sec(sec_h)
		self._sec_l = self.get_sec(sec_l)
		random.seed(time.time())
		if self._day_h == 0 or self._day_l == 0 or self._sec_h == 0 or self._sec_l == 0:
			print "input params error"

	#input: "yyyy:mm:dd"
	def get_day(self, day):
		try:
			day_ = day.strip().split(":")
			if len(day_) != 3:
				return 0
			list_ = [int(d) for d in day_]
			year_ = list_[0]
			month_ = list_[1]
			day_ = list_[2]
			if year_ < 1970 or year_ > 2017 or month_ < 1 or month_ > 12 or day_ < 1 or day_ > 31:
				return 0
			t = time.struct_time([year_,month_,day_,0,0,0,-1,-1,-1])
			return time.mktime(t)
		except Exception, e:
			print e
			return 0

	#input "hh:mm:ss"
	def get_sec(self, sec):
		try:
			sec_ = sec.strip().split(":")
			if len(sec_) != 3:
				return 0
			list_ = [int(s) for s in sec_]
			hour_ = list_[0]
			minute_ = list_[1]
			second_ = list_[2]
			if hour_ < 0 or hour_ > 23 or minute_ < 0 or minute_ > 59 or second_ < 0 or second_ > 59:
				return 0
			return hour_*3600+minute_*60+second_
		except Exception, e:
			print e
			return 0

	def get_rand_day(self):
		begin = int(self._day_l / 86400) * 86400;
		end = int(self._day_h / 86400) * 86400 + 86399
		return int(random.randint(begin, end) / 86400 ) * 86400

	def get_rand_sec(self):
		return random.randint(self._sec_l, self._sec_h)
	
	#100个/1ms左右
	def get(self):
		return self.get_rand_day() + self.get_rand_sec()

if __name__ == "__main__":
	tr = TimeRand("2001:3:23","2001:3:23","3:4:5","4:5:6")
	for i in range(100000):
		t = tr.get()
	print t
	print time.gmtime(t)
