#!/bin/sh
while true; do
    read -p "!!!STOP!!! This will drop current DATABASE. Don't forget to create BACKUP! Type y or n:" yn
    case $yn in
        [Yy]* ) docker-compose -f docker-compose.prod.yml down; docker volume rm remote_postgres_data; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
