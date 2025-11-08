<?php
// Add employee
include 'db_connect.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $role = $_POST['role'];
    $salary = $_POST['salary'];

    $sql = "INSERT INTO employees (name, role, salary) VALUES ('$name', '$role', '$salary')";
    if ($conn->query($sql)) {
        header("Location: index.php");
    } else {
        echo "Error: " . $conn->error;
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add Employee</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container mt-5">
    <h1>Add Employee</h1>
    <form method="POST">
        <input type="text" name="name" placeholder="Name" class="form-control mb-3" required>
        <input type="text" name="role" placeholder="Role" class="form-control mb-3" required>
        <input type="number" name="salary" placeholder="Salary" class="form-control mb-3" required>
        <button type="submit" class="btn btn-success">Save</button>
        <a href="index.php" class="btn btn-secondary">Back</a>
    </form>
</body>
</html>
