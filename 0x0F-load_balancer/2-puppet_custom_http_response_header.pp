# A manifest for creating a custom HTTP header

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


exec {'add_header':
  command => 'sudo sed -i "25 a\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  path    => '/usr/bin'
}

# run nginx
service {'nginx':
  ensure  => running,
  require => Package['install_nginx']
}
