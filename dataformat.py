import re
from copy import deepcopy
import csv
# TAKLA WAS HERE
class ThermData:

	def __init__(self, filename, calibration = []):
		self.name = filename.replace(".txt","")
		self.data = self.extractData(filename)
		self.calib = []
		self.formattedData = []

		if calibration == []:
			 self.calibrateData()
		else:
			self.calibrateData(calibration)

		self.formatData(self.data)

	def extractData(self, filename,numPairs = 8):
		with open(filename, "r") as f:
			data = f.read()
		
		lineChar = '\r'
		rows = self.__regExData(data,lineChar,numPairs)

		if len(rows) == 0:
			lineChar = '\n'
			rows = self.__regExData(data,lineChar,numPairs)

		for i in range(len(rows)):
			rows[i] = rows[i].replace("N",str(i)).replace(lineChar,"").strip(";")
			rows[i] = rows[i].split(";")
			rows[i] = map(int,rows[i])
		return rows

	def getName (self):
		return self.name

	def getData (self):
		return self.data

	def getCalibData (self):
		return self.calib

	def getFormattedData (self):
		return self.formattedData

	def calibrateData (self, calibration = [[0,1,2,3,4,5],[0,819,1638,2458,3277,4095]]):

		calibData = deepcopy(self.data)

		for i in range(len(calibData)):
			for j in range(1,len(calibData[1])):
				val = calibData[i][j]
				calibData[i][j] = self.__findCalibVal(calibration, val)

		self.calib = calibData

	def formatData(self,data):
		formatData = deepcopy(data)

		for i in range(len(formatData)):
			for j in [0,8]:
				self.__swap(formatData[i],j+2,j+5)
				self.__swap(formatData[i],j+2,j+3)
				self.__swap(formatData[i],j+4,j+7)
				self.__swap(formatData[i],j+6,j+7)

		self.formattedData = formatData

	def exportData(self, data, filename):
		with open(filename, "w") as f:
			dataStr = ""
			for i in range(len(data)):
				dataStr = dataStr + str(data[i]).strip("[]") + "\n"
			f.write(dataStr)
	
	#averages the data grouping n values into one.
	def averageData(data, n):
		length = len(data)%n #number of group of n that can be created.
		avgData = []

		for i in range(length):
			avgRow = deepcopy(datat[i*n])
			for j in range (len(data)):
				for k in range(1,17):
					# data[i][k]
					pass
	
	def writeToCSV(self, data, csvname):
		with open(csvname, 'wb') as csvfile:
			linkswriter = csv.writer(csvfile, delimiter=',')
			linkswriter.writerows(data)

	def __regExData(self, data, escChar, numPairs):
		regEx = "N;"
		digPair = escChar +"\d+;\d+;"

		regEx += digPair*numPairs

		lineFinder = re.compile(regEx)
		rows = re.findall(lineFinder, data)

		return rows



	def __findIndexPair(self, calLst, val):
		calLen = len(calLst)
		ind1 = min(range(calLen), key=lambda i: abs(calLst[i]-val))

		if ind1 != 0 or ind1 != calLen-1:
			ind2 = min([ind1-1, ind1+1], key = lambda i: abs(calLst[i]-val))
		elif ind1 == 0:
			ind2 = 1
		elif ind1 == calLen -1:
			ind2 = calLen -2
		
		indPair = [ind1, ind2]
		indPair.sort()

		return indPair

	def __findCalibVal(self,calibData, val):
		indexPair = self.__findIndexPair(calibData[1], val)
		low = indexPair[0]
		high = indexPair[1]
		thermData = calibData[0]
		binVals = calibData[1]

		mult = (thermData[high] - thermData[low])/float(binVals[high] - binVals[low])
		calibVal = mult*val

		return round(calibVal,4)
	
	def __swap (self,lst, i,j):
		lst[i], lst[j] = lst[j], lst[i]

	

therm1 = ThermData("tempramp2.txt")
# print therm1.getData()
# print therm1.getCalibData()
therm1.exportData(therm1.getFormattedData(),therm1.getName()+"_Export.txt")
# therm1.writeToCSV(therm1.getFormattedData(),therm1.getName()+"_CSV.csv")




