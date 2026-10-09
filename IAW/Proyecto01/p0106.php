<!DOCTYPE html>
<html lang="en">
    <?php var_export($_POST);?>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1><?php echo "la suma es:". ($_POST['n1'] + $_POST['n2']) ?></h1>
</body>
</html>