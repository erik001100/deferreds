from twisted.internet.defer import Deferred

def myCallback(age):
	return age

def realAge(x):
	return x+1

def exactAge(x):
	print x*2

d = Deferred()
d.addCallback(myCallback)
d.addCallback(realAge)
d.addCallback(exactAge)
d.callback(29)
#d.callback(3)