# kills process killmenow
exec {
  path => '/usr/bin'
  command => 'pkill -f killmenow'
}
