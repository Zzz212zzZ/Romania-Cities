import re
import math



def get_preVal(start,end,locationDic):
    def squareDist(x1, y1, x2, y2):
        return int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

    # x=[abs(dist[0]-locationDic['B'][0])+abs(dist[1]-locationDic['B'][1]) for dist in locationDic.values()]
    # preVal=abs(locationDic[start][0]-locationDic[end][0])+abs(locationDic[start][1]-locationDic[end][1])
    preVal=squareDist(locationDic[start][0],locationDic[start][1],locationDic[end][0],locationDic[end][1])

    # x = [squareDist(dist[0], dist[1], locationDic['B'][0], locationDic['B'][1]) for dist in locationDic.values()]
    # indexNum = vers.index(name)
    return preVal





class Node(object):
    def __init__(self, name):
        self.name = name
        # self.nextV=nextV  #如果nextV不是空，则可以找到nextN
        self.connectedNodes = {}


def search(start,end,adList,locationDic,edges):
# A*算法 
# return的有：每一轮的openList,closeList


# start = "A"
# end = "B"
    #每次迭代传入当时的openNodes的复制品
    openNodeNames=[[start]]
    expandedNodeNames=[[]]
    thisExpand=["none"]

    openNodes = {}  # {节点名称:[当前代价,预估代价]}
    come_from = {}
    currentNode = start
    openNodes[start] = [0, get_preVal(start,end,locationDic)]
    expandedNodes = []  # 是否已拓展
    # expandedNodes.append(start)

    while True:
        #----------------------- 先找到最小节点--------------------------
        openNodes = dict(sorted(openNodes.items(), key=lambda i: sum(i[1])))  # 根据值的和来进行排序  #Open表
        openNodesList=list(openNodes)
        currentNodeName = openNodesList[0][0]
        # openNodes.pop(currentNodeName)
        #----------------------- 先找到最小节点--------------------------
        # 判断这个节点是否是最终节点,若是的话，直接跳出，得到最佳结果
        #跳出条件是最优节点是最终结点，而不是说找到最终结点了就跳出
        thisExpand.append(currentNodeName)
        if (currentNodeName == end):
            expandedNodes.append(currentNodeName)
            openNodes.pop(currentNodeName)

            #存储
            expandedNodeNames.append(expandedNodes[:])
            openNodeNames.append(list(openNodes.keys())[:])


            break

        currentNode=adList[currentNodeName]
        # 拓展这个节点，将该节点加入到所有节点的字典中,加入的同时还需要计算其预估值
        # 然后遍历它的邻接表，对于已有节点，可以尝试更新其新的当前代价（如果更优的话）
        for connectedNodeName, expandVal in currentNode.connectedNodes.items():
            if connectedNodeName in expandedNodes:
                continue   #不考虑已拓展结点的更新，否则会一直迭代更新其附近的结点

            if connectedNodeName in openNodes :
                if openNodes[currentNode.name][0] + expandVal < openNodes[connectedNodeName][0]:  # 已有节点的当前代价+已有节点的拓展代价<待拓展节点的当前代价时
                    openNodes[connectedNodeName][0] = openNodes[currentNode.name][0] + expandVal
                    # 只有更新了，才更新come_from
                    come_from[connectedNodeName] = currentNode.name


            else:
                openNodes[connectedNodeName] = [openNodes[currentNode.name][0] + expandVal, get_preVal(connectedNodeName,end,locationDic)]
                come_from[connectedNodeName] = currentNode.name


        expandedNodes.append(currentNodeName)
        openNodes.pop(currentNodeName)

        #存储
        expandedNodeNames.append(expandedNodes[:])
        openNodeNames.append(list(openNodes.keys())[:])

    # 顺着comefrom找回去
    rsNodeList = [end]
    currentNodeName = end
    while (currentNodeName != start):
        currentNodeName = come_from[currentNodeName]
        rsNodeList.append(currentNodeName)

    rsNodeList.reverse()  # 最终遍历集合

    #计算实际距离
    dist=0
    for num in range(0,len(rsNodeList)-1):
        #取得相应的距离
        for edge in edges:
            if rsNodeList[num] in edge and rsNodeList[num+1] in edge:
                dist+=edge[-1]
                break

    return {"openNodeNames":openNodeNames,"expandedNodeNames":expandedNodeNames,"thisExpand":thisExpand,"rsNodeList":rsNodeList,"distance":dist}


    print(str(rsNodeList))
    print(f"{dist}")

