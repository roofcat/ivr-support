'use strict';

var baseUrl = document.location.href;
// urls busquedas
var queryUrl = '/search/';

// urls exportar reportes
var exportUrl = '/export/';

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

	drawJTables( link );	
	$( '#closeLoadingModal' ).click();

	exportLink = baseUrl + exportUrl + date_from + '/' + date_to + '/';
	$( '#btnGenerateReport' ).show();

});

$( '#btnGenerateReport' ).on( 'click', function () {
	var btn = $( this );
	btn.attr( 'disabled', true );
	sendUrlToReportTask( exportLink, btn );
	var title = "Reporte llamadas";
	var body = "Se ha iniciado el proceso para generar tu reporte Excel ";
	body += "cuando este proceso finalice recibirás un email con el archivo ";
	body += "adjunto, por favor espere unos minutos...";
	notificationModal( title, body );

});

$( '#showMenu' ).on( 'click', function () {
	$( '#menuModal' ).modal( 'show', true );
});

function sendUrlToReportTask ( link, btn ) {
	$.ajax({
		url: link,
		type: 'GET',
	})
	.done(function( data ) {
		btn.attr('disabled', false );
		console.log( data );
	})
	.fail(function( jqXHR, textStatus, errorThrown ) {
		btn.attr('disabled', false );
		console.log( errorThrown );
	});
};

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
		    	'data': 'timeStamp',
		    	'title': 'Fecha',
		    	'render': function ( data, type, row, meta ) {
					return ( !data ) ? "" : moment( data ).format( 'DD-MM-YYYY H:mm:ss' );
				},
		    },
		    {
		    	'data': 'beginCall',
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
		    	'data': 'callAnswered',
		    	'title': 'Contestó IVR',
		    	'render': function ( data, type, row, meta ) {
					var html = '';
					if ( data ) {
						html = '<div align="center"><span class="glyphicon glyphicon-ok"></span></div>';
					} else {
						html = '<div align="center"><span class="glyphicon glyphicon-remove"></span></div>';
					};
					return html;
				},
		    },
		    {
		    	'data': 'IVRSel',
		    	'title': 'Nº Anexo',
		    },
		    {
		    	'data': 'dialIntentBegin1',
		    	'title': 'Fecha Inicio',
		    	'render': function ( data, type, row, meta ) {
					return ( !data ) ? "" : moment( data ).format( 'DD-MM-YYYY H:mm:ss' );
				},
		    },
		    {
		    	'data': 'dialIntentCaller1',
		    	'title': 'Nº que llama',
		    },
		    {
		    	'data': 'dialIntentCalled1',
		    	'title': 'Nº donde se transfiere',
		    },
		    {
		    	'data': 'dialIntentEnd1',
		    	'title': 'Fecha término',
		    	'render': function ( data, type, row, meta ) {
					return ( !data ) ? "" : moment( data ).format( 'DD-MM-YYYY H:mm:ss' );
				},
		    },
		    {
		    	'data': 'dialIntentAnswered1',
		    	'title': 'Transferencia contestada',
		    	'render': function ( data, type, row, meta ) {
					var html = '';
					if ( data ) {
						html = '<div align="center"><span class="glyphicon glyphicon-ok"></span></div>';
					} else {
						html = '<div align="center"><span class="glyphicon glyphicon-remove"></span></div>';
					};
					return html;
				},
		    },
		    {
		    	'data': 'endDial',
		    	'title': 'Término llamada',
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

	html += '<label>Fecha registro:</label> ' + date_to_format( data.timeStamp ) + ' <br>';
	html += '<label>Inicio de llamada:</label> ' + date_to_format( data.beginCall ) + ' <br>';
	html += '<label>Nº que llama:</label> ' + data.origin + ' - ';
	html += '<label>Nº Anexo:</label> ';

	if ( data.IVRSel ) {
		html += data.IVRSel + ' <br>';
	} else {
		' ' + ' <br>';
	};

	html += '<label>Llamada respondida:</label> ';
	
	if ( data.callAnswered === true ) {
		html += '<span class="glyphicon glyphicon-ok"></span>';
	} else {
		html+= '<span class="glyphicon glyphicon-remove"></span>';
	};

	html += ' - ';
	html += '<label>Último estado IVR:</label> ' + data.lastState + ' <br>';
	html += '<label>Fecha de inicio de llamada de transferencia:</label> ';
	
	if ( data.dialIntentBegin1 ) {
		html +=  date_to_format( data.dialIntentBegin1 ) + ' <br>';
	} else {
		html += ' <br>';
	};

	html += '<label>Número que llama:</label> ';

	if ( data.dialIntentCaller1 ) {
		html += data.dialIntentCaller1 + ' <br>';
	} else {
		html += ' <br>';
	};
	html += '<label>Número a donde se transfiere la llamada:</label> ';

	if ( data.dialIntentCalled1 ) {
		html += data.dialIntentCalled1 + ' <br>';
	} else {
		html += ' <br>';
	};

	html += '<label>Término de la llamada de transferencia:</label> ';

	if ( data.dialIntentEnd1 ) {
		html += data.dialIntentEnd1 + ' <br>';
	} else {
		html += ' <br>';
	};

	html += '<label>Transferencia contestada:</label> ';
	
	if ( data.dialIntentAnswered1 === true ) {
		html += '<span class="glyphicon glyphicon-ok"></span>';
	} else {
		html+= '<span class="glyphicon glyphicon-remove"></span>';
	};
	
	html += ' <br>';
	html += '<label>Código de término de llamada:</label> ' + data.hc + ' <br>';
	html += '<label>Fecha término de llamada:</label> ' + date_to_format( data.endDial ) + ' <br>';
	html += ' ';
	html += '</div>';

	notificationModal( title, html );
	$( '#closeLoadingModal' ).click();
};