# change the soft limit of open files in the OS
exec {'change limit soft':
  command  => "sudo sed -i 's/holberton soft nofile 4/holberton soft nofile 8192/g'  /etc/security/limits.conf",
  provider => shell
}

# change the hard limit of open files in the OS
exec {'change limit hard':
  command  => "sudo sed -i 's/holberton hard nofile 5/holberton hard nofile 65535/g'  /etc/security/limits.conf",
  provider => shell
}
