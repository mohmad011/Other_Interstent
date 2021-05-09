/*global,$*/

$(function (){

	'use strict';

	// Hide Placeholder On Form Focus

	$('[placeholder]').focus(function (){

		$(this).attr('data-text', $(this).attr('placeholder'));

		$(this).attr('placeholder', '');

		}).blur(function(){

			$(this).attr('placeholder' , $(this).attr('data-text'));

		});
	// Add Asterisk On Required Field

	'use strict';
	
	$('input').each(function(){
		if($(this).attr('required') === 'required'){
			$(this).after('<span class="asterisk">*</span>');
		}
	});

	// Convert Password Feild To Text Feild On Hover

		'use strict';

		var passfeild = $('.password');
	
		$('.show-pass').hover(function(){

			passfeild.attr('type' , 'text');

		}, function (){
			passfeild.attr('type' , 'password');
		});
	// Conformation Message On Button

	$('.confirm').click(function (){
		return confirm('Are Yor Sure To Deleted ?');
	});
});