docker run -d -p 5000:5000 \
    -e MYSQL_DATABASE_USER=root \
    -e MYSQL_DATABASE_PASSWORD=password \
    -e MYSQL_DATABASE_DB=userdb \
    -e MYSQL_DATABASE_HOST=host.docker.internal \
    diptichoudhary/manage-user:0.1