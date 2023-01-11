# puppet manifest that runs a kill command

exec { 'kill_cmd':
  command  => '/bin/pkill -f killmenow'
}
