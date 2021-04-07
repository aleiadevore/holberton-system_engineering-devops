# /etc/puppet/manifests/nginx.pp
include nginx
nginx::resource::server { 'aleiadevore.tech':
  listen_port => 80,
}
