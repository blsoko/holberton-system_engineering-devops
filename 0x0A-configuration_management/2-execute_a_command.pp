#Kill a process
exec {'pkill killmenow':
    path => ['/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/'],
}