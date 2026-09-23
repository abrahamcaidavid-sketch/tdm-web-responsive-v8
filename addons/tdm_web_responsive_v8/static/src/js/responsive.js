/* Copyright 2026 TDM - LGPL-3.0-or-later */
openerp.tdm_web_responsive_v8 = function (instance) {
    'use strict';

    var MOBILE_MAX_WIDTH = 991;
    var $document = $(document);
    var $window = $(window);

    function is_mobile() {
        return $window.width() <= MOBILE_MAX_WIDTH;
    }

    function set_menu_state(open) {
        $('body').toggleClass('tdm_mobile_menu_open', open);
        $('.tdm_mobile_sidebar_toggle')
            .attr('aria-expanded', open ? 'true' : 'false')
            .attr('title', open ? '关闭功能菜单' : '打开功能菜单');
    }

    function ensure_mobile_controls() {
        var $header = $('#oe_main_menu_navbar .navbar-header');
        var $container = $('.openerp_webclient_container');

        if ($header.length && !$('.tdm_mobile_sidebar_toggle').length) {
            $('<button/>', {
                'type': 'button',
                'class': 'tdm_mobile_sidebar_toggle',
                'aria-label': '打开功能菜单',
                'aria-expanded': 'false',
                'title': '打开功能菜单'
            })
                .append($('<span/>', {'class': 'fa fa-bars'}))
                .append($('<span/>', {
                    'class': 'tdm_mobile_sidebar_text',
                    'text': '功能'
                }))
                .appendTo($header);
        }

        if ($container.length && !$('.tdm_mobile_menu_backdrop').length) {
            $('<div/>', {
                'class': 'tdm_mobile_menu_backdrop',
                'aria-hidden': 'true'
            }).insertAfter($container);
        }
    }

    function refresh_mobile_ui() {
        ensure_mobile_controls();
        $('body').toggleClass('tdm_mobile_view', is_mobile());
        if (!is_mobile()) {
            set_menu_state(false);
        }
    }

    $document.on('click', '.tdm_mobile_sidebar_toggle', function (event) {
        event.preventDefault();
        event.stopPropagation();
        set_menu_state(!$('body').hasClass('tdm_mobile_menu_open'));
    });

    $document.on('click', '.tdm_mobile_menu_backdrop', function () {
        set_menu_state(false);
    });

    $document.on('click', '.oe_leftbar a.oe_menu_leaf', function () {
        if (is_mobile()) {
            set_menu_state(false);
        }
    });

    $document.on('click', '#oe_main_menu_placeholder a.oe_menu_toggler, ' +
        '#oe_main_menu_placeholder a.oe_menu_leaf', function () {
        if (is_mobile()) {
            window.setTimeout(function () {
                set_menu_state(true);
                $('#oe_main_menu_navbar .navbar-collapse').collapse('hide');
            }, 0);
        }
    });

    $document.on('keydown', function (event) {
        if (event.which === 27) {
            set_menu_state(false);
        }
    });

    $window.on('resize.tdm_web_responsive_v8', refresh_mobile_ui);

    $(function () {
        refresh_mobile_ui();
    });
};

