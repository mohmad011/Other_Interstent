<?php 	

		$pageTitle = 'Dashbourd';
		// $pageColor = '#080';
		session_start();
		if(isset($_SESSION['username'])){	
			include '../init/init.php';



			include $temp . 'footer/footer.php';
			
		}else{
			header('Location: ../index/index.php');

			exit();
		}
		
		

		// session_start();
		// if(isset($_SESSION['username'])){
		// 	// echo "Welcome " . 
		// 	// $_SESSION['username'];
			
		// }else {
		// 	header('Location: ../index/index.php');
		// 	exit();
		// }