FIND WHAT DEFAULT DATABASE IS

```sql
SELECT sp.name, sp.default_database_name
FROM sys.server_principals sp
WHERE sp.name = SUSER_SNAME();
```

MODIFY DEFAULT DATABASE
```sql
ALTER LOGIN ldaijiw WITH DEFAULT_DATABASE = db_name;
```

sqlcmd command to connect to server

```
sqlcmd -S servername -U username -P password
```


servername: ldaijiw-micro.cdix33vx1qyf.eu-west-2.rds.amazonaws.com
