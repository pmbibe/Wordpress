# Wordpress - Centos7

git clone https://github.com/pmbibe/Wordpress

cd Wordpress

chmod +x mysql-nginx-php.sh

./mysql-nginx-php.sh

python3 CreatesiteWordpress.py web1.com web2.com web3.com

Ở đây, mật khẩu mặc định của mysql sẽ là HelloWorld nên chúng ta có thể đổi lại tùy ý chúng ta ở trong file .my.cnf

Đối với server đã cài đặt mysql, nginx và php. Thì nên tạo file .my.cnf chưa user và pass để đăng nhập mysql.

[mysql]

user=root

password=HelloWorld

PHP sử dụng unixsocket. Bằng cách sử dụng câu lệnh sau: \cp www.conf /etc/php-fpm.d/www.conf
