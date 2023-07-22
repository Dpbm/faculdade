<?php
    $access = $_GET['access'];
    if($access != 'granted'){
        include("denied.html");
    }else{
        include("index.html");
    }
?>