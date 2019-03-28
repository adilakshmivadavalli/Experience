<?php
        include 'check_cookie.php';

        $server_name = "localhost";
        $user_name = "movie_user";
        $admin_name = "movie_admin";
        $admin_password = "password";
        $dbname = "moviedb";

        $conn = new mysqli($server_name, $admin_name, $admin_password, $dbname);

        //这部分只用于检查数据库的连接情况
        if ($conn ->connect_error){
            echo "Mysql database connection failed";
        }

        //这部分只用于检查数据库的连接情况

        $film = $_GET['mod_movie_name'];
        $new_name = $_GET['mod_new_name'];
        $genre = $_GET['mod_genre'];
        $tomatoes = $_GET['mod_tomatoes'];
        $audience = $_GET['mod_audience'];
        $budget = $_GET['mod_budget'];
        $year = $_GET['mod_year'];
        
        $set_parameter = "Film= '".$new_name."', Genre= '".$genre."', Rotten_Ratings= ".$tomatoes.", Audience_Ratings= ".$audience.", Budget_M= ".$budget.", Year_Release= ".$year;
        $sql = "UPDATE movie_table SET ".$set_parameter." WHERE Film = '".$film."'";

        if ($conn->query($sql) === TRUE) {
                echo "Record updated successfully!";
            }
            else {
                echo "Error: ".$sql."<br>".$conn->error;
            }
        echo "<a href='admin_page.html'><button>Go Back</button></a>";
        $conn->close();
        ?>

