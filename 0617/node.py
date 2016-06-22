#-*- coding: utf-8 -*-

class Node:
	def __init__(self, name, target_count, point_distribute, point, start_part):
		self.name = name
		self.target_count = target_count
		self.point_distribute = point_distribute
		self.point = point
		self.start_part = start_part
		
	def getName(self):
		return self.name

	def addTargetCount(self):  			# いくつのnodeに配分するのか数える
		self.target_count += 1
	
	def CalculatePoint(self):  			# 今回各nodeにこのnodeからいくつ足せばいいか計算する
		if self.target_count != 0:		# target_countが0のものは除く
			self.point_distribute = float(self.point / self.target_count)

	def getPointDistribute(self):
		return self.point_distribute

	def UpdatePoint(self, point): 		# 各nodeから得たpointを足してこのnodeの新しいpointにする
		self.point = point
		if self.target_count == 0:		# どのnodeにも分配しないとき、もとのpointはすべて自分のpointになる
			self.point += 100.0

	def getPoint(self):
		return self.point

	def setStart(self, start_temp): 	# どのnodeからpointがもらえるのか格納しておく
		(self.start_part).append(start_temp)

	def getStart(self):
		return self.start_part

	def printInfo(self):
		print "%s: %.3lf" % (self.name, self.point)
