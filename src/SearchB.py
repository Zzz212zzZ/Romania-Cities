class Node(object):
    def __init__(self, name):
        self.name = name
        # self.nextV=nextV  #如果nextV不是空，则可以找到nextN
        self.connectedNodes = {}




def search(start,end,adList):
    # 广度遍历
    openNodeNames=[[start]]
    expandedNodeNames=[[]]
    thisExpand=["none"]

    openNodes = [start]  # {节点名,当前代价}
    expandedNodes=[]
    come_from = {}  # 在里面说明被访问过
    # come_from[start] = start
    loopFind = True

    while (loopFind):
        curNodeName = openNodes.pop(0)
        if(curNodeName=="U"):
            print(213)
        expandedNodes.append(curNodeName)

        # 这个节点开始拓展,先在邻接表中找到其位置
        connectedNodes = adList[curNodeName].connectedNodes

        # 再以此拓展其连接的节点，将它们加入到come_from中
        for nodeName in connectedNodes.keys():
            # 如果拓展到目标节点，即退出循环
            if (end == nodeName):
                openNodes.append(end)
                come_from[nodeName] = curNodeName
                loopFind = False
                break

            if nodeName in openNodes or nodeName in expandedNodes:
                continue

            else:
                openNodes.append(nodeName)
                come_from[nodeName]=curNodeName

        openNodeNames.append(openNodes[:])
        expandedNodeNames.append(expandedNodes[:])
        thisExpand.append(curNodeName)


    # 顺着comefrom找回去
    nodeList = [end]
    current = end
    last=None
    distance=0
    while (current != start):
        last = come_from[current]
        nodeList.append(last)
        distance+=adList[last].connectedNodes[current]
        current=last

    nodeList.reverse()  # 最终遍历集合

    rsDict= {"openNodeNames":openNodeNames,"expandedNodeNames":expandedNodeNames,"thisExpand":thisExpand,"rsNodeList":nodeList,"distance":distance}

    return rsDict


