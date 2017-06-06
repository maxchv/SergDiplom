$(function () {
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
                //<span style="cursor: pointer" id="btn-feedback" class="scroll-link" data-toggle="modal" data-target="#dlg-feedback">Мои отзывы</span>
                //<span style="cursor: pointer" id="btn-orders" class="scroll-link" data-toggle="modal" data-target="#dlg-order">Заказать</span>
                $('<li><span data-target="' + menu[i].target + '" data-toggle="modal" style="cursor: pointer" id="' + menu[i].id + '" class="scroll-link">' + menu[i].title + '</span></li>').insertBefore(enter);
            }
            $('<li><a href="/logout/" class="scroll-link new-link">Выход</a></li>').insertBefore(enter);
            enter.remove();
        }
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
                'title':   $('#form-feedback').find("input[name=title]").val(),
                'message': $('#form-feedback').find('textarea[name=message]').val()
            }
        },
        function (data) {
            output = $('#form-feedback').find('.output');
            output.empty();
            output.append($.parseHTML(data.message));
            output.slideDown();
            if (data.status == 'ok') {
                setTimeout(function () {
                    // clean data
                    $('#form-feedback').find('textarea[name=message]').val('');
                    $('#form-feedback').find("input[name=title]").val('');
                    output.empty();
                    $('#form-feedback').modal("hide");
                }, 2000);
            }
        }
    );


    process_form(
        $('#form-order'),
        function () {
            return {
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
            if (data.status == 'ok') {
                setTimeout(function () {
                    // clean data
                    $('#form-order').find("input[name=datetime]").val('');
                    $('#form-order').find("select[name=master]").val('');
                    $('#form-order').modal('hide');
                    output.empty();
                }, 2000);
            }
        }
    );

    // регистрация
    process_form(
        $('#form-register'),
        function () {
            return {
                //'csrfmiddlewaretoken': $('#form-register').find("input[name=csrfmiddlewaretoken]").val(),
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
            if (data.status == 'ok') {
                update_menu(data.menu);
                setTimeout(function () {
                    // clean data
                    $('#form-register').find("input[name=password1]").val('');
                    $('#form-register').find("input[name=password2]").val('');
                    output.empty();
                    $("#dlg-register").modal("hide");
                    $("#dlg-login").modal("show");
                }, 2000);
            }
        }
    );

    process_form(
        $('#form-login'),
        function () {
            return {
                'username': $('#form-login').find("input[name=username]").val(),
                'password': $('#form-login').find("input[name=password]").val()
            }
        },
        function (data) {
            output = $('#form-login').find('.output');
            output.empty();
            output.append($.parseHTML(data.message.replace("__all__", '')));
            output.slideDown();
            if (data.status == 'ok') {
                update_menu(data.menu);
                $("#dlg-login").modal("hide");
                $('#form-login').find("input[name=password]").val('');
            }
        }
    );

    // маски
    $("[type=tel]").mask("(099) 999-99-99");
});