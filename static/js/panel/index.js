'use strict';

var baseUrl = document.location.href;
// urls busquedas
var queryUrl = '/search/';

// urls exportar reportes
var exportUrl = 'reports/export/';

// urls para modal detalle de email
var callDetailUrl = 'call-detail/';

// url link storage
var attachUrl = 'https://storage.googleapis.com';

// link dinamico para las rutas de exportar
var exportLink = '';

$( document ).ready( function () {
	baseUrl = baseUrl.split('/');
	delete baseUrl[4];
	//delete baseUrl[3];
	baseUrl = baseUrl.join('/')
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

// Validar los campos de fecha
$( '.datePicker' ).on( 'change', function () {

	var date_from = $( '#date_from' ).val();
	var date_to = $( '#date_to' ).val();

	date_from = moment( date_from, 'DD/MM/YYYY' ).unix();
	date_to = moment( date_to, 'DD/MM/YYYY' ).unix();

	if ( date_from > date_to ) {
		setDefaultDates();
	};
});

function setDefaultDates () {
	$( '#date_from' ).val( moment().subtract( 7, 'days' ).format( 'DD/MM/YYYY' ) );
	$( '#date_to' ).val( moment().format( 'DD/MM/YYYY' ) );
};

$( '#run_search' ).on( 'click', function () {

	$( '#closeMenuModal' ).click();
	$( '#loadingModal' ).modal( 'show', true );

	var date_from = $( '#date_from' ).val();
	var date_to = $( '#date_to' ).val();

	date_from = date_to_timestamp( date_from );
	date_to = date_to_timestamp( date_to );

	var link = baseUrl + queryUrl + date_from + '/' + date_to + '/';

	console.log( link );

	drawJTables( link );

	$( '#closeLoadingModal' ).click();
});

$( '#showMenu' ).on( 'click', function () {
	$( '#menuModal' ).modal( 'show', true );
});

function drawJTables( urlSource ) {
	var table = $( '#tableCall' ).dataTable({
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
				'data': 'pk',
				'title': 'Detalle',
				'render': function ( data, type, row, meta ) {
					if ( data != null ) {
						var html = '';
						html += '<span style="font-size:16px;color:#2196f3;align:center;cursor:pointer;" title="Click para ver más detalle." class="glyphicon glyphicon-info-sign" id="spanDetail" data-pk="' + data + '"></span>';
						return html;
					} else {
						return "";
					};
				},
			},
			{
				'data': 'session_file',
				'title': 'Audio',
				'render': function ( data, type, row, meta ) {
					if ( data ) {
						var html = '<div style="font-size:11px;">';
						html += '<a href="/media/' + data + '" title="Ir al audio" target="_blank"><span class="glyphicon glyphicon-headphones"></span></a>';
						html += '</div>';
						return html;
					} else {
						return "";
					};
				},
			},
			{
				'data': 'timestamp',
				'title': 'Fecha',
				'render': function ( data, type, row, meta ) {
					return ( !data ) ? "" : moment( data ).format( 'DD-MM-YYYY H:mm:ss' );
				},
			},
			{
				'data': 'begin_call',
				'title': 'Inicio llamada',
				'render': function ( data, type, row, meta ) {
					return ( !data ) ? "" : moment( data ).format( 'DD-MM-YYYY H:mm:ss' );
				},
			},
			{
				'data': 'origin',
				'title': 'Nº que llama',
			},
			{
				'data': 'call_answered',
				'title': 'Contestó IVR',
				'render': function ( data, type, row, meta ) {
					var html = '';
					if ( data ) {
						html = '<div align="center"><span class="glyphicon glyphicon-ok"></span></div>';
					} else {
						html = '<div align="center"><span class="glyphicon glyphicon-remove"></span></div>';
					}
					return html;
				},
			},
			{
				'data': 'ivr_sel',
				'title': 'Nº Anexo',
			},
			{
				'data': 'dial_intent_begin',
				'title': 'Fecha inicio',
				'render': function ( data, type, row, meta ) {
					return ( !data ) ? "" : moment( data ).format( 'DD-MM-YYYY H:mm:ss' );
				},
			},
			{
				'data': 'dial_intent_caller',
				'title': 'Nº que llama',
			},
			{
				'data': 'dial_intent_called',
				'title': 'Nº donde se transfiere',
			},
			{
				'data': 'dial_intent_end',
				'title': 'Fecha término',
				'render': function ( data, type, row, meta ) {
					return ( !data ) ? "" : moment( data ).format( 'DD-MM-YYYY H:mm:ss' );
				},
			},
			{
				'data': 'dial_intent_answered',
				'title': 'Transferencia contestada',
				'render': function ( data, type, row, meta ) {
					var html = '';
					if ( data ) {
						html = '<div align="center"><span class="glyphicon glyphicon-ok"></span></div>';
					} else {
						html = '<div align="center"><span class="glyphicon glyphicon-remove"></span></div>';
					}
					return html;
				},
			},
			{
				'data': 'end_dial',
				'title': 'Término de llamada',
				'render': function ( data, type, row, meta ) {
					return ( !data ) ? "" : moment( data ).format( 'DD-MM-YYYY H:mm:ss' );
				},
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
	table.removeClass( 'display' );
	table.addClass( 'table table-hover table-striped table-condensed table-responsive' );
};

/*
* Detalle de Llamada
*/
$( '#tableCall' ).on( 'click', 'td', function () {
	var span = $( this ).find( "#spanDetail" );
	var pk = span.data( "pk" );
	if ( pk ) {
		$( '#loadingModal' ).modal( 'show', true );
		getRowDetail( pk );
	};
});

function getRowDetail ( pk ) {
	$.ajax({
		url: callDetailUrl,
		type: 'GET',
		dataType: 'json',
		data: {
			'pk': pk,
		},
	})
	.done( function ( data ) {
		drawCallDetailModal( data ); 
	})
	.fail( function ( jqXHR, textStatus, errorThrown ) {
		console.log( errorThrown );
	});
	
};

function drawCallDetailModal ( data ) {
	var title = 'Detalle de llamada';
	var html = '<div style="font-size: 12px;"><br>';

	html += '<label>Fecha registro:</label> ' + date_to_format( data.timestamp ) + ' <br>';
	html += '<label>Inicio de llamada:</label> ' + date_to_format( data.begin_call ) + ' <br>';
	html += '<label>Nº que llama:</label> ' + data.origin + ' - ';
	html += '<label>Nº Anexo:</label> ' + data.ivr_sel + ' <br>';
	html += '<label>Llamada respondida:</label> ';
	if ( data.call_answered === true ) {
		html += '<span class="glyphicon glyphicon-ok"></span>';
	} else {
		html+= '<span class="glyphicon glyphicon-remove"></span>';
	};
	html += ' - ';
	html += '<label>Último estado IVR:</label> ' + data.last_state + ' <br>';
	html += '<label>Fecha de inicio de llamada de transferencia:</label> ' + date_to_format( data.dial_intent_begin ) + ' <br>';
	html += '<label>Número que llama:</label> ' + data.dial_intent_caller + ' <br>';
	html += '<label>Número a donde se transfiere la llamada:</label> ' + data.dial_intent_called + ' <br>';
	html += '<label>Término de la llamada de transferencia:</label> ' + data.dial_intent_end + ' <br>';
	html += '<label>Transferencia contestada:</label> ';
	if ( data.dial_intent_answered === true ) {
		html += '<span class="glyphicon glyphicon-ok"></span>';
	} else {
		html+= '<span class="glyphicon glyphicon-remove"></span>';
	};
	html += ' <br>';
	html += '<label>Archivo de audio:</label> ';
	if ( data.session_file ) {
		html += '<audio controls>';
		html += '<source src="' + data.session_file + '">';
		html += '</audio>';
	} else {
		html += 'Sin archivo de audio.';
	};
	html += ' <br>';
	html += '<label>Código de término de llamada:</label> ' + data.hc + ' <br>';
	html += '<label>Fecha término de llamada:</label> ' + date_to_format( data.end_dial ) + ' <br>';
	html += ' ';
	html += '</div>';

	notificationModal( title, html );
	$( '#closeLoadingModal' ).click();
};