# increased the number of ulimit set only if it is less than 15 

exec { 'set_ulimit':
    command => '/bin/sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4000\"/" /etc/default/nginx',
    onlyif  => '/bin/grep -q "ULIMIT=\"-n 15\"" /etc/default/nginx',
    notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
    command     => '/usr/sbin/service nginx restart',
    refreshonly => true,
}
