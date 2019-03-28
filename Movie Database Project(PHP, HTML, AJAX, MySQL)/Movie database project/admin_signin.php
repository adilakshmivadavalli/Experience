<?php
        $server_name = "localhost";
        $user_name = "movie_user";
        $admin_name = "movie_admin";
        $admin_password = "password";
        $dbname = "moviedb";

        $conn = new mysqli($server_name, $admin_name, $admin_password, $dbname);

        if ($conn ->connect_error){
            echo "Mysql database connection failed";
        }


        $user_name = $_GET['user_name'];
        $user_password = $_GET['user_password'];


        $sql = "SELECT Password FROM account_table WHERE Name = '".$user_name."'";
       
        $result = $conn->query($sql);
        $row = $result->fetch_assoc();
        $registered_password = $row["Password"];
        
        if ($user_password === $registered_password) {
            if (isset($_GET['user_remember'])){
                setcookie('user_name', $user_name, time() + (86400 * 30), '/');
                setcookie('user_password',$user_password, time() + (86400 * 30), '/');
            }
            else {
                setcookie('user_name', $user_name,0, '/');
                setcookie('user_password', $user_password,0, '/');
            }
  
            header("Location: admin_page.html");
        }
        else {
            echo "Sign-in failed.";
        }

        $conn->close();
    ?>
