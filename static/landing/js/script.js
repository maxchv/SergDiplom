/**
 * Created by shaptala on 06.02.2017.
 */
$(function () {

    function login_down(time, delay) {
        var time = time || 1200;
        var delay = delay || 0;
        $('#background').delay(delay).fadeIn(time);
        $("#login").show().delay(delay).animate({top: "200px"}, time, function () {
            $("#id_username").focus();
        });
    }

    $("#enter").click(function () {
        // форма входа
        login_down();
    });

    function order_down(time, delay) {
        var time = time || 1200;
        var delay = delay || 0;
        $('#background').delay(delay).fadeIn(time);
        $("#order").show().delay(delay).animate({top: "200px"}, time, function () {
            $("#order").find('input:nth-of-type(2)').focus();
        });
    }

    function btn_orders() {
        $("#btn-orders").click(function () {
            order_down();
        });
    }

    btn_orders();

    function register_down(time) {
        var time = time || 1200;
        $("#login:visible").animate({top: "-300px"}, time, function () {
            $("#login").hide();
            $("#register").show().animate({top: "150px"}, time, function () {
                $("#id_username").focus();
            });
        });
    }

    // форма регистрации
    $("#btn-form-register").click(function () {
        register_down();
    });

    function login_up(time) {
        var time = time || 1200;
        $("#login:visible").animate({top: "-300px"}, time, function () {
            $("#login").hide();
        });
    }

    function register_up(time) {
        var time = time || 1200;
        $("#register:visible").animate({top: "-500px"}, time, function () {
            $("#register").hide();
        });
    }

    function order_up(time) {
        var time = time || 1200;
        $("#order:visible").animate({top: "-500px"}, time, function () {
            $("#order").hide();
        });
    }

    // клик по фону
    $("#background").click(function () {
        $(this).fadeOut(1200);
        login_up();
        register_up();
        order_up();
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

    function form_up(form, time, top) {
        var time = time || 1200;
        var top = top || '-500px';
        form.animate({top: top}, time, function () {
            form.hide();
        });
    }

    function process_form(form, data, callback) {
        form.submit(function (e) {
            e.preventDefault();
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
        {
            'csrfmiddlewaretoken': $('#form-feedback').find("input[name=csrfmiddlewaretoken]").val(),
            'title': $('#form-feedback').find("input[name=title]").val(),
            'message': $('#form-feedback').find('textarea[name=message]').val()
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

    //
    //
    // $("#form-feedback").submit(function (e) {
    //     e.preventDefault();
    //     var self = $(this);
    //     var data = {
    //         'title': self.find("input[name=titl]").val(),
    //         'message': self.find('textarea[name=message]').val()
    //     };
    //     console.log(data);
    //     var url = self.attr('action');
    //     $.ajax({
    //             beforeSend: function (xhr, settings) {
    //                 if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
    //                     xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    //                 }
    //             },
    //             method: 'POST',
    //             url: url,
    //             data: data,
    //             success: function (data) {
    //                 console.dir(data);
    //                 if (data.status == 'ok') {
    //                     feedback_up();
    //                     $("#background").fadeOut(1200);
    //                 }
    //                 else if (data.status == 'error') {
    //                     console.log(typeof data.message);
    //                     output = self.find('.form-errors');
    //                     output.append($.parseHTML(data.message));
    //                     output.slideDown();
    //                 }
    //             },
    //             error: function (xhr, str) {
    //                 console.log("error: " + xhr.responseCode)
    //             }
    //         }
    //     );
    // });

    process_form(
        $('#form-order'),
        {
            'csrfmiddlewaretoken': $('#form-order').find("input[name=csrfmiddlewaretoken]").val(),
            'datetime': $('#form-order').find("input[name=datetime]").val(),
            'phone': $('#form-order').find("input[name=phone]").val(),
            'master': $('#form-order').find("select[name=master]").val()
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

    // $("#form-order").submit(function (e) {
    //     e.preventDefault();
    //     var self = $(this);
    //     var data = {
    //         'datetime': self.find("input[name=datetime]").val(),
    //         'phone': self.find("input[name=phone]").val(),
    //         'master': self.find("select[name=master]").val()
    //     };
    //     var url = self.attr('action');
    //     $.ajax({
    //             beforeSend: function (xhr, settings) {
    //                 if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
    //                     xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    //                 }
    //             },
    //             method: 'POST',
    //             url: url,
    //             data: data,
    //             success: function (data) {
    //                 console.dir(data);
    //                 if (data.status == 'ok') {
    //                     order_up();
    //                     $("#background").fadeOut(1200);
    //                 }
    //                 else if (data.status == 'error') {
    //                     console.dir(data);
    //                     //var msg = data.message['0']['0'];
    //                     //console.log(msg);
    //                     //     if (data.message) {
    //                     //         var output = login.find(".form-errors");
    //                     //         output.text(msg.message);
    //                     //         $('#login').animate({height: "280px"});
    //                     //         output.slideDown();
    //                     //         login.find("input[name=username]").focus();
    //                     //         login.find("input[name=username]").select();
    //                     //     }
    //                 }
    //             },
    //             error: function (xhr, str) {
    //                 console.log("error: " + xhr.responseCode)
    //             }
    //         }
    //     );
    // });

    // регистрация
    $("#form-register").submit(function (e) {
        e.preventDefault();
        var self = $(this);
        var data = {
            'username': self.find("input[name=username]").val(),
            'password1': self.find("input[name=password1]").val(),
            'password2': self.find("input[name=password2]").val()
        };
        var url = $('#form-register').attr('action');
        $.ajax({
                beforeSend: function (xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                    }
                },
                method: 'POST',
                url: url,
                data: data,
                success: function (data) {
                    console.dir(data);
                    if (data.status == 'ok') {
                        //update_menu(data.menu);
                        register_up();
                        login_down(1200, 1000);
                        //$("#background").fadeOut(1200);
                    }
                    //else if (data.status == 'error') {
                    //     var msg = data.message['0']['0'];
                    //     console.log(msg);
                    //     if (data.message) {
                    //         var output = login.find(".form-errors");
                    //         output.text(msg.message);
                    //         $('#login').animate({height: "280px"});
                    //         output.slideDown();
                    //         login.find("input[name=username]").focus();
                    //         login.find("input[name=username]").select();
                    //     }
                    // }
                },
                error: function (xhr, str) {
                    console.log("error: " + xhr.responseCode)
                }
            }
        );
    });

    // аутентификация
    $("#form-login").submit(function (e) {
        e.preventDefault();
        var login = $(this);
        var data = {
            'username': login.find("input[name=username]").val(),
            'password': login.find("input[name=password]").val()
        };
        var url = $('#form-login').attr('action');
        console.log('url: ' + url);
        $.ajax({
                beforeSend: function (xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                    }
                },
                method: 'POST',
                url: url,
                data: data,
                success: function (data) {
                    console.dir(data);
                    if (data.status == 'ok') {
                        update_menu(data.menu);
                        login_up();
                        $("#background").fadeOut(1200);
                        // setTimeout(function () {
                        //     window.location = window.location;
                        // }, 1200);
                    } else if (data.status == 'error') {
                        var msg = data.message['0']['0'];
                        console.log(msg);
                        if (data.message) {
                            var form_errors = login.find(".form-errors");
                            output.text(msg.message);
                            $('#login').animate({height: "280px"});
                            output.slideDown();
                            login.find("input[name=username]").focus();
                            login.find("input[name=username]").select();
                        }
                    }
                },
                error: function (xhr, str) {
                    console.log("error: " + xhr.responseCode)
                }
            }
        );
    });

    // маски
    $("[type=tel]").mask("(099) 999-99-99");
});