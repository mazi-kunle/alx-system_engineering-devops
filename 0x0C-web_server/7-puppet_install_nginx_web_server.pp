# A manifest to install and configure nginx

# update apt
exec {'update_apt':
  command => 'sudo apt-get update',
  path    => '/usr/bin'
}

# install nginx
package {'install_nginx':
  ensure  => installed,
  name    => 'nginx',
  require => Exec['update_apt']
}

# create index.html
file {'/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!\n"
}

exec {'redirect_me':
  command => 'sudo sed -i "25 i\	location /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}" /etc/nginx/sites-available/default',
  path    => '/usr/bin'
}

# run nginx
service {'nginx':
  ensure  => running,
  require => Package['install_nginx']
}
