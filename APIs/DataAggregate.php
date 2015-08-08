<?php

require 'connection.php';

$sql = "SELECT t.type_code
		FROM  `Errors` e
		INNER JOIN Types t ON t.type_id = e.type_id
		ORDER BY e.type_id ASC";
		
		$stmt = $dbConn->prepare($sql);
		$stmt->execute();
		$errors = $stmt->fetchAll();
		
		$errorCount = 0;
		$currentError = $errors[0]["type_code"];
		$data = array();
		
		foreach($errors as $e) {
			if ($e["type_code"] == $currentError) {
				$errorCount++;	
			}
			else {
				$data[] = array("$currentError" => $errorCount);
				$currentError = $e["type_code"];
				$errorCount = 1;
			}
		}
		echo json_encode($data);
?>