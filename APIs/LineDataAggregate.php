<?php
   require 'connection.php';
   
   $sql = "SELECT dateTime, t.type_code
		   FROM  `Errors` e
		   INNER JOIN Types t ON t.type_id = e.type_id
		   ORDER BY DATETIME ASC";

		$stmt = $dbConn->prepare($sql);
		$stmt->execute();
		$errors = $stmt->fetchAll();
		
		$data = array();
		
		foreach($errors as $e) {
			$data[] = array($e["dateTime"] => $e["type_code"]);
		}
   		
		echo json_encode($data);
?>