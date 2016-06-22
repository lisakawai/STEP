#-*- coding: utf-8 -*-
import node

def readLine () :
	itemList = []  														# データの読み込み
	for line in open('/Users/LisaKawai/Desktop/STEP/0617/homework4/medium_data.txt', 'r'):
		itemList.append(line.replace('\n', ''))  						# 改行コードを取り除いてリストにつけ足す

	count_node = int(itemList[0])

	nodeList = []  														# 各nodeのデータを入れる
	for line in itemList[1: count_node + 1]:
		nodeList.append(Node(line, 0, 0.000, 100.000, []))				# nodeの初期値を埋め込む

	for line in itemList[count_node + 2:]:  							# edgeは空白で区切ってedgeに格納
		edge = line.split()
		for i in nodeList:
			if edge[0] == i.getName():  								# edgeのstartになる回数を数える 
				i.addTargetCount()
			elif edge[1] == i.getName(): 								# edgeのtargetになったとき、startとなっているnodeを調べる
				i.setStart(edge[0])
	
	return nodeList


def distribute (nodeList) :

	total = 0.000 														# pointの合計の初期値
	total_estimate = len(nodeList) * 100.0 								# pointの合計になっているはずの数
	
	map ( lambda line : line.CalculatePoint(), nodeList)				# 全てのnodeにたいして配分するpointを計算する
	map ( change_point, nodeList )										# 全てのnodeにたいしてpointを更新する

	for line in nodeList:												# nodeのpointを表示し、pointの合計を計算する
		line.printInfo()
		total += line.getPoint()

	if total > (total_estimate + 1) or total < (total_estimate - 1):	# pointの合計が間違っていないか確認
		print total, total_estimate
		print 'calculate error\n'


def change_point(n):
	temp_point = 0
	for line in range(len(n.getStart())):								# edgeのtargetになったときのstartからpointをもらう
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
