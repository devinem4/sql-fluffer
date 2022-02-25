# sql-fluffer

https://dashboard.heroku.com/apps/sql-fluffer

### dev notes

```
$ uvicorn app.main:app --reload
```

### disabling linter on specific lines

```sql
a.a*a.b AS bad_1  -- noqa: L006
```

```sql
-- Ignore rule L012 from this line forward
SELECT col_a a FROM foo -- noqa: disable=L012

-- Ignore all rules from this line forward
SELECT col_a a FROM foo -- noqa: disable=all

-- Enforce all rules from this line forward
SELECT col_a a FROM foo -- noqa: enable=all
```
