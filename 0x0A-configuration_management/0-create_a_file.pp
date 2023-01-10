# Using Puppet, create a file in /tmp.

file {'school':
  ensure  => present,
  path    => '/tmp/school',
  content => 'I Love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744'
}
