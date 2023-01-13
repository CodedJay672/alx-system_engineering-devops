# puppet script that edits the ssh_config file

exec { 'echo':
  command => '/usr/bin/echo "    IdentityFile ~/.ssh/school\n    PasswordAuthentication no" >> /etc/ssh/ssh_config'
}
