<?php 	

        /**
         * Manage Members Page
         * You Can Add | Edit | Delete Members From Here
         */

		$pageTitle = 'Members';
		// $pageColor = '#080';
		session_start();
		if(isset($_SESSION['username'])){	
            include '../init/init.php';
            
            $do = isset($_GET['do']) ? $_GET['do'] : 'Manage';

            // Start Manage Page

            if($do == 'Manage') { // Manage Page 
            
                $stmt = $connect->prepare('SELECT * FROM user WHERE GroupID != 1');

                $stmt->execute();
                
                $rows = $stmt->fetchAll();
            
            ?>

                <div class='container'>
                    <h1 class='text-center Manage'>Manage Member</h1>
                    <div class='table-resposnsive'>
                        <table class='main-table text-center table table-bordered'>
                            <tr>
                                <td>#ID</td>
                                <td>Username</td>
                                <td>Email</td>
                                <td>FullName</td>
                                <td>Registerd Date</td>
                                <td>Control</td>
                            </tr>
                            <tr>


                            <?php 
                                foreach($rows as $row){

                                    echo '<tr>';
                                        echo '<td>' . $row['UserID'] .'</td>';
                                        echo '<td>' . $row['Username'] .'</td>';
                                        echo '<td>' . $row['Email'] .'</td>';
                                        echo '<td>' . $row['FullName'] .'</td>';
                                        echo '<td> </td>';
                                        echo "<td>
                                                <a href='members.php?do=Edit&userid = " . $row['UserID'] ."' class='btn btn-success'>Edit</a>
                                                <a href='members.php?do=Delete&userid = " . $row['UserID'] ."' class='btn btn-danger confirm'>Delete</a>
                                             </td>";
                                    echo '</tr>';
                                }
                            
                            
                            ?>
  
                        </table>
                    </div>
                    <a href='members.php?do=Add' class='btn btn-primary'>Add New Members</a>
                </div>
                
             
    <?php   }elseif ($do == 'Edit'){ // Edit Page 
             
                $userid = isset($_GET['userid']) && is_numeric($_GET['userid']) ? intval($_GET['userid']) : 0 ;

                $stmt = $connect->prepare('SELECT * FROM user WHERE UserID = ? LIMIT 1 ');
                $stmt->execute(array($userid));
                $row = $stmt->fetch();
                $count = $stmt->rowCount();

			// If Count > 0 This mean The Database Contain About This Username

                if($count > 0) { ?>
                        
                    <div class='container'>

                        <h1 class='text-center Edit'>Edit Member</h1>
                        <form class='form-horizontal' action = '?do=Update' method='POST'>
                            <input type='hidden' name='userid' value='<?php echo $userid; ?>'/>
                            <div class='form-group form-group-lg'>

                                <!-- Start Username Field -->
                                <div class='col-sm-offset-4 col-sm-8 col-md-4 member'>
                                    <input type='text' name='username' placeholder='Username' value='<?php $row['Username'] ?>' required='required' class='form-control' autocomplete='off'>
                                </div>
                                <!-- End Username Field -->

                            </div>

                            <div class='form-group form-group-lg'>

                                <!-- Start Password Field -->
                                <div class='col-sm-offset-4 col-sm-8 col-md-4 member'>
                                    <input type='password' name='password' placeholder='Password'  class='form-control' autocomplete='new-password'>
                                </div>
                                <!-- End Password Field -->

                            </div>

                            <div class='form-group form-group-lg'>

                                <!-- Start Email Field -->
                                <div class='col-sm-offset-4 col-sm-8 col-md-4 member'>
                                    <input type='email' name='email' placeholder='Email' value='<?php $row['Email'] ?>' required='required' class='form-control' autocomplete='off'>
                                </div>
                                <!-- End Email Field --> 

                            </div>
                        
                            
                            <div class='form-group form-group-lg'>

                                <!-- Start FullName Field -->
                                <div class='col-sm-offset-4 col-sm-6 col-md-4 member'>
                                    <input type='text' name='fullName' placeholder='FullName' value='<?php $row['FullName'] ?>' required='required' class='form-control' autocomplete='off'>
                                </div>
                                <!-- End FullName Field -->

                            </div>
                            
                            <!-- Start submit Field -->
                            <div class='form-group form-group-lg'>
                                <div class='col-sm-offset-4 col-sm-8 member'>
                                    <input type='submit' value='Save' class='btn btn-primary btn-lg' >
                                </div>
                            </div>
                            <!-- End submit Field --> 
                        </form>
                    </div>

        <?php           
                }
                else{
                    $error = 'There\'s No such ID' ;
                    redirectHome($error , 3);
                }
            
            }elseif ($do == 'Update') {

                if($_SERVER['REQUEST_METHOD'] == 'POST'){

                    echo "<div class='container'> <h1 class='text-center Update'>Update Member</h1> </div>";
                    echo '<div class="container">';

                    // Get Variable From The Form

                    $id = $_POST['userid'];
                    $user = $_POST['username'];
                    $pass = $_POST['password'];
                    $hashedpass = sha1($pass);
                    $email = $_POST['email'];
                    $name = $_POST['fullName'];

                    // Validate Form

                    $formErrors = array(
                        'Username Can Not Be Empty And Can Not Be Less Than 3<strong> Characters</strong> ',
                        'Email Can Not Be<strong> Empty</strong> ',
                        'FullName Can Not Be<strong> Empty</strong>'
                    ); 

                    if(empty($user) OR strlen($user) < 3){
                        echo '<div class="alert alert-danger">' . $formErrors[0] . '</div>' ;
                    }
                    if(empty($email)){
                        echo '<div class="alert alert-danger">' . $formErrors[1] . '</div>' ;
                    }
                    if(empty($name)){
                        echo '<div class="alert alert-danger">' . $formErrors[2] . '</div>' ;
                    }

                    // Check If Not Found Error To Update The Data

                    if(strlen($user) > 3 And !empty($email) And !empty($name) ){
                        // Update The Database With This Info

                        $stmt = $connect->prepare("UPDATE user SET Username = ?, Password = ?, Email = ?, FullName = ? WHERE UserID = ? ");

                        $stmt->execute(array($user, $hashedpass, $email, $name, $id));

                        // Echo Success Message

                        echo '<div class="alert alert-success">' . $stmt->rowCount() . ' Record Update </div>';
                    }

                }
                else{
                    $error = 'You Can not reach to here direct' ;
                    redirectHome($error , 3); ;
                }

                echo '</div>'; // this div for container
                
            }elseif ($do == 'Add') { // Add Member Page ?>
                        
                <div class='container'>

                <h1 class='text-center Edit'>Add New Member</h1>
                <form class='form-horizontal' action = '?do=Insert' method='POST'>
                    <div class='form-group form-group-lg'>

                        <!-- Start Username Field -->
                        <div class='col-sm-offset-4 col-sm-8 col-md-4 member'>
                            <input type='text' name='username' placeholder='Username' required='required' class='form-control' autocomplete='off'>
                        </div>
                        <!-- End Username Field -->

                    </div>

                    <div class='form-group form-group-lg'>

                        <!-- Start Password Field -->
                        <div class='col-sm-offset-4 col-sm-8 col-md-4 member'>
                            <input type='password' name='password' placeholder='Password' required='required'  class='password form-control' autocomplete='new-password'>
                            <i class="show-pass fa fa-eye fa-2x"></i>
                        </div>
                        <!-- End Password Field -->

                    </div>

                    <div class='form-group form-group-lg'>

                        <!-- Start Email Field -->
                        <div class='col-sm-offset-4 col-sm-8 col-md-4 member'>
                            <input type='email' name='email' placeholder='Email' required='required' class='form-control' autocomplete='off'>
                        </div>
                        <!-- End Email Field --> 

                    </div>
                
                    
                    <div class='form-group form-group-lg'>

                        <!-- Start FullName Field -->
                        <div class='col-sm-offset-4 col-sm-6 col-md-4 member'>
                            <input type='text' name='fullName' placeholder='FullName'  required='required' class='form-control' autocomplete='off'>
                        </div>
                        <!-- End FullName Field -->

                    </div>
                    
                    <!-- Start submit Field -->
                    <div class='form-group form-group-lg'>
                        <div class='col-sm-offset-4 col-sm-8 member'>
                            <input type='submit' value='Save' class='btn btn-primary btn-lg' >
                        </div>
                    </div>
                    <!-- End submit Field --> 
                </form>
            </div>


    <?php   
            }elseif ($do == 'Insert') { // Insert Member Page 
                        
                // echo $_POST['username'] . $_POST['password'] . $_POST['email'] . $_POST['fullName'];

                if($_SERVER['REQUEST_METHOD'] == 'POST'){

                    echo "<div class='container'> <h1 class='text-center Insert'>Insert Member</h1> </div>";
                    echo '<div class="container">';

                    // Get Variable From The Form

                    $user = $_POST['username'];
                    $pass = $_POST['password'];
                    $hashedpass = sha1($pass);
                    $email = $_POST['email'];
                    $name = $_POST['fullName'];

                    // Validate Form

                    $formErrors = array(
                        'Username Can Not Be Empty And Can Not Be Less Than 3<strong> Characters</strong> ',
                        'Email Can Not Be<strong> Empty</strong> ',
                        'Password Can Not Be<strong> Empty</strong> ',
                        'FullName Can Not Be<strong> Empty</strong>'
                    ); 

                    if(empty($user) OR strlen($user) < 3){
                        echo '<div class="alert alert-danger">' . $formErrors[0] . '</div>' ;
                    }
                    if(empty($email)){
                        echo '<div class="alert alert-danger">' . $formErrors[1] . '</div>' ;
                    }
                    if(empty($pass)){
                        echo '<div class="alert alert-danger">' . $formErrors[2] . '</div>' ;
                    }
                    if(empty($name)){
                        echo '<div class="alert alert-danger">' . $formErrors[3] . '</div>' ;
                    }

                    // Check If Not Found Error To Update The Data

                    if(strlen($user) >= 3 And !empty($email) And !empty($name) ){
                        // Insert The Database With This Info

                        $stmt = $connect->prepare("INSERT INTO user (Username , Password, Email, FullName ) VALUES(:user, :pass, :email, :name )");

                        $stmt->execute(array(
                           'user'  =>  $user, 
                           'pass'  =>  $hashedpass, 
                           'email' =>  $email,
                           'name'  =>  $name
                        ));

                        // Echo Success Message

                        echo '<div class="alert alert-success">' . $stmt->rowCount() . ' Record Update </div>';
                    }

                }
                else{
                    $error = 'You Can not reach to here direct' ;
                    redirectHome($error , 3);
                }

                     echo '</div>'; // this div for container

            }elseif ($do == 'Delete'){ // Edit Page 
                echo "<div class='container'> <h1 class='text-center Delete'>Delete Member</h1> </div>";
                echo '<div class="container">';
             
                    $userid = isset($_GET['userid']) && is_numeric($_GET['userid']) ? intval($_GET['userid']) : 0 ;

                    $stmt = $connect->prepare('SELECT * FROM user WHERE UserID = ? LIMIT 1 ');
                    $stmt->execute(array($userid));
                    $count = $stmt->rowCount();

                // If Count > 0 This mean The Database Contain About This Username

                    if($count > 0) {

                        $stmt = $connect->prepare('DELETE FROM user WHERE UserID = :user');

                        $stmt->bindParam(':user' , $userid);

                        $stmt->execute();

                        echo '<div class="alert alert-success">' . $stmt->rowCount() . ' Record Deleted </div>';
                    }
            }else{
                    $error = 'You Can not reach to here direct' ;
                    redirectHome($error , 3);
            }

                echo '</div>';
            
			include $temp . 'footer/footer.php';
			
		}else{
			header('Location: ../index/index.php');

			exit();
		}