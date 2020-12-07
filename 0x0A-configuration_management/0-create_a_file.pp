#Create a file
file { '/tmp/holberton':
  ensure  => 'file',
  content => 'I Love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
