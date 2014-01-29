$(function () {
    var url = "_" + $(".active").id + ".html";
    $.ajax({
        url: url,
        cache: false
    }).done(function(html) {
        $("#table").append(html);
    });
});