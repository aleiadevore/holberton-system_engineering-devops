# kills process killmenow
exec { 'killit':
  path    => '/usr/bin',
  command => 'pkill -f killmenow'
}
