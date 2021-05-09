<?php

    /**
     *  Title Function That Echo The Page Title In Case The Page
     *  Has The Varriable $pageTitle Ans Echo Defult Title If It Is Not Found
     */

     function gettitle() {

        global $pageTitle;

        if(isset($pageTitle)) {
            echo $pageTitle;
        }else{
            echo 'Defult';
        }
     }

     
     function getcolor() {

        global $pageColor;

        if(isset($pageColor)) {
            echo $pageColor;
        }else{
            echo '#596275';
        }
     }