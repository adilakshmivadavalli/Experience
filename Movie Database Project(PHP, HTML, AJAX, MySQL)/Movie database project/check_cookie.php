<?php

       
        if (!isset($_COOKIE['user_name']) and !isset($_COOKIE['user_password'])) {
            exit("authentication required;");
        }
        else {
            
            $user_name = $_COOKIE['user_name'];
            $user_password = $_COOKIE['user_password'];
            
            $server_name = "localhost";
            $user_name = "movie_user";
            $admin_name = "movie_admin";
            $admin_password = "password";
            $dbname = "moviedb";
            
            $conn = new mysqli($server_name, $admin_name, $admin_password, $dbname);

            if ($conn ->connect_error){
                echo "Mysql database connection failed";
            }
            
            $sql = "SELECT Password FROM account_table WHERE Name = '".$user_name."'";
       
            $result = $conn->query($sql);
            $row = $result->fetch_assoc();
            $registered_password = $row["Password"];
        
            if ($user_password === $registered_password) {
                exit("authentication failed;");
            }
            
            $conn->close();
        }
    
        
        

