# A manifest to debug an apache server

exec {'debug':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin'
}
