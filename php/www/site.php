<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
</head>
<body>
    <?php 
        echo "<h1>Sani's Site</h1>";
        echo "<hr>";
        echo "<p>This is my site</p>";
    ?>

    <?php
        $characterName = "Tom";
        $characterAge = 80;
        echo "There was once a man named $characterName <br>";
        echo "He was $characterAge years old <br>";
        $characterName = "Mike";
        echo "He really liked the name $characterName <br>";
        echo "but didn't like being $characterAge <br>";
    ?>

    <!-- Data types -->
    <?php
        $phrase = "To be or not to be";
        $age = 30;
        $gpa = 3.023;
        $isMale = true;
        $noValue = null;
        echo $phrase;
    ?>

    <!-- Strings -->
    <?php
        echo "<br>";
        $phrase = "Giraffe Academy";
        echo $phrase;
        echo "<br>";
        echo strtolower($phrase);
        echo "<br>";
        echo strlen($phrase);
        echo "<br>";
        echo $phrase[1];
        echo "<br>";
        $phrase[0] = "J";
        echo $phrase;
        echo "<br> <br>";

        echo str_replace("Jiraffe", "Panda", $phrase);

        echo "<br>";
        echo substr($phrase, -8, 3);
        echo "<br> <br>";
    ?>

    <!-- Numbers -->
    <?php
        echo 5+4;
        echo "<br>";
        echo 20 / 4;
        echo "<br>";
        echo 10 % 3;
        echo "<br>";
        $num = 10;
        $num++;
        $num += 10;
        echo $num;
        echo "<br>";
        echo abs(-100);
        echo "<br>";
        echo pow(2, 4);
        echo "<br>";
        echo sqrt(2);
        echo "<br>";
        echo max(2, 10);
        echo "<br>";
        echo round(3.4);
        echo "<br>";
        echo ceil(3.2);
        echo "<br>";
        echo floor(3.8);
    ?>
</body>
</html>