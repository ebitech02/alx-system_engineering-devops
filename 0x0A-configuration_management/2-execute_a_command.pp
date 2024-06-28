exec { 'kill killmenow process':
command   => 'pkill -f killmenow',
onlyif    => 'pgrep -f killmenow',
path      => ['/bin', '/usr/bin'],
}

