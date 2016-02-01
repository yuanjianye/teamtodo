<?php
require "tt_config.php";
$conn=mysql_connect($myserver_name,$myserver_username,$myserver_password);
if(!$conn){
    die('Could not connect: '.mysql_error());
}
mysql_select_db($myserver_database,$conn);
#$strsql="select * from `tb_todolist`";
$filename="./add_user.json";
$handle=fopen($filename,"r");
$content=fread($handle,filesize($filename));
#print $content;
$useradd=json_decode($content);
print $useradd->{'user_name'};
print $useradd->{'user_passwd'};
$sqlstr = "INSERT INTO tb_user (user_name,user_passwd) VALUES ("
    ."'"
    .$useradd->{'user_name'} 
    ."'"
    .','
    ."'"
    .openssl_digest($useradd->{'user_passwd'},'sha512')
    ."'"
    .")";
echo $sqlstr;
mysql_query($sqlstr);
mysql_error();
mysql_close($conn);
?>
