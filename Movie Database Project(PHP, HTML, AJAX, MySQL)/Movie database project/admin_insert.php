<?php
        include 'check_cookie.php';
        
        $server_name = "localhost";
        $user_name = "movie_user";
        $admin_name = "movie_admin";
        $admin_password = "password";
        $dbname = "moviedb";

        $conn = new mysqli($server_name, $admin_name, $admin_password, $dbname);

        if ($conn ->connect_error){
            echo "Mysql database connection failed";
        }

        $film = $_GET['add_movie_name'];
        $genre = $_GET['add_genre'];
        $tomatoes = $_GET['add_tomatoes'];
        $audience = $_GET['add_audience'];
        $budget = $_GET['add_budget'];
        $year = $_GET['add_year'];

        $sql = "INSERT INTO movie_table (Film, Genre, Rotten_Ratings, Audience_Ratings, Budget_M, Year_Release) "
                    . "VALUES ('".$film."','".$genre."','".$tomatoes."','".$audience."','".$budget."','".$year."')";

        $results = $conn->query($sql);
        echo "Record added successfully!";
        echo "<br/>";
        echo "<a href='admin_page.html'><button>Go back</button></a>";
        ?>


