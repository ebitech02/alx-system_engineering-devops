exec { 'apply-fix':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
  unless  => 'grep -q "php" /var/www/html/wp-settings.php',
}

