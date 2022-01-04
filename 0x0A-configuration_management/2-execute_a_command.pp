# create a manifest that kills a process
exec {'kill a process':
  command => 'pkill killmenow',
  path    => '/usr/bin'
}
