from twisted.internet.defer import Deferred

def myCallback(age, name, sex):
	print age, name, sex
	return (age, name)

def trueGuy(res):
	print "My full name is", res[1]+' Appleton' 
	print "My real age is", res[0]+10


d = Deferred()
d.addCallback(myCallback, name='Larry', sex='male')
d.addCallback(trueGuy)
d.callback(29)
