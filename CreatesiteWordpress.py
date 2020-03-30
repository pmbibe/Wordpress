import os
def prepare():
    print("Installing php-mysql-nginx")
    os.system("chmod +x mysql-nginx-php.sh && ./mysql-nginx-php.sh")
def download_wordpress():
    os.system("wget https://vi.wordpress.org/latest-vi.tar.gz")
    os.system("tar -xvf latest-vi.tar.gz")
def deploy_site_wordpress(name):
    nginx_path = "/usr/share/nginx/" + name
    os.system("mkdir " + nginx_path)
    os.system("""cp -R wordpress/* """ + nginx_path)
    os.system("chmod -R 755 " + nginx_path)
    os.system("chown -R nginx:nginx /usr/share/nginx/")
#    copyfile = "cp default.conf /etc/nginx/conf.d/" + name + ".conf"
#    os.system(copyfile)
def create_file_config_nginx(name):
    file_config = name + ".nginx.conf"
    create_new_config_comand = """sed 's/domain_name/""" + name + """/' > /etc/nginx/conf.d/ """ + name + ".conf"
    os.system(create_new_config_comand)
#    copyfile = "cp default.conf /etc/nginx/conf.d/" + name + ".conf"
#    os.system(copyfile)
#    os.system("""echo "some data for the file" >> """ + file_config)
    