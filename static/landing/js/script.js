$(function () {
    $("#enter").click(function () {
        // форма входа
        form_down($("#login"));
    });

    function btn_orders() {
        $("#btn-orders").click(function () {
            //order_down();
            form_down($("#order"));
        });
    }

    btn_orders();

    // форма регистрации
    $("#btn-form-register").click(function () {
        //register_down();
        form_up($("#login"));
        form_down($("#register"), 1200, 700);
    });

    // клик по фону
    $("#background").click(function () {
        $(this).fadeOut(1200);
        //login_up();
        form_up($('#login'));
        //register_up();
        form_up($('#register'));
        //order_up();
        form_up($('#order'));
        form_up($('#feedback'));
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
        if (menu) {
            var mainNav = $("#mainNav");
            var enter = mainNav.find("#enter").parent();
            for (var i = 0; i < menu.length; i++) {
                // <span style="cursor: pointer" id="btn-orders" class="scroll-link">Мои заказы</span>
                $('<li><span data-link="' + menu[i].link + '" style="cursor: pointer" id="' + menu[i].id + '" class="scroll-link">' + menu[i].title + '</a></li>').insertBefore(enter);
            }
            $('<li><a href="/logout/" class="scroll-link new-link">Выход</a></li>').insertBefore(enter);
            enter.remove();
            btn_orders();
            btn_panel_admin();
        }
    }

    function btn_panel_admin() {
        $("#btn-admin-panel").click(function () {
            window.location = $(this).attr('data-link');
        });
    }

    btn_panel_admin();

    function form_down(form, time, delay, top) {
        var time = time || 1200;
        var delay = delay || 0;
        var top = top || "200px";
        $('#background').delay(delay).fadeIn(time);
        form.show().delay(delay).animate({top: top}, time, function () {
            form.find('input:nth-of-type(2)').focus();
        });
    }

    function btn_feedback() {
        $("#btn-feedback").click(function () {
            form_down($("#feedback"));
        });
    }

    btn_feedback();

    function form_up(form, time, top, delay) {
        var time = time || 1200;
        var top = top || '-500px';
        var delay = delay || 0;
        form.delay(delay).animate({top: top}, time, function () {
            form.hide();
        });
    }

    function process_form(form, get_data, callback) {
        form.submit(function (e) {
            e.preventDefault();
            var data = get_data();
            console.log(data);
            var url = form.attr('action');
            $.ajax({
                    beforeSend: function (xhr, settings) {
                        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                        }
                    },
                    method: 'POST',
                    url: url,
                    data: data,
                    success: callback,
                    error: function (xhr, str) {
                        console.log("error: " + xhr.responseCode)
                    }
                }
            );
        });
    }

    process_form(
        $('#form-feedback'),
        function () {
            return {
                'csrfmiddlewaretoken': $('#form-feedback').find("input[name=csrfmiddlewaretoken]").val(),
                'title': $('#form-feedback').find("input[name=title]").val(),
                'message': $('#form-feedback').find('textarea[name=message]').val()
            }
        },
        function (data) {
            output = $('#form-feedback').find('.output');
            output.empty();
            output.append($.parseHTML(data.message));
            output.slideDown();
            $('#feedback').animate({'height': '400px'});
            if (data.status == 'ok') {
                setTimeout(function () {
                    form_up($('#feedback'));
                    $("#background").fadeOut(1200);
                    // clean data
                    $('#form-feedback').find('textarea[name=message]').val('');
                    $('#form-feedback').find("input[name=title]").val('');
                    output.empty();
                    $('#feedback').css({'height': '350px'});
                }, 2000);
            }
        }
    );


    process_form(
        $('#form-order'),
        function () {
            return {
                'csrfmiddlewaretoken': $('#form-order').find("input[name=csrfmiddlewaretoken]").val(),
                'datetime': $('#form-order').find("input[name=datetime]").val(),
                'phone': $('#form-order').find("input[name=phone]").val(),
                'master': $('#form-order').find("select[name=master]").val()
            }
        },
        function (data) {
            output = $('#form-order').find('.output');
            output.empty();
            output.append($.parseHTML(data.message));
            output.slideDown();
            $('#order').animate({'height': '360px'});
            if (data.status == 'ok') {
                setTimeout(function () {
                    form_up($('#order'));
                    $("#background").fadeOut(1200);
                    // clean data
                    $('#form-order').find("input[name=datetime]").val('');
                    $('#form-order').find("select[name=master]").val('');
                    output.empty();
                    $('#order').css({'height': '320px'});
                }, 2000);
            }
        }
    );

    // регистрация
    process_form(
        $('#form-register'),
        function () {
            return {
                'csrfmiddlewaretoken': $('#form-register').find("input[name=csrfmiddlewaretoken]").val(),
                'username': $('#form-register').find("input[name=username]").val(),
                'password1': $('#form-register').find("input[name=password1]").val(),
                'password2': $('#form-register').find("input[name=password1]").val(),
            }
        },
        function (data) {
            output = $('#form-register').find('.output');
            output.empty();
            output.append($.parseHTML(data.message.replace("__all__", '')));
            output.slideDown();
            $('#register').animate({'height': '460px'});
            if (data.status == 'ok') {
                update_menu(data.menu);
                setTimeout(function () {
                    form_up($('#register'));
                    // clean data
                    $('#form-register').find("input[name=password1]").val('');
                    $('#form-register').find("input[name=password2]").val('');
                    output.empty();
                    $('#register').css({'height': '400px'});
                    form_down($('#login'), 1200, 700);
                }, 2000);
            }
        }
    );

    process_form(
        $('#form-login'),
        function () {
            return {
                'csrfmiddlewaretoken': $('#form-login').find("input[name=csrfmiddlewaretoken]").val(),
                'username': $('#form-login').find("input[name=username]").val(),
                'password': $('#form-login').find("input[name=password]").val()
            }
        },
        function (data) {
            output = $('#form-login').find('.output');
            output.empty();
            output.append($.parseHTML(data.message.replace("__all__", '')));
            output.slideDown();
            $('#login').animate({'height': '295px'});
            if (data.status == 'ok') {
                update_menu(data.menu);
                setTimeout(function () {
                    form_up($('#login'));
                    $("#background").fadeOut(1200);
                    // clean data
                    $('#form-login').find("input[name=password]").val('');
                    output.empty();
                    $('#login').css({'height': '250px'});
                }, 2000);
            }
        }
    );

    // маски
    $("[type=tel]").mask("(099) 999-99-99");
});