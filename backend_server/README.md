## Database setup

```
mysql> CREATE DATABASE swiss_tournament CHARACTER SET UTF8;
Query OK, 1 row affected (0.18 sec)

mysql> CREATE USER federer@localhost IDENTIFIED BY 'password';
Query OK, 0 rows affected (0.25 sec)

mysql> GRANT ALL PRIVILEGES ON swiss_tournament.* TO federer@localhost;
Query OK, 0 rows affected (0.03 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.06 sec)

mysql> SET PASSWORD FOR 'federer'@'localhost'= PASSWORD('hello123');
Query OK, 0 rows affected (0.06 sec)

mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.03 sec)
```

## Django setup

1. Create a `virtualenv` and run the following commands within the `virtualenv`
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py createsuperuser`
5. `python manage.py runserver`

**To reset your database**, `python manage.py reset_db`


_______________

## Programming tips

0. Refer to your previous code reviews and implement suggested improvements

1. Improve the quality of your code by:
	* Striving for more elegant solutions
	* Naming variables well
	* Having small functions that do one thing really well and are testable
	* Aiming to write more idiomatic Python code
	* Following Django conventions
	* Write reusable code. 
	* See if you can place your functions within suitable modules and classes

2. Get your code reviewed after each milestone, so that the quality of your codebase improves with time. 

3. Don't resort to hacks if things don't work. Think from first principles, read tutorials, take a step back and then solve the problem with a fresh mindset.

4. Master your tools - Use Django's test framework, IPython, pdb to speed up your development workflow.

__________________
