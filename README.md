# Mesos Marathon Web Client

Mesos Marathon Web Client is a simple web application that allows you to create a simple job in Mesos Cluster by using Marathon API.

## Prerequisite 
1. Fully functional Marathon with Mesos Cluster
2. Fresh Ubuntu 14.04.5 (To host this Application)

## Installation 

Step 1: Update your Operating System

     $ sudo apt-get update -y

Step 2: Install Apache & Project Dependencies

    $ sudo apt-get install apache2 libapache2-mod-wsgi python python-dev git vim -y 

Step 3: Enable mod_wsgi

    $ sudo a2enmod wsgi
Step 4: Go to Apache ROOT Directory

    $ cd /var/www

Step 5: Clone Project Files
    
    $ sudo git clone https://github.com/timam/mesos-marathon-web-client.git

Step 6: Replace default apache configuration with the following lines

    $ sudo vim /etc/apache2/sites-availabe/000-default.conf
    
	<VirtualHost *:80>
                WSGIScriptAlias / /var/www/mesos-marathon-web-client/app.wsgi
                WSGIDaemonProcess app python-path=/var/www/mesos-marathon-web-client:/var/www/mesos-marathon-web-client/app/venv/lib/python2.7/site-packages
                WSGIProcessGroup app
                <Directory /var/www/mesos-marathon-web-client/app>
                	Require all granted
		</Directory>
                Alias /static /var/www/mesos-marathon-web-client/app/static
                <Directory /var/www/mesos-marathon-web-client/app/static>
                	Require all granted
		</Directory>
                ErrorLog ${APACHE_LOG_DIR}/error.log
                LogLevel warn
                CustomLog ${APACHE_LOG_DIR}/access.log combined
	</VirtualHost>

Step 9: Now you have set up Mesos Marathon Web Client all the way down, But you need to configure this application with your marathon url.  Follow the comments, You will surely get where need to change
    
    $ sudo vim /var/www/mesos-marathon-web-client/app/__init__.py
    
Step 7: Restart Apache

    $ sudo service apache2 restart
    
Step 10 : Test IT!!  Go to http://your.ip from Browser

## Functionality 
* [Create] - Creates a New App on Mesos Cluster
* [Destroy] - Destroys the App Created on Mesos Cluster