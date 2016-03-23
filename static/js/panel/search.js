'use strict';

var baseUrl = document.location.href;

var queryUrl = 'query/';

var exportUrl = 'reports/export/';

var detailUrl = 'detail/';

var attacgUrl = '';

var exportLink = '';

$( document ).ready( function () {

	baseUrl = baseUrl.split( '/' );
	delete baseUrl[5];
	delete baseUrl[4];
	console.log( baseUrl );
	baseUrl = baseUrl.join( '/' );
	baseUrl = baseUrl.substring( 0, baseUrl.length - 1 );
	console.log( baseUrl );

	$( '.datePicker' ).datetimepicker ({
		'dayOfWeekStart': 1,
		'lang': 'es',
		'timepicker': false,
		'format': 'd/m/Y',
		'formatDate': 'Y/m/d',
	});

	setDefaultDates();
	$( '#menuModal' ).modal( 'show', true );

});

function setDefaultDates () {

	$( '#date_from' ).val( moment().subtract( 7, 'days' ).format( 'DD/MM/YYYY' ) );
	$( '#date_to' ).val( moment().format( 'DD/MM/YYYY' ) );

};

function drawJqueryTable ( urlSource ) {
	var table = $( '#tableCards' ).dataTable({
		"ajaxSource": urlSource,
		"destroy": true,
		"lengthChange": false,
		"ordering": false,
		"pageLength": 50,
		"paging": true,
		"processing": true,
		"scrollCollapse": true,
		"scrollX": "100%",
		"scrollY": "450px",
		"searching": false,
		"serverSide": true,
		"columns": [
			{
				'data': 'collection',
				'title': 'collection',

			},
			{
				'data': 'sp',
				'title': 'sp',

			},
			{
				'data': 'key',
				'title': 'key',

			},
			{
				'data': 'begin_call',
				'title': 'begin_call',

			},
			{
				'data': 'origin',
				'title': 'origin',

			},
			{
				'data': 'call_answered',
				'title': 'call_answered',

			},
			{
				'data': 'last_state',
				'title': 'last_state',

			},
			{
				'data': 'ivr_sel',
				'title': 'ivr_sel',

			},
			{
				'data': 'dial_intent_begin',
				'title': 'dial_intent_begin',

			},
			{
				'data': 'dial_intent_caller',
				'title': 'dial_intent_caller',

			},
			{
				'data': 'dial_intent_called',
				'title': 'dial_intent_called',

			},
			{
				'data': 'dial_intent_end',
				'title': 'dial_intent_end',

			},
			{
				'data': 'dial_intent_answered',
				'title': 'dial_intent_answered',

			},
			{
				'data': 'session_file',
				'title': 'session_file',

			},
			{
				'data': 'hc',
				'title': 'hc',

			},
			{
				'data': 'routing',
				'title': 'routing',

			},
			{
				'data': 'name',
				'title': 'name',

			},
			{
				'data': 'end_dial',
				'title': 'end_dial',

			},
			{
				'data': 'timestamp',
				'title': 'timestamp',

			},
		],
		"language": {
			"emptyTable": "No se encontraron registros.",
            "info": "Página _PAGE_ de _PAGES_",
            "infoEmpty": "No se encontraron registros.",
            "infoFiltered": "(Filtrado de _MAX_ registros).",
            "loadingRecords": "Cargando...",
            "paginate": {
            	"previous": "Anterior",
            	"next": "Siguiente",
            },
            "processing": "Proceso en curso.",
            "search": "Buscar",
            "zeroRecords": "No se encontraron registros.",
        },
	});
	table.removeClass('display');
	table.addClass('table table-hover table-striped table-condensed table-responsive');
};
