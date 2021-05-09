<?php 	
		session_start();
		$noNavebar = '';
		$pageTitle = 'Login';
		// $pageColor = '#335';
		if(isset($_SESSION['username'])){
			header('Location: ../dashbourd/dashbourd.php');
		}
		
		$init = '../init/init.php';
		include $init;


		// Check If User Coming From HTTP Request

		if($_SERVER['REQUEST_METHOD'] == 'POST'){
			$username = $_POST['user'];
			$password = $_POST['pass'];
			$hashedPass = sha1($password);

			// Check If The User Exist In Database

			$stmt = $connect->prepare('SELECT 
											UserID, Username, Password 
									   FROM 
									   		user 
									   WHERE 
									   		Username = ? 
									   AND 
									   		Password = ? 
									   AND 
											GroupID = 1
									   LIMIT 1');
			$stmt->execute(array($username, $hashedPass));
			$row = $stmt->fetch();
			$count = $stmt->rowCount();

			// If Count > 0 This mean The Database Contain About This Username

			if($count > 0){
				 $_SESSION['username'] = $username; // Register Session Name
				 $_SESSION['ID'] = $row['UserID']; // Register Session ID
				 header('Location: ../dashbourd/dashbourd.php'); // Redirect To Dashbourd Page
				 exit();
			}

		}

?>
	<form class="login" action="<?php echo $_SERVER['PHP_SELF'] ?>" method="POST">
		<h4 class="text-center">Admin Login</h4>
		<input class="form-control" type="username" name="user" placeholder="Username" autocomplete="off">
		<input class="form-control" type="password" name="pass" placeholder="Password" autocomplete="new-password">
		<input class="btn btn-primary btn-block input-lg" type="submit" value="Login">
	</form>

<?php include $temp . 'footer/footer.php'; ?>