# Define class for holberton user setup
class holberton_user_setup {
  
  # Create holberton user
  user { 'holberton':
    ensure => present,
    home   => '/home/holberton',
    shell  => '/bin/bash',
  }

  # Set password for holberton user
  exec { 'set-holberton-password':
    command => 'passwd holberton',
    unless  => 'grep -q "^holberton:" /etc/passwd',
  }

  # Allow SSH access for holberton user
  file { '/etc/ssh/sshd_config':
    content => "AllowUsers holberton",
    notify  => Service['ssh'],
  }

  # Change ownership and permissions of files
  file { '/path/to/files':
    owner   => 'holberton',
    group   => 'holberton',
    recurse => true,
    mode    => '755',
  }
}
