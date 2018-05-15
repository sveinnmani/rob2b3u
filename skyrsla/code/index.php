<html>
	<head>
		<title>Security system</title>
		<link rel="stylesheet" type="text/css" href="css/style.css">
	</head>
	<body>
		<?php
		phpinfo();
		?>
		<img src="http://10.201.38.165:8081" width="640" height="480"/>
		<form action ="/forward" method="POST">
			<input type="submit" value="forward">
		</form>
		<form action ="/backward" method="POST">
			<input type="submit" value="backward">
		</form>
		<form action ="/left" method="POST">
			<input type="submit" value="left">
		</form>
		<form action ="/right" method="POST">
			<input type="submit" value="right">
		</form>
		<form action ="/stop" method="POST">
			<input type="submit" value="stop">
		</form>
	
		<button id="autorun" type="submit">Run code</button>
		<!--<script type="text/javascript" src="http://code.jquery.com/jquery-latest.min.js"></script>
		<script src="javascript/main.js"></script>-->
		<script type="text/javascript">
			var ip = "<?php echo $_SERVER['SERVER_ADDR']; ?>";
			alert(ip);
		</script>
	</body>
</html>
