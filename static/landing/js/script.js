/**
 * Created by shaptala on 06.02.2017.
 */
$(function () {
    $("#enter").click(function () {
        // форма входа
        $("#login").show();
        $('#background').fadeIn(1200);
        $("#login").animate({top: "200px"}, 1200, function () {
            $("#id_username").focus();
        });
    });

    function login_up() {
        $("#login:visible").animate({top: "-300px"}, 1200, function () {
            $("#login").hide();
        });
    }

    // форма регистрации
    $("#btn-register").click(function () {
        login_up();
         $("#register").delay(1000).animate({top: "200px"}, 1200, function () {
            $("#id_username").focus();
        });
    });

    $("#background").click(function () {
        $(this).fadeOut(1200);
        login_up();
        $("#register:visible").animate({top: "-300px"}, 1200, function () {
            $("#register").hide();
        });
    });
});