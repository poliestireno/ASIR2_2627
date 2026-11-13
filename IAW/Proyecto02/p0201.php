<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        for ($i=0; $i < 10000; $i++)
        {
            echo "<p>ESTE ES MI PARRAFO NÚMERO ". $i ."</p>";
        }
        $aAlumnos = array ();
        $aAlumnos[0]="Dylan";
        $aAlumnos[1]="Ainara";
        $aAlumnos[2]="Gino";
        $aAlumnos[3]="Moha";
        $aAlumnos[4]="Dani";
        $aAlumnos[5]="Álvaro";
        $aAlumnos[6]="Adrián";
        echo "<ul>";
        foreach ($aAlumnos as $iAlumno) 
        {
            echo "<li>".$iAlumno."</li>";
        }
        echo "</ul>";

        // CREAR UN ARRAY DE NUMERO DE ZAPATOS DE 15 PERSONAS, CALCULAR EL ZAPATO MAYOR, EL MENOR Y LA MEDIA
    ?>

</body>
</html>