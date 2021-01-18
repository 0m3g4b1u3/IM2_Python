################################################################################
##	Program: 	My Line
##	Filename:	myLine.py
##	Author:		0m3g4b1u3
################################################################################
class Line():
    def __init__(self, slope, y_int):
        self.slope = float(slope)
        self.y_int = float(y_int)

    def __str__(self):
        rString = "#"*43+"\n"
        rString += "####       LINE INFO GENERATOR        #####\n"
        rString += "#"*43+"\n\n"
        rString += "Slope-Intercept Form: y = %.3lfx + %.3lf\n\n" % (self.slope, self.y_int)
        ##  EXTEND IT!  ##
        rString += "Dont forget the \\n at the end of each line, \ntwo will add an extra break like above. O.o \n"
        return rString

    @property
    def slope(self):
        return self.__slope

    @slope.setter
    def slope(self, val):
        self.__slope = val

    @property
    def y_int(self):
        return self.__y_int

    @y_int.setter
    def y_int(self, val):
        self.__y_int = val

##  PROGRAM START  ##
my_line = Line(2, 8)
print(my_line)
