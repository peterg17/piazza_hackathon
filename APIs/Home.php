<?php

require 'connection.php';

$sql = "SELECT u.email, error_id, datetime, t.type_code, message, solution
		FROM  `Errors` e
		INNER JOIN Types t ON t.type_id = e.type_id
		INNER JOIN Users u ON u.user_id = e.user_id";
		$stmt = $dbConn->prepare($sql);
		$stmt->execute();
		$errors = $stmt->fetchAll();

$output = array();
$output[] = array("username" => $errors[0]["email"]);

foreach($errors as $userError) {
	$timestamp = $userError["datetime"];
	$errorID = $userError["error_id"];
	$errorType = $userError["type_code"];
	$errorMessage = $userError["message"];
	$solutionComments = $userError["solution"];
	$output[] = array("timestamp" => $timestamp ,"errorID" => $errorID, "errorType" => $errorType, 
				"errorMessage" => $errorMessage, 
				"solutionComments" => $solutionComments);
}

echo json_encode($output);

?>