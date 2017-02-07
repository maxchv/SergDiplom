/**
 * Created by shaptala on 06.02.2017.
 */
$(function () {
    $("#enter").click(function () {
        // alert("hello");
        $("#login").show();
        $('#background').fadeIn(1200);
        $("#login").animate({top: "200px"}, 1200, function () {
            $("#id_username").focus();
        });
    });

    $("#background").click(function () {
        $(this).fadeOut(1200);
        $("#login").animate({top: "-300px"}, 1200, function () {
            $("#login").hide();
        });
    });
});