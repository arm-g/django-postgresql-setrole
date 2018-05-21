# django-postgresql-setrole
This module is a good solution in case you have more than one user in your database and they all do read/write operations in the same database. So not have conflict it is a good practice to have one role lets say `ROLE_A` and the rest inherit the rights of `ROLE_A` and in case there is a need to create new object in db it should be done as `ROLE_A`. In postgres it can be done using `SET ROLE` command.