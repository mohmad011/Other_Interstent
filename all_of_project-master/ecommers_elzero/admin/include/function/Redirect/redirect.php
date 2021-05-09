<?php

    /**
     * 
     */

     function redirectHome($errorMessage , $second = 3){
        echo "<div class='alert alert-danger'> $errorMessage </div>"; 
        echo "<div class='alert alert-danger'>' You Will Redirect To Home Page After ' $errorMessage ' Seconds ' </div>"; 

        header("refresh:$second ; url=../index/index.php");

        exit();
     }