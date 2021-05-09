<?php
	
	include '../connect/connect.php';

	// Routes
	
	$temp = '../include/template/'; // Template Director
	$css = '../layout/css/'; // CSS Directory
	$js = '../layout/js/'; // js Directory
	$lang = '../include/language/'; // language Director
	$func = '../include/function/'; // Function Director

	// Include The Imporant Files
	include $func . 'Title/func_title.php';
	include $func . 'Color/func_color.php';
	include $func . 'Redirect/redirect.php';
	include $lang . 'english/english.php';
	include $temp . 'header/header.php';

	// Include NavBar On All Pages Expact The One With $noNavebar Variable

	if (!isset($noNavebar)) { include '../include/template/navbar/navbar.php'; }