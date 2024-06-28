# execute a command
exec { 'kill-killmenow':
command => 'pkill killmenow',
path    => '/usr/bin',
}

