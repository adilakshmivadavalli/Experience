<html>
    <head>
        <title>Search</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
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

        $movie_name = $_GET['movie_name'];
        $genre = $_GET['genre'];
        $tomatoes_min = $_GET['tomatoes_min'];
        $tomatoes_max = $_GET['tomatoes_max'];
        $audience_min = $_GET['audience_min'];
        $audience_max = $_GET['audience_max'];
        $budget_min = $_GET['budget_min'];
        $budget_max = $_GET['budget_max'];
        $year_min = $_GET['year_min'];
        $year_max = $_GET['year_max'];
        

        $where_condition = "WHERE Film LIKE "."'%".$movie_name."%'";
        if($genre != null){
            $where_condition = $where_condition . " AND Genre LIKE '". $genre."'" ;
        }
        if($tomatoes_min != null){
            $where_condition = $where_condition . " AND Rotten_Ratings >= ". $tomatoes_min ;
        }
        if($tomatoes_max != null){
            $where_condition = $where_condition . " AND Rotten_Ratings <= ". $tomatoes_max ;
        }
        if($audience_min != null){
            $where_condition = $where_condition . " AND Audience_Ratings >= ". $audience_min ;
        }
        if($audience_max != null){
            $where_condition = $where_condition . " AND Audience_Ratings <= ". $audience_max ;
        }
        if($budget_min != null){
            $where_condition = $where_condition . " AND Budget_M >=". $budget_min ;
        }
        if($budget_max != null){
            $where_condition = $where_condition . " AND Budget_M <=". $budget_max ;
        }
        if($year_min != null){
            $where_condition = $where_condition . " AND Year_Release >=". $year_min ;
        }
        if($year_max != null){
            $where_condition = $where_condition . " AND Year_Release <=". $year_max ;
        }

        $sql = "SELECT Film, Genre, Rotten_Ratings, Audience_Ratings, Budget_M, Year_Release FROM movie_table ".$where_condition;
        $result = $conn->query($sql);
        
        if($result->num_rows > 0){
            echo"<style>table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
                margin-left:auto;
                margin-right:auto;
            }
            </style>";
            echo "<h2>Search Results</h2>";
            echo"<table name='return_result' id='return_result_id'>";
            echo"<tr><th>Movie</th><th>Genre</th><th>Rotten Ratings %</th><th>Audience Ratings %</th><th>Budget in Millions $</th><th>Year</th><th>Modify</th><th>Delete</th></tr>";
                
            while($row = $result->fetch_assoc()){
                $movie_name=$row["Film"];
                    echo "<tr>";
                    echo"<td>";echo $row["Film"],"</td>";
                    echo"<td>";echo $row["Genre"],"</td>";
                    echo"<td>";echo $row["Rotten_Ratings"],"</td>";
                    echo"<td>";echo $row["Audience_Ratings"],"</td>";
                    echo"<td>";echo $row["Budget_M"],"</td>";
                    echo"<td>";echo $row["Year_Release"],"</td>";
                    echo"<td>";echo "<button onclick='movie_modify(this)'>Modify</button>","</td>";
                    echo"<td>";echo "<button onclick='movie_delete(this)'>Delete</button>","</td>";
                    echo "<tr>";
            }
            
            echo "</table>";
        }
        else {
            echo "No results.";
        }
    ?>
    </body>
</html>