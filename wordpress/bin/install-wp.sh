#!/usr/bin/env sh

# Install WordPress.

wp core install \
  --title="hackabox" \
  --admin_user="admin" \
  --admin_password="admin" \
  --admin_email="admin@example.com" \
  --url="http://192.168.10.164:8008/" \
  --skip-email\

# Update permalink structure.
# wp option update permalink_structure "/%year%/%monthnum%/%postname%/" --skip-themes --skip-plugins

# Activate plugin.
#wp plugin activate iwp-client 
#wp plugin activate social-warfare 
#wp plugin activate wp-advanced-search 
#wp plugin activate wp-file-upload 
wp plugin activate easy-cookies-policy
# wp plugin activate wp-time-capsule # Causes error

# Update DB
# wp db import dump.sql

#Add a user
wp user create bob bob@example.com --role=author --user_pass="letmein"
