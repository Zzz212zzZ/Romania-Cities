from flask import Flask, render_template, request
import A_star
import re
import SearchB
import SearchD

class Node(object):
    def __init__(self, name):
        self.name = name
        # self.nextV=nextV  #如果nextV不是空，则可以找到nextN
        self.connectedNodes = {}   #临界点:value


vers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'L',
        'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Z']
edges = [['A', 'Z', 75], ['A', 'T', 118], ['A', 'S', 140], ['Z', 'O', 71], ['T', 'L', 111], ['S', 'O', 151],
         ['L', 'M', 70], ['M', 'D', 75], ['D', 'C', 120], [
             'S', 'F', 99], ['S', 'R', 80], ['C', 'R', 146],
         ['C', 'P', 138], ['R', 'P', 97], ['F', 'B', 211], [
             'P', 'B', 101], ['B', 'G', 90], ['B', 'U', 85],
         ['U', 'H', 98], ['U', 'V', 142], ['V', 'I', 92], ['H', 'E', 86], ['I', 'N', 87]]
def loadLocation(vers):
        # return首字母坐标组成的字典
    locationStr = "Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),\
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),\
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),\
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),\
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),\
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),\
    Vaslui=(509, 444), Zerind=(108, 531))"
    p = re.compile(r"[(](.*?)[)]", re.S)
    locationStrList = re.findall(p, locationStr)
    locationDic = {}
    for num, location in enumerate(locationStrList):
        tmpLocation = location.split(", ")  # 化为[x,y]的形式
        tmpLocation = [int(locationX) for locationX in tmpLocation]
        locationDic[vers[num]] = tmpLocation

    return locationDic


def initAdList(vers, edges):
    # 初始化邻接表的首元素，用名称来初始化
    adList = {}  # node名:结点实体
    for v in vers:
        adList[v] = Node(v)
    # 对于每一个点，遍历
    for node in adList.values():
        head = node.name
        for e in edges:
            if head in e:
                another = e[1] if head == e[0] else e[0]
                node.connectedNodes[another] = e[2]
    return adList

def modifyAns(ansDict):
    for num,openNodeName in enumerate(ansDict["openNodeNames"]):
        ansDict["openNodeNames"][num]="-".join(openNodeName)

    for num,expandedNodeName in enumerate(ansDict["expandedNodeNames"]):
        ansDict["expandedNodeNames"][num]="-".join(expandedNodeName)

    ansDict["rsNodeList"]="->".join(ansDict["rsNodeList"])
    


app = Flask(__name__)




@app.route('/')
def hello_world():
    global adList, locationDic
    adList = initAdList(vers, edges)
    locationDic = loadLocation(vers)
    return render_template('index.html')


@app.route('/searchA', methods=['POST', ])
def searchA():
    #返回的dict有：openNodeNames，expandedNodeNames,这两个数组需要转化
    #为了前端画线,需要知道是哪个expanded出去的，所以

    start = request.form.get("start")
    end = request.form.get("end")
    ansDict=A_star.search(start, end, adList, locationDic, edges)
    modifyAns(ansDict)
    # print(str(start))
    return ansDict

@app.route('/searchB', methods=['POST', ])
def searchB():
    #返回的dict有：openNodeNames，expandedNodeNames,这两个数组需要转化
    #为了前端画线,需要知道是哪个expanded出去的，所以
    start = request.form.get("start")
    end = request.form.get("end")
    ansDict=SearchB.search(start, end, adList)
    modifyAns(ansDict)
    # print(str(start))
    return ansDict

@app.route('/searchD', methods=['POST', ])
def searchD():
    #返回的dict有：openNodeNames，expandedNodeNames,这两个数组需要转化
    #为了前端画线,需要知道是哪个expanded出去的，所以
    start = request.form.get("start")
    end = request.form.get("end")
    ansDict=SearchD.search(start, end, adList)
    modifyAns(ansDict)
    # print(str(start))
    return ansDict


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')


