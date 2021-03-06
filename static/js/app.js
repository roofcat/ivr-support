'use strict';

$.material.init();

function getCookie(name) {
    var cookieValue = null;
    if ( document.cookie && document.cookie != '' ) {
        var cookies = document.cookie.split(';');
        for ( var i = 0; i < cookies.length; i++ ) {
            var cookie = jQuery.trim( cookies[i] );
            // Does this cookie string begin with the name we want?
            if ( cookie.substring( 0, name.length + 1 ) == (name + '=') ) {
                cookieValue = decodeURIComponent( cookie.substring( name.length + 1 ) );
                break;
            };
        };
    };
    return cookieValue;
};

function notificationModal ( t, b ) {
    var title = $( '#notificationTitle' );
    var body = $( '#notificationBody' );
    title.empty().append( t );
    body.empty().append( b );
    $( '#notificationModal' ).modal( 'show', true );
};

function timestamp_to_date ( date ) {
    return moment.unix( date ).format( 'DD-MM-YYYY h:mm:ss a' );
};

function date_to_timestamp ( date, max ) {
    return moment( date, 'DD/MM/YYYY' ).unix();
};

function date_to_format ( date ) {
    return moment( date ).format( 'DD-MM-YYYY H:mm:ss a' );
};
