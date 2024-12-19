

def search(start,end,adList):

    openNodeNames=[[start]]
    expandedNodeNames=[[]]
    thisExpand=["none"]


    come_from = {}
    openNodes = [start]  # [name]
    expandedNodes=[]

    loopFind = True

    while (loopFind):
        curNodeName = openNodes.pop(0)
        expandedNodes.append(curNodeName)
        connectedNodes =adList[curNodeName].connectedNodes
        # 这个节点开始拓展,先在邻接表中找到其位置

        # 稍微智能一点?（需要吗），类似于贪婪，按从大到小的方式入栈（即下一次是最小的开始） 这个题不适用？
        # connectedNodes=connectedNodes.
        for nodeName in connectedNodes.keys():
            # if (k in come_from):
            #     continue
            if (nodeName == end):
                come_from[nodeName] = curNodeName
                openNodes.append(nodeName)
                # expandedNodes.append(nodeName)
                loopFind = False
                break

            if (nodeName not in openNodes and nodeName not in expandedNodes):
                come_from[nodeName] = curNodeName
                openNodes.insert(0, nodeName)

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

