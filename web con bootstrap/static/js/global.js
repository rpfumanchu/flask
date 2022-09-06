$(document).ready(function(){
    console.log("Hola que tal 1")

    $("#toggle_spinner").click(function() {
        $("#spinner_chachi").toggle();
        document.body.append($("<div>"))
    })
})

$(function() {
    console.log("Hola que tal 2")
})