<?php
//database ko name php_crud_db
$servername = "localhost";
$username = "root";
$password = ""; 
$database = "php_crud_db";

$conn = new mysqli($servername, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
