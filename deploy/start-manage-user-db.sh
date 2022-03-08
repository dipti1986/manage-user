docker run -d -p 3306:3306 \
    -e MYSQL_DATABASE=userdb \
    -e MYSQL_ROOT_PASSWORD=password \
    -v $(pwd)/create_db.sql:/docker-entrypoint-initdb.d/1.sql \
    --name mysql \
    mysql