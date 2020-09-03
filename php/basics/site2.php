<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <!-- Classes and objects -->
    <?php
        class Book {
            public $title;
            private $author;
            var $pages; // var is similar to public

            function __construct($aTitle, $aAuthor, $aPages){
                $this->title = $aTitle;
                $this->author = $aAuthor;
                $this->pages = $aPages;
            }

            function printDes(){
                echo "$this->title  by  $this->author";
            }

            function getAuthor(){
                return $this->author;
            }

            function setAuthor($aAuthor){
                $this->author = $aAuthor;
            }
        }

        // $book1 = new Book;
        // $book1->title = "Harry Potter";
        // $book1->author = "JK Rowling";
        // $book1->pages = 400;
        
        // $book2 = new Book;
        // $book2->title = "Lord of the Rings";
        // $book2->author = "Tolkein";
        // $book2->pages = 700;

        $book3 = new Book("a bok", "bik", 21);
        $book3->printDes();

        echo $book3->title;


        class StoryBook extends Book {
            // some code goes here
        }
    ?>
</body>
</html>