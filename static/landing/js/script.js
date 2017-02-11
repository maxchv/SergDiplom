/**
 * Created by shaptala on 06.02.2017.
 */
$(function () {
    $("#enter").click(function () {
        // форма входа
        $('#background').fadeIn(1200);
        $("#login").show().animate({top: "200px"}, 1200, function () {
            $("#id_username").focus();
        });
    });

    // форма регистрации
    $("#btn-register").click(function () {
        $("#login:visible").animate({top: "-300px"}, 1200, function () {
            $("#login").hide();
            $("#register").show().animate({top: "150px"}, 1200, function () {
                $("#id_username").focus();
            });
        });

    });

    function login_up() {
        $("#login:visible").animate({top: "-300px"}, 1200, function () {
            $("#login").hide();
        });
    }

    $("#background").click(function () {
        $(this).fadeOut(1200);
        login_up();
        $("#register:visible").animate({top: "-500px"}, 1200, function () {
            $("#register").hide();
        });
    });

    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function update_menu(menu) {
        console.dir(menu);
        var mainNav = $("#mainNav");
        mainNav.find("li:last-child").remove();
        for (var i = 0; i < menu.length; i++) {
            mainNav.append('<li><a href="' + menu[i].link + '" class="scroll-link">' + menu[i].title + '</a></li>');
        }
        mainNav.append('<li><a href="/logout/" class="scroll-link new-link">Выход</a></li>');
    }

    $("#form-login").submit(function (e) {
        e.preventDefault();
        var login = $("#login");
        var data = {
            'username': login.find("input[name=username]").val(),
            'password': login.find("input[name=password]").val()
        };
        $.ajax({
                beforeSend: function (xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                    }
                },
                method: 'POST',
                url: '/login_ajax/',
                data: data,
                success: function (data) {
                    console.dir(data);
                    if (data.status == 'ok') {
                        update_menu(data.menu);
                        login_up();
                        $("#background").fadeOut(1200);
                    } else if(data.status == 'error') {
                        var msg = data.message['0']['0'];
                        console.log(msg);
                        if(data.message) {
                            var form_errors = $("#form-login").find(".form-errors");
                            form_errors.text(msg.message);
                            login.animate({height: "280px"});
                            form_errors.slideDown();
                            login.find("input[name=username]").focus();
                            login.find("input[name=username]").select();
                        }
                    }
                },
                error: function (xhr, str) {
                    console.log("error: " + xhr.responseCode)
                }
            }
        )
    });
});