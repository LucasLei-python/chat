if(window.XMLHttpRequest){
    //当前浏览器支持XMLHttpRequest
    //通过XMLHttpRequest()创建xhr对象
    var xhr = new XMLHttpRequest();
}else{
    var xhr = new ActiveXObject("Microsoft.XMLHTTP");
}