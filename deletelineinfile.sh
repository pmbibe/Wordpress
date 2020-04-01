#!/bin/bash
sed -i ' /WP_SITEURL/d' /srv/www/$1/wp-config.php  && sed -i '/WP_HOME/d' /srv/www/$1/wp-config.php
