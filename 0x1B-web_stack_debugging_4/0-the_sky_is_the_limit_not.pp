class apache_traffic_increase {
  package { 'apache2':
    ensure => installed,
  }

  service { 'apache2':
    ensure => running,
    enable => true,
    require => Package['apache2'],
  }

  file { '/etc/apache2/sites-available/default':
    content => "MaxClients 150\n", # Adjust the value as needed
    notify => Service['apache2'],
  }
}

