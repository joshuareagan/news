# Udacity SQL Project

## Project Description

This program was written to complete the 'Logs Analysis' project for 
Udacity's 'Full Stack Developer' course. Given `newsdata.sql` (not 
included in this repo), one generates the `news` database. Then 3
queries are to be run on this database and the results displayed:

1. The top 3 articles viewed.
1. The top authors.
1. All days in which the percentage of requests is more than 1% errors.

## Dependencies

The program uses postgresql, so you will need the `psycopg2` python 
library. You also need the initial `newsdata.sql` file, not included 
in this repo. (It's given as part of the assignment.)

## Setup

You can install the program by cloning the repo:

```
git clone https://github.com/joshuareagan/news.git
```

You'll also need to create the `news` database from `newsdata.sql` as
follows:

```
psql -d news -f newsdata.sql
```

## Usage

To run the program:

```
python newsdata.py
```

The output should look as follows:

```
Top articles:
  Candidate is jerk, alleges rival -- 338647 views
  Bears love berries, alleges bear -- 253801 views
  Bad things gone, say good people -- 170098 views
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
