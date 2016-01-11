如果数据库尚有活动连接，则drop数据库时会失败并有错误提示。

```sql
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'testdb' AND pid <> pg_backend_pid();
```


>
>pg_stat_activity是一个系统视图，表中的每一行代表一个服务进程的属性和状态。
>
>boolean pg_terminate_backend(pid int)是一个系统函数，用于终止一个后端服务进程。
>
>int pg_backend_pid()系统函数用于获取附加到当前会话的服务器进程的ID

恢复数据库

```sql
psql -h localhost -U postgres -d green < ~/Downloads/public.sql
```

备份数据库
```sql
pg_dump -h localhost -U postgres green > databasename.bak
```