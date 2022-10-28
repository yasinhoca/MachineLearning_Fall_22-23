document.addEventListener('DOMContentLoaded', function () {

    document.getElementById('makeTreeButton').addEventListener('click', async () => {
        document.getElementById("secondPage").style.display = "block";
        document.getElementById("firstPage").style.display = "none";

        var className = document.getElementById('class-select');
        eel.agacOlustur(className.options[className.selectedIndex].text);
    })

    document.getElementById('backFirstPage').addEventListener('click', async () => {
        document.getElementById("secondPage").style.display = "none";
        document.getElementById("firstPage").style.display = "block";
    })


    eel.expose(setLoading); 
    function setLoading(val) {
        loading = val;
        if (val == true) {
            document.getElementById('fileName').innerHTML = 'loading...';
        } else {
            document.getElementById('fileName').innerHTML = '';
        }
    }


    document.getElementById('addFile').addEventListener('click', async () => {
        await eel.file_import();
    })

    eel.expose(getHeadersJS); 
    function getHeadersJS(x) {

        var columns = '';
        var selectItem = '';
        for (let col in x) {
            columns += "<th>" + x[col] + "</th>";
            selectItem += "<option value=" + x[col] + ">" + x[col] + "</option>";
        }

        document.getElementById('tableHead').innerHTML = columns;
        document.getElementById('class-select').innerHTML = selectItem;

    }

    eel.expose(getFirstRowJS); 
    function getFirstRowJS(x) {

        var rows = "<tr>";
        for (let row in x) {
            rows += "<td>" + x[row] + "</td>";

        }
        document.getElementById('tableBody').innerHTML += rows + "</tr>";
    }

    eel.expose(cleanTable);
    function cleanTable() {
        document.getElementById('tableBody').innerHTML = "";
    }

    eel.expose(getTree); 
    function getTree(y) {


        var level = 0;

        var arrStr = y.split(/['']/);

        var dict = [];
        var parentArray = [];

        for (let str in arrStr) {

            var node = true;
            var leaf = false;

            arrStr[str] = arrStr[str].split(' ').join('');

            for (var i = 0; i < arrStr[str].length; i++) {

                if (arrStr[str].charAt(i) == '{') {
                    level++;
                    node = false;
                } else if (arrStr[str].charAt(i) == '}') {
                    level--;
                    node = false;
                    parentArray.pop();
                    console.log(parentArray)
                } else if (arrStr[str].charAt(i) == ',' || arrStr[str].charAt(i) == ':') {
                    node = false;
                }

                console.log(level)
            }

            if (arrStr[str] == ':{') {
                parentArray.push(arrStr[str - 1])
            }

            if (arrStr[str - 1] == ':') {
                leaf = true;

                dict.push({
                    key: arrStr[str],
                    node: 'leaf',
                    level: level + 1,
                    parent: arrStr[str - 2]
                });
            }




            if (node && !leaf) {

                prevNode = Object.keys(dict).pop();

                var prevNodeisLeaf = JSON.stringify(dict[prevNode]?.node);
                var prevNodeParent = JSON.stringify(dict[prevNode]?.parent);

                var parent = arrStr[str - 2];



                console.log('parent: ' + parent + 'prev node parent: ', prevNodeParent)
                console.log('Node name: ' + arrStr[str])

                dict.push({
                    key: arrStr[str],
                    node: 'node',
                    level: level,
                    parent: parentArray.at(-1)
                });
            }


        }




        const $ = go.GraphObject.make;  

        diagram =
            $(go.Diagram, "myDiagramDiv",
                {
                    "toolManager.hoverDelay": 100,  
                    allowCopy: false,
                    layout: 
                        $(go.TreeLayout,
                            { angle: 90, nodeSpacing: 10, layerSpacing: 40, layerStyle: go.TreeLayout.LayerUniform })
                });


        function getColor(node) {
            if (node == "leaf") return "#90eea8";
            if (node == "node") return "#add8e6";
            return "lightgray";
        }

        function setupTree(diagram) {
            diagram.nodeTemplate =
                $(go.Node, "Auto",
                    $(go.Shape, "Rectangle",
                        {
                            fill: "lightgray",
                            stroke: null, strokeWidth: 0,
                            stretch: go.GraphObject.Fill,
                            alignment: go.Spot.Center
                        },
                        new go.Binding("fill", "node", getColor)),
                    $(go.TextBlock,
                        {
                            font: "700 16px Droid Serif, sans-serif",
                            textAlign: "center",
                            margin: 15
                        },
                        new go.Binding("text", "key"))
                );

            diagram.linkTemplate =
                $(go.Link,
                    { routing: go.Link.Orthogonal, corner: 5 },
                    $(go.Shape));


            diagram.model = new go.TreeModel(dict);
        }

        setupTree(diagram);

        document.getElementById('zoomToFit').addEventListener('click', () => myDiagram.commandHandler.zoomToFit());

        document.getElementById('centerRoot').addEventListener('click', () => {
            myDiagram.scale = 1;
            myDiagram.scrollToRect(myDiagram.findNodeForKey(0).actualBounds);
        });


    }




});