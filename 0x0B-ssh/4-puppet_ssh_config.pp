# Changes permissions to refuse password
file_line { 'id-file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton'
}

file_line { 'aunthentication':
  path        => '/etc/ssh/ssh_config',
        match => 'PasswordAuthentication',
  line        => 'PasswordAuthentication no'
}