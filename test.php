<?php
    $myserver_name="localhost";
    $myserver_username="root";
    $myserver_password="Jiawm5535";
    $myserver_database="teamtodo";
    $conn=mysql_connect($myserver_name,$myserver_username,$myserver_password);
//    echo $conn."\n";
    $strsql="select * from `tb_todolist`";
    $result=mysql_db_query($myserver_database,$strsql,$conn);
//    echo $result,"\n";
    for($i=0;$i<mysql_num_fields($result);$i++){
        echo mysql_field_name($result,$i);
        echo "\t";
    }
    echo "\n";
    mysql_data_seek($result,0);
    $x = 0;
    while($row=mysql_fetch_row($result)){
        for($i=0;$i<mysql_num_fields($result);$i++){
            echo $row[$i];
            echo "\t";
            $myresult_obj[$x]->{mysql_field_name($result,$i)}=$row[$i];
        }
        $x++;
        echo "\n";
    }
    $myattr = array('a'=>1, 'b'=>2, 'c'=>3);
    $row_json = json_encode($myresult_obj);
    echo $row_json;
    echo "\n";

//    echo $row."\n";
//    echo "this is a test";
?>
