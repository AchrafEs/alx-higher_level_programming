`0x0D-SQL_introduction`

SQL, which stands for Structured Query Language, is a domain-specific programming language designed for managing and
manipulating relational databases. It serves as the standard language for interacting with databases, enabling users to
create, modify, retrieve, and manage data stored in a structured manner.

Here's a breakdown of the key components and concepts of SQL:

1. `Databases and Tables:` A database is a collection of organi zed data. Within a database, data is stored in tables,
which are structured sets of rows and columns. Each table represents a specific entity or concept.

2. `Queries:` SQL is primarily used to write queries, which are instructions that you provide to the database to retrieve
or manipulate data. Queries are formulated using SQL statements.

3. `SQL Statements:` SQL consists of various types of statements, each serving a distinct purpose:

`SELECT:` Used to retrieve data from one or more tables. It is the foundation of querying and retrieving information from databases.

`INSERT:` Used to add new records (rows) into a table.

`UPDATE:` Used to modify existing records in a table.

`DELETE:` Used to remove records from a table.

`CREATE:` Used to create new databases and tables.

`ALTER:`Used to modify the structure of existing tables (e.g., add, modify, or delete columns).

`DROP:` Used to delete databases and tables.

`JOIN:` Used to combine data from multiple tables based on related columns.

`GROUP BY:` Used to group rows based on certain columns and perform aggregate functions (e.g., SUM, AVG, COUNT) on those
groups.

`ORDER BY:` Used to sort the result set based on one or more columns.

`WHERE:` Used to filter rows based on specified conditions.

`HAVING:` Used to filter groups resulting from the GROUP BY clause.

4. `Clauses:` SQL statements are often composed of various clauses that provide additional instructions or conditions. For
example, the SELECT statement can include clauses like WHERE, GROUP BY, HAVING, and ORDER BY to refine the results.

5. `Data Types:` Each column in a table has a data type that specifies the kind of data it can store, such as integers,
strings, dates, and more.

6. `Normalization:` This is a database design concept that involves organizing tables and data to reduce data redundancy
and maintain data integrity.

7. `Indexes:` Indexes are structures that improve the speed of data retrieval operations by providing a faster way to look
up data based on specific columns.

8. `Transactions:` A transaction is a sequence of SQL statements executed as a single unit of work. Transactions ensure
data consistency and integrity in the database.

9. `ACID Properties:` ACID stands for Atomicity, Consistency, Isolation, and Durability. These properties ensure that
database transactions are reliable and maintain data integrity.

10. `Views:` A view is a virtual table created by executing a SELECT statement. It allows you to simplify complex queries
and restrict access to certain data.

SQL is widely used by software developers, data analysts, database administrators, and other professionals working with
databases. It's supported by most relational database management systems (RDBMS), such as MySQL, PostgreSQL, Microsoft SQL Server, Oracle Database, and SQLite.
