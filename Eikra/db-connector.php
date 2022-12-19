 <?php
$servername = "localhost";
$username = "nilesh";
$password = "1234";
$dbname = "streetcorner";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?> 