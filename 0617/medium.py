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

	def addTargetCount(self):   # いくつのnodeに配分するのか数える
		self.target_count += 1
	
	def CalculatePoint(self):   # 今回各nodeにこのnodeからいくつ足せばいいか計算する
		if self.target_count != 0:   # target_countが0のものは除く
			self.point_distribute = float(self.point / self.target_count)

	def getPointDistribute(self):
		return self.point_distribute

	def UpdatePoint(self, point):   # 各nodeから得たpointを足してこのnodeの新しいpointにする
		self.point = point
		if self.target_count == 0:   # どのnodeにも分配しないとき、もとのpointはすべて自分のpointになる
			self.point += 100.0

	def getPoint(self):
		return self.point

	def setStart(self, start_temp):   # どのnodeからpointがもらえるのか格納しておく
		(self.start_part).append(start_temp)

	def getStart(self):
		return self.start_part

	def printInfo(self):
		print "%s: %.3lf" % (self.name, self.point)


def readLine () :
	itemList = []   # データの読み込み
	for line in open('/Users/LisaKawai/Desktop/STEP/0617/homework4/medium_data.txt', 'r'):
		itemList.append(line.replace('\n', ''))   # 改行コードを取り除いてリストにつけ足す

	count_node = int(itemList[0])

	nodeList = []   # 各nodeのデータを入れる
	for line in itemList[1: count_node + 1]:
		nodeList.append(Node(line, 0, 0.000, 100.000, []))   # nodeの初期値を埋め込む

	for line in itemList[count_node + 2:]:   # edgeは空白で区切ってedgeに格納
		edge = line.split()
		for i in nodeList:
			if edge[0] == i.getName():   # edgeのstartになる回数を数える 
				i.addTargetCount()
			elif edge[1] == i.getName():   # edgeのtargetになったとき、startとなっているnodeを調べる
				i.setStart(edge[0])
	
	return nodeList


def distribute (nodeList) :

	total = 0.000    # pointの合計の初期値
	total_estimate = len(nodeList) * 100.0   # pointの合計になっているはずの数
	
	map ( lambda line : line.CalculatePoint(), nodeList)   # 全てのnodeにたいして配分するpointを計算する
	map ( change_point, nodeList )   # 全てのnodeにたいしてpointを更新する

	for line in nodeList:   # nodeのpointを表示し、pointの合計を計算する
		line.printInfo()
		total += line.getPoint()

	if total > (total_estimate + 1) or total < (total_estimate - 1):   # pointの合計が間違っていないか確認
		print total, total_estimate
		print 'calculate error\n'


def change_point(n):
	temp_point = 0
	for line in range(len(n.getStart())):   # edgeのtargetになったときのstartからpointをもらう
		for i in nodeList:		
			if n.getStart()[line] == i.getName():
				temp_point += i.getPointDistribute()
	
	n.UpdatePoint(temp_point)


while True:
	nodeList = readLine()

	for count in range(1,51):
		print "<%d回目>" % count
		distribute ( nodeList )
	break
