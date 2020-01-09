if(window.XMLHttpRequest){
    //当前浏览器支持XMLHttpRequest
    //通过XMLHttpRequest()创建xhr对象
    var xhr = new XMLHttpRequest();
}else{
    var xhr = new ActiveXObject("Microsoft.XMLHTTP");
}

function convert_FormData_to_json (formData) {
    var objData = {};
    for (var entry of formData.entries()){objData[entry[0]] = entry[1];}
    return JSON.stringify(objData);};

function convert_objData_to_json (htobj) {
    var objData = {};    
    $.each(htobj,function(i,obj){        
        objData[obj.name]=obj.value;

    })
    return objData};