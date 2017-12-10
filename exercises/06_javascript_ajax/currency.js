$(document).ready(
    function(){
        $("#form").submit(
            function(e){
                e.preventDefault();
                $("#currencies").empty();
                jQuery.getJSON("http://api.fixer.io/"+$("#date").val()+"?callback=?",function(data){
                    for(x in data.rates)
                        $("#currencies").append("<tr>"+"<td>"+x+"</td>"+"<td>"+data.rates[x]+"</td>"+"</tr>");
                });

            });
    })