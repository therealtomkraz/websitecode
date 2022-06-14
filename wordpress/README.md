# HackaBox Wordpress

Playground for WordPress hacking  and scanning

**DO NOT EXPOSE THIS TO INTERNET!**

## Installation

```
$ git clone https://github.com/vavkamil/dvwp.git
$ cd dvwp/
```

## Usage

```
$ cd dvwp/
$ ./go.sh
```

## Removal
```
$ cd dvwp/
$ ./down.sh
```


## Shell
`docker exec -ti dvwp_wordpres_1 /bin/bash`

## Interface

* [http://127.0.0.1:31337](http://127.0.0.1:31337)
* [http://127.0.0.1:31337/wp-login.php](http://127.0.0.1:31337/wp-login.php)
* [http://127.0.0.1:31338/phpmyadmin/](http://127.0.0.1:31338/phpmyadmin/)

## Credentials
* Wordpress: admin/admin
* MySQL: root/mypassword

## Vulnerabilities

Feel free to contribute with pull requests ;)

### Plugins

* [Easy Cookies Policy <= 1.6.2  -  Broken Access Control to Stored XSS
  - CVE-2021-24405

