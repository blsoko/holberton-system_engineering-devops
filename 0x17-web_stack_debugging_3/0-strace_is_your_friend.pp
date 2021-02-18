# phpp to php

exec { 'wrong php':
    command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
    path    => [ '/usr/local/bin/', '/bin/' ],
}
