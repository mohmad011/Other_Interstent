<?php

	function lang($phrase) {

		$lang = array(

			// Navbar Links

			'HOME_ADMIN' 	=> 'HOME',
			'CATEGORIES'   	=> 'Categories',
			'ITEMS' 		=>	'Items',
			'MEMBERS'		=> 'Members',
			'STATISTICS' 	=> 'Statistics',
			'LOGS' 			=> 'Logs',
			'' => '',
			'' => '',
			'' => '',
			'' => '',
			'' => '',
		);

		return $lang[$phrase];
	}