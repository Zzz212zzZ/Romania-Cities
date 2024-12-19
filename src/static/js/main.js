timeInterval=500
rsTimeInterval=100
pathColor="#bfcfff"
rsColor="#a6caa1"
trId=""
rsCnt=0

edgelist = [['A', 'Z'], ['A', 'T'], ['A', 'S'], ['Z', 'O'], ['T', 'L'], ['S', 'O'], ['L', 'M'], ['M', 'D'], ['D', 'C'], ['S', 'F'], ['S', 'R'], ['C', 'R'], ['C', 'P'], ['R', 'P'], ['F', 'B'], ['P', 'B'], ['B', 'G'], ['B', 'U'], ['U', 'H'], ['U', 'V'], ['V', 'I'], ['H', 'E'], ['I', 'N']];


function createLineElement(x, y, length, angle, id) {
    var line = document.createElement("div");
    line.setAttribute("id", id)
    var styles = 'border: 1px solid black; '
        + 'width: ' + length + 'px; '
        + 'height: 0px; '
        + '-moz-transform: rotate(' + angle + 'rad); '
        + '-webkit-transform: rotate(' + angle + 'rad); '
        + '-o-transform: rotate(' + angle + 'rad); '
        + '-ms-transform: rotate(' + angle + 'rad); '
        + 'position: absolute; '
        + 'top: ' + y + 'px; '
        + 'left: ' + x + 'px; ';
    line.setAttribute('style', styles);
    return line;
}

function createLine(x1, y1, x2, y2, id) {
    var a = x1 - x2,
        b = y1 - y2,
        c = Math.sqrt(a * a + b * b);

    var sx = (x1 + x2) / 2,
        sy = (y1 + y2) / 2;

    var x = sx - c / 2,
        y = sy;

    var alpha = Math.PI - Math.atan2(-b, a);

    return createLineElement(x, y, c, alpha, id);
}
// 获取元素坐标
function getElementOffset(element) {
    let offset = { left: 0, top: 0 }
    let current = element.offsetParent

    offset.left += element.offsetLeft
    offset.top += element.offsetTop

    while (current !== null) {
        offset.left += current.offsetLeft
        offset.top += current.offsetTop
        current = current.offsetParent
    }
    return offset
}

// id1第一个元素的id，id2第二个元素的id
function drawLines() {
    for (var i = 0; i < edgelist.length; i++) {
        points = edgelist[i];
        p1 = document.getElementById(points[0])
        p2 = document.getElementById(points[1])
        document.body.appendChild(createLine(340 + parseInt(p1.style["left"]) + 21,
            8 + parseInt(p1.style["top"]) + 16,
            340 + parseInt(p2.style["left"]) + 21,
            8 + parseInt(p2.style["top"]) + 16, points[0] + points[1]
        ))
    }



}
drawLines()


original = "<g id='cube-2' data-name='cube'><rect class='cls-1'></rect><path class='cls-2'd='M20.66,7.26a0,0,0,0,1,0,0l0,0c0-.07-.1-.14-.15-.21l-.09-.1a2.5,2.5,0,0,0-.86-.68l-6.4-3h0a2.7,2.7,0,0,0-2.26,0l-6.4,3a2.6,2.6,0,0,0-.86.68L3.52,7a1,1,0,0,0-.15.2l0,0a0,0,0,0,1,0,0A2.39,2.39,0,0,0,3,8.46v7.06a2.49,2.49,0,0,0,1.46,2.26l6.4,3a2.7,2.7,0,0,0,2.27,0l6.4-3A2.49,2.49,0,0,0,21,15.54V8.46A2.39,2.39,0,0,0,20.66,7.26Zm-8.95-2.2a.73.73,0,0,1,.58,0l5.33,2.48L12,10.15,6.38,7.54ZM5.3,16a.47.47,0,0,1-.3-.43V9.1l6,2.79v6.72Zm13.39,0L13,18.61V11.89L19,9.1v6.44A.48.48,0,0,1,18.69,16Z'></path></g>"

black = "<g id='cube-2' data-name='cube'><rect class='cls-1'></rect><path class='cls-2' d='M11.25,11.83,3,8.36v7.73a1.69,1.69,0,0,0,1,1.52L11.19,21l.06,0Z'></path><path class='cls-2'd='M12,10.5l8.51-3.57A1.62,1.62,0,0,0,20,6.55L12.8,3.18a1.87,1.87,0,0,0-1.6,0L4,6.55a1.62,1.62,0,0,0-.51.38Z'></path><path class='cls-2' d='M12.75,11.83V21l.05,0L20,17.61a1.69,1.69,0,0,0,1-1.51V8.36Z'></path></g>"

right = "<g id='done-all-2' data-name='done-all'><rect class='cls-1'></rect><path class='cls-2'd='M16.62,6.21a1,1,0,0,0-1.41.17l-7,9L4.78,11.2a1,1,0,1,0-1.56,1.25l4.17,5.18a1,1,0,0,0,.78.37h0A1,1,0,0,0,9,17.62l7.83-10A1,1,0,0,0,16.62,6.21Z'></path><path class='cls-2'd='M21.62,6.21a1,1,0,0,0-1.41.17l-7,9-.61-.75-1.26,1.62,1.1,1.37a1,1,0,0,0,.78.37h0a1,1,0,0,0,.78-.38l7.83-10A1,1,0,0,0,21.62,6.21Z'></path><path class='cls-2' d='M8.71,13.06,10,11.44l-.2-.24A1,1,0,0,0,8.37,11a1,1,0,0,0-.15,1.41Z'></path></g>"


function clearMap(algorithm){
    //图标还原
    var svgCollection=document.querySelectorAll("svg")
    svgCollection.forEach(function(svgItem){
        var svgName=svgItem.getAttribute("id")
        // console.log(svgName)
        changeSVG(svgName,original)
    })

    //线还原
    edgelist.forEach(function(points){
        var myLine=document.getElementById(points[0]+points[1])
        myLine.style["border"]="1px solid black"
    })

    //表格初始化
    trId=""
    var thVal=""
    if(algorithm[algorithm.length-1]==="A"){
        console.log("213")
        trId="#ARow"
        thVal="A*算法"
    }

    if(algorithm[algorithm.length-1]==="B"){
        trId="#BRow"
        thVal="广搜算法"
    }

    if(algorithm[algorithm.length-1]==="D"){
        trId="#DRow"
        thVal="深搜算法"
    }

    // console.log(trName)

    var str="<th scope='row'>"+thVal+"</th>\
    <td id='open'>{}</td>\
    <td id='close'>{}</td>\
    <td id='cnt'>nan</td>\
    <td id='path'>?-?</td>\
    <td id='dist'>nan</td>"

    document.querySelector(trId).innerHTML=str
}





function beginSearch() {
    var data = { "start": $("#start").val(), "end": $("#end").val() }
    var algorithmIndex=document.getElementById("algorithm").selectedIndex
    var algorithm=document.querySelectorAll("#algorithm option")[algorithmIndex].value
    var url="/"+algorithm
    console.log(url)
    console.log(trId)
    clearMap(algorithm)

    $.ajax({
        url: url,
        //  dataType:"json",  
        type: "POST",
        async:false,   
        data: data,
        success: function (data) {
            console.log(data)
            var cnt = 0
            //先该结点变色，更新open表，close表，搜索轮数0
            changeSVG(data["openNodeNames"][0], black)
            var row = document.querySelector(trId)
            row.cells["open"].innerHTML = data["openNodeNames"][cnt]
            row.cells["close"].innerHTML = data["expandedNodeNames"][cnt]
            row.cells["cnt"].innerHTML = cnt
            cnt += 1
            setTimeout(iteration, timeInterval)

            function iteration() {
                
                row.cells["open"].innerHTML = data["openNodeNames"][cnt]
                row.cells["close"].innerHTML = data["expandedNodeNames"][cnt]
                row.cells["cnt"].innerHTML = cnt
                

                //描绘画面------------------
                //先填充open表中比之前多的结点
                var plus=[]
                curOpenList=data["openNodeNames"][cnt].split("-")
                lastOpenList=data["openNodeNames"][cnt-1].split("-")

                // console.log(curOpenList)
                for(var i=0;i<curOpenList.length;i++){
                    if(curOpenList[0]==""){
                        break;
                    }
                    var thisNodeName=curOpenList[i];
                    if (lastOpenList.indexOf(thisNodeName)==-1){
                        // console.log(thisNodeName)
                        changeSVG(thisNodeName,black)
                        drawNewLine(data["thisExpand"][cnt],thisNodeName,pathColor)
                    }
                }

                if(cnt==data["expandedNodeNames"].length-1){
                    row.cells["path"].innerHTML=data["rsNodeList"]
                    row.cells["dist"].innerHTML=data["distance"]
                    //画最终结点

                    var rsList=data["rsNodeList"].split("->")
                    rsCnt=0
                    changeSVG(rsList[0],right)
                    setTimeout(iterationRs,rsTimeInterval)

                    function iterationRs(){
                        rsCnt+=1
                        drawNewLine(rsList[rsCnt-1],rsList[rsCnt],rsColor)
                        changeSVG(rsList[rsCnt],right)
                        if(rsCnt<rsList.length-1){
                            setTimeout(iterationRs,rsTimeInterval)
                        }
                    }

                }

                cnt += 1
                if (cnt < data["expandedNodeNames"].length) {
                    //继续循环
                    // console.log("循环内" + cnt)
                    setTimeout(iteration, timeInterval)
                }
            }
        }

    });

    


}
    function drawNewLine(name1,name2,myColor){
        // console.log(name1,"+",name2)
        var lineName=name1+name2
        var line=document.getElementById(lineName)
        
        if(line===null){
             lineName=name2+name1
        }
        // console.log(lineName)
        visitEdge(lineName,myColor)

    }
    function changeSVG(id, style) {
        var element = document.getElementById(id)
        element.innerHTML = style

    }

    function visitEdge(id,myColor) {
        var line = document.getElementById(id)
        line.style["border"] = "2px solid "+myColor
        
    }


