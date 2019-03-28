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

        $film = $_GET['del_movie_name'];

        $sql = "DELETE FROM movie_table WHERE Film = '".$film."'";

        if ($conn->query($sql) === TRUE) {
                echo "Record deleted successfully!";
            }
            else {
                echo "Error: ".$sql."<br>".$conn->error;
            }

        echo "<a href='admin_page.html'><button>Go Back</button></a>";    
        $conn->close();
        ?>

