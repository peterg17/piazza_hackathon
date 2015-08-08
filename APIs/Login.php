<?php

require 'connection.php';

$sql = "SELECT *
		FROM Users
		WHERE email = :email
		AND password = :password";
	
		$stmt = $dbConn->prepare($sql);
		//$stmt->execute(array(":email" => $_GET['email'], ":password" => $_GET['password']));
		$stmt->execute(array(":email" => $_POST['email'], ":password" => $_POST['password']));
		$record = $stmt->fetch();
		
		if(empty($record)) {
			$response = array("loginApproved" => FALSE);	
		}
		else {
			$response = array("loginApproved" => TRUE);
		}
		
		echo json_encode($response);
		
?>