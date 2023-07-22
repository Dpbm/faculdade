<?php
    header('Access-Control-Allow-Origin: *');
    header('Content-type: application/json');

    $data = array('hello' => 'world!');

    echo json_encode($data);
?>