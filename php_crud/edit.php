<?php
// Edit employee
include 'db_connect.php';
$id = $_GET['id'];
$result = $conn->query("SELECT * FROM employees WHERE id=$id");
$employee = $result->fetch_assoc();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $role = $_POST['role'];
    $salary = $_POST['salary'];
    $conn->query("UPDATE employees SET name='$name', role='$role', salary='$salary' WHERE id=$id");
    header("Location: index.php");
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Edit Employee</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container mt-5">
    <h1>Edit Employee</h1>
    <form method="POST">
        <input type="text" name="name" value="<?= $employee['name'] ?>" class="form-control mb-3" required>
        <input type="text" name="role" value="<?= $employee['role'] ?>" class="form-control mb-3" required>
        <input type="number" name="salary" value="<?= $employee['salary'] ?>" class="form-control mb-3" required>
        <button type="submit" class="btn btn-primary">Update</button>
        <a href="index.php" class="btn btn-secondary">Back</a>
    </form>
</body>
</html>
