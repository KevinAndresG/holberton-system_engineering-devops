# install the puppet-lint
package { 'puppet-lint':
  ensure => 'installed',
  name => 'puppet-lint',
  provider => 'gem',
  install_options => ['-v 2.5.0'],
}
