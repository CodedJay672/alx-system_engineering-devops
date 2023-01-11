file { 'content':
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  path    => '/tmp/school',
  content => 'I love Puppet'
}
