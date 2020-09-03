<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
</head>
<body>
    <!-- Including HTML files -->
    <?php
        include "header.html"
    ?>

    <!-- Including php files -->
    <?php
        $title = "testing";
        $author = "sani";
        $wordcount = 12;
        include "article_header.php";
        sayHello("Visitor");
    ?>

    

    <?php 
        echo "<h1>Sani's Site</h1>";
        echo "<hr>";
        echo "<p>This is my site</p>";
    ?>
    <br><br>

    <!-- If Condition -->
    <?php
        $isMale = true;
        $isTall = false;

        if ($isMale && $isTall){
            echo "tall male";
        } elseif ($isMale && !$isTall) {
            echo "short male";
        }
    ?>

    <br><br>
    <!-- Functions --> 
    <?php
        function sayHi($name){
             echo "hello $name";
        }
        sayHi("Tom");

        function cube($num){
            return pow($num, 3);
        }
        echo cube(4);
    ?>

    <br><br>

    <!-- Associative array  - similar to dictionary -->
    <form action="site.php" method="post">
        <input type="text" name="name"><br>
        <input type="submit">
    </form>
    <?php
        $grades = array("Jim"=>"A+", "Pam"=>"B-", "Oscar"=>"C+");
        // $age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");

        echo $grades[$_POST["name"]];
    ?>
    <br><br>


    <!-- Arrays -->
    <?php
        $friends = array("kevin", "Hello", "mellwo",);
        $friends[2] = "bee";
        echo $friends[2];
        echo count($friends);
    ?>

    <br><br>
    <form action="site.php" method="post">
        Apples: <input type="checkbox" name="fruits[]" value="apples"><br>
        Oranges: <input type="checkbox" name="fruits[]" value="oranges"><br>
        Pears: <input type="checkbox" name="fruits[]" value="apears"><br>
        <input type="submit">
    </form>
    <?php
        $fruits = $_POST["fruits"];
        echo $fruits[0];
    ?>
    <br>

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
        echo "<br>";
        echo "<br>";
    ?>

    <form action="site.php" method="get">
        Name: <input type="text" name="name">
        <br><br>
        Age: <input type="text" name="age">
        <br><br>
        <input type="submit">
    </form>
    <br>
    Your name is <?php echo $_GET["name"] ?>
    <br>
    Your age is <?php echo $_GET["age"] ?>

    <br><br><br>

    <form action="site.php" method="get">
        <input type="number" name="num1">
        <br>
        <input type="number" name="num2">
        <br>
        <input type="submit">
    </form>
    <br>
    Answer: <?php echo $_GET["num1"] + $_GET["num2"] ?>
    <br>


    <form action="site.php" method="get">
        Color: <input type="text" name="color">
        <br>
        Plural Noun: <input type="text" name="pluralNoun">
        <br>
        Celebrity: <input type="text" name="celebrity">
        <br>
        <input type="submit">
    </form>
    <br>
    <?php
        $color = $_GET["color"];
        $pluralNoun = $_GET["pluralNoun"];
        $celebrity = $_GET["celebrity"];
        echo "Roses are $color <br>";
        echo "$pluralNoun are blue <br>";
        echo "I love $celebrity <br>";
    ?>
    <br><br>
    <form action="site.php" method="post">
        <input type="password" name="password">
        <input type="submit">
    </form>
    <?php
        echo $_POST["password"];
    ?>


</body>
</html>