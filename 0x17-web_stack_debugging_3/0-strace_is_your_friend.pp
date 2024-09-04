# Ensures Apache has the correct directory and permissions

package { 'apache2':
  ensure =>  installed,
}

file { '/var/www/html':
  ensure =>  directory,
  owner  =>  'www-data',
  group  =>  'www-data',
  mode   =>  '0755',
}

file { '/var/www/html/directory':
  ensure => directory,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

file { '/var/log/apache2':
  ensure => directory,
  owner  =>  'www-data',
  group  =>  'www-data',
  mode   =>  '0755',
}

service { 'apache2':
  ensure =>  running,
  enable => true,
}

