#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##	Program: 	My Angle 1
##	Filename:	myAngle1.py
##	Author:		0m3g4b1u3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class Angle():
	def __init__(self, degree):
		self._degree = float(degree)

	def __str__(self):
		rString = "Measure: %.3lf\n" % self.degree
		rString += "Complement: %.3lf\n" % self.getComp()
		return rString

	@property
	def degree(self):
		return self._degree

	@degree.setter
	def degree(self, val):
		while(val >= 180):
			val = val - 180
		self._degree = val

	def getComp(self):
		return 90 - self.degree

	def getSup(self):
		return 180 - self.degree

	def possLP(self, other):
		rString = ""
		if self.degree + other.degree == 180:
			if self.degree > 90:
				rString += "\t /\n"
				rString += "  %.1lf\t/ %.1lf\n" % (self.degree , other.degree )
				rString += "----------------\n"
				rString += "Could be Linear Pairs"
			else:
				rString += "\t /\n"
				rString += "  %.1lf\t/ %.1lf\n" % (other.degree , self.degree )
				rString += "----------------\n"
				rString += "Could be Linear Pairs"
		else:
			rString += "Could not be Linear Pairs"
		return rString

	def possVert(self, other):
		rString = ""
		if self.degree == other.degree:
			if self.degree < 90:
				rString += "\t  /\n"
				rString += "\t / %.1lf\n" % self.degree
				rString += "-----------------\n"
				rString += "  %.1lf /\n" % other.degree
				rString += "      /\n\n"
				rString += "Could be Vertical Angles"
			else:
				rString += "\t /\n"
				rString += "  %.1lf\t/\n" % other.degree
				rString += "-----------------\n"
				rString += "      / %.1lf\n" % self.degree
				rString += "     /\n\n"
				rString += "Could be Vertical Angles"
		else:
			rString += "Could not be Vertical Angles"
		return rString

##  Start Program  ##
angle1 = Angle(72)
angle2 = Angle(72)

print(angle1.possVert(angle2))
