# Udacity SQL Project

This program was written to complete the 'Logs Analysis' project for 
Udacity's 'Full Stack Developer' course. It works by using the postgresql
Python library to make three queries to a given database. The three results
are then printed.

To run in the commandline, just do:

```
python newsdata.py
```

The 'news' database must be present.

The output should look as follows:

```
Top articles:
"Candidate is jerk, alleges rival" -- 338647 views
"Bears love berries, alleges bear" -- 253801 views
"Bad things gone, say good people" -- 170098 views
"Goats eat Google's lawn" -- 84906 views
"Trouble for troubled troublemakers" -- 84810 views
"Balloon goons doomed" -- 84557 views
"There are a lot of bears" -- 84504 views
"Media obsessed with bears" -- 84383 views
-----
Top authors:
Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views
-----
Days with more than 1% of requests being errors:
July 17, 2016 -- 2.26%
```
