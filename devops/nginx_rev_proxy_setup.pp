#!/usr/bin/env puppet
# manifest to install nginx and setup reverse proxy
package { 'nginx':
    ensure => 'installed',
}

service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
}

file { '/etc/nginx/sites-available/nearly-valued-leopard.ngrok-free.app':
    ensure  => 'file',
    content => template('templates/vitasync_routes.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/nearly-valued-leopard.ngrok-free.app':
    ensure => 'link',
    target => '/etc/nginx/sites-available/nearly-valued-leopard.ngrok-free.app',
    require => File['/etc/nginx/sites-available/nearly-valued-leopard.ngrok-free.app'],
    notify  => Service['nginx'],
}

exec { 'test_nginx_config':
    command => '/usr/sbin/nginx -t',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    notify  => Service['nginx'],
}
