<?php
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

        $user_name = $_GET['user_name'];
        $user_password = $_GET['user_password'];
        $user_email = $_GET['user_email'];


        $sql = "INSERT INTO account_table (Name, Password, Email) "
               . "VALUES ('".$user_name."','".$user_password."','".$user_email."')";

            if ($conn->query($sql) === TRUE) {
                echo "Account registered successfully!";
                
            }
            else {
                echo "Error: ".$sql."<br>".$conn->error;
            }
            echo "<a href='index.html'><button>Go Back</button></a>";
            $conn->close();
    ?>
