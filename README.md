# Getting Started
`django-postgresql-setrole` module sets `SET ROLE` statement in every connection to Postgres.
This module is a good solution in case you have more than one user(role) in your database and they all do read/write operations in the same database. In postgres `role` inheritance is one directional and `Postgres` will not let you set up circular membership loops. Learn more about role inheritance constraints in `Postgres` [here](https://www.postgresql.org/docs/current/static/role-membership.html)
So not have conflict it is a good practice to have one role lets say `ROLE_A` and the rest inherit the rights of `ROLE_A` and in case there is a need to create new object in db it should be done as `ROLE_A`. In postgres it can be done using `SET ROLE` command unless we don't want to have a database and a lot of ownerships in it (different tables with different owners etc.).

# Prerequisites
Python 2.7.*

# Installing
1) Add `postgresql_setrole` to `INSTALLED_APPS`
2) Add `SET_ROLE` in your database connection. 
E.g.  
```DATABASES = {
    "default": {
        ...,  # other settings
        "SET_ROLE": "owner",
    }.
}
```
# Licence
This project is licensed under the MIT License - see the LICENSE.md file for details

# Acknowledgments
Feel free to contact us and share your experience.

