import psycopg2

dhand = psycopg2.connect("dbname=news")
curs = dhand.cursor()

# The three SQL queries are kept in the strings
# 'q_articles', 'q_authors', & 'q_errors'.

# q_articles is for the top articles of all time.
q_articles =  \
    """
    select articles.title, count(*) as num from articles, log
        where log.path like '%' || articles.slug
        group by articles.title
        order by num desc;
    """

# q_authors is for the most popular authors of all time.
q_authors =  \
    """
    select authors.name, count(*) as num from articles, log, authors
        where log.path like '%' || articles.slug
        and articles.author = authors.id
        group by authors.name
        order by num desc;
    """

# q_errors is for the days more than 1% of requests led to errors.
q_errors =  \
    """
    select a.date, errors, requests from
        (select date(time) as date, count(*) as errors from log
            where status like '4%'
            or status like '5%'
            group by date
        ) as a,
        (select date(time) as date, count(*) as requests from log
            group by date
        ) as b
        where a.date = b.date
        and cast(errors as decimal) / requests > 0.01;
    """

# Get and print the top articles.

curs.execute(q_articles)
articles = curs.fetchall()

print("Top articles:")
for title, num in articles:
    print('"'+title+'"'+' -- '+str(num)+' views')
print("-----")

# Get and print the top authors.

curs.execute(q_authors)
authors = curs.fetchall()

print("Top authors:")
for author, num in authors:
    print(author+' -- '+str(num)+' views')
print("-----")

# Get and print days with > 1% errors.

curs.execute(q_errors)
errors = curs.fetchall()

print("Days with more than 1% of requests being errors:")
for day, error, requests in errors:
    pretty_date = str(day.strftime("%B %d, %Y"))
    percent_error = round(error/float(requests)*100, 2)
    print(pretty_date+' -- '+str(percent_error)+'%')

curs.close()
