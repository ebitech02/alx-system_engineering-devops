# fixing internal server error bug

package { 'apache2':
  ensure  => installed,
}
# make sure the wp-settings.php has the correct extensions

exec { 'correct-phpp-php':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin', '/usr/bin'],
  onlyif  => 'grep -q "phpp" /var/www/html/wp-settings.php',
}

