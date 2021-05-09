<?php

    /**
     *    Categories => [ Manage | Edit | Update | Add | Insert | Delete | Stats ]
     *  
     *    Condition ? True : False ==> $do = isset($_GET['do]) ? $_GET['do'] : 'Manage';
     */

     $do = isset($_GET['do']) ? $_GET['do'] : 'Manage';

   //   $do = '';

   //   if (isset($_GET['do'])){

   //      $do = $_GET['do'];

   //   }else{

   //      $do = 'Manage';
   //   }

     // If The Page Is Main Page

     if($do == 'Manage') {

        echo 'Welcome You Are In Manage Categories Page';
        echo '<a href="page.php?do=Insert">Add New Categories +</a>';
     } elseif ($do == 'Add'){
        
        echo 'Welcome You Are In Add Categories Page';
     }elseif ($do == 'Insert'){
        
        echo 'Welcome You Are In Insert Categories Page';
     }else{
         echo " Error There's No Page With This Name";
     }