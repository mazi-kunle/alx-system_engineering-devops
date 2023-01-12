# a manifest for ssh configuration

exec {'ssh':
  command => 'echo "IdentityFile ~/.ssh/school\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/usr/bin'
}
