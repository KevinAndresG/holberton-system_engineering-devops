# fixing the apache sintax
exec {'Fix an apache server':
  command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path    => '/usr/bin:/usr/sbin:/bin'
}
