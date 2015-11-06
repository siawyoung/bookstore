# Environment

Start local MySQL instance running and make sure you have a database created:

```
CREATE DATABASE bookstore_dev;
```

Add `.env` to the root of the project with the following (example) settings:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=1234
```