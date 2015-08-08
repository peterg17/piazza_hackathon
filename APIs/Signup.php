<?php

require 'connection.php';

$sql = "INSERT INTO Users
		(email, password)
		VALUES(:email, :password)";
		
		$stmt = $dbConn->prepare($sql);
		$stmt->execute(array(":email" => $_POST["email"],
	 					  ":password" => $_POST["password"]));
						  
		$response = array("message" => "Welcome ".$_POST["email"]); 
		echo json_encode($response);
?>