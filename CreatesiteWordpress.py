import os
from os import path
import sys
def prepare():
    os.system("Installing php-mysql-nginx")
    os.system("chmod +x mysql-nginx-php.sh && ./mysql-nginx-php.sh")
def download_wordpress():
    os.system("wget https://vi.wordpress.org/latest-vi.tar.gz")
    os.system("tar -xvf latest-vi.tar.gz")
def deploy_site_wordpress(name):
    nginx_path = "mkdir /usr/share/nginx/" + name
    os.system(nginx_path)
    copy_file = """cp -R wordpress/* /usr/share/nginx/""" + name
    os.system(copy_file)
    chmod_file = "chmod -R 755 /usr/share/nginx/" + name
    os.system(chmod_file)
    os.system("chown -R nginx:nginx /usr/share/nginx/")
#    copyfile = "cp default.conf /etc/nginx/conf.d/" + name + ".conf"
#    os.system(copyfile)
def create_file_config_nginx(name):
    file_config = name + ".nginx.conf"
    create_new_config_comand = """sed 's/domain_name/""" + name + """/' default.conf > /etc/nginx/conf.d/""" + name + ".conf"
    os.system(create_new_config_comand)
def config_databases(name):
    name_split = name.split(".")
    databases = name_split[0]+"_db"
    user = name_split[0]+"_user"
    password = name_split[0]+"_7b****"
    command = """mysql -Bse "CREATE DATABASE """ + databases + """; CREATE USER '""" + user + """'@'localhost' IDENTIFIED BY '"""+ password+ """'; GRANT ALL PRIVILEGES ON """ + databases+ """.* TO '"""+ user+ """'@'localhost';""" + '"'
    os.system(command)
    command_wp_databases = """sed 's/database_name_here/""" + databases + """/; s/username_here/""" + user + """/; s/password_here/""" + password + """/' wp-config.php > /usr/share/nginx/""" + name + "/wp-config.php"
    os.system(command_wp_databases)
def main():
    if path.exists('wordpress') == False:
        download_wordpress()
    for site in (1, len(sys.argv)):
        deploy_site_wordpress(sys.argv[site])
        create_file_config_nginx(sys.argv[site])
        config_databases(sys.argv[site])
main()
