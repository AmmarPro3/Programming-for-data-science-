```
question set 1

                Question 1:
                    We want to understand more about the movies that families are watching. The following categories are 
                    considered family movies: Animation, Children, Classics, Comedy, Family and Music.

                    Create a query that lists each movie, the film category it is classified in, and the number of 
                    times it has been rented out.
```

WITH t1 AS (select f.title AS film_title, c.name AS category_name
FROM film f
JOIN film_category fc
ON f.film_id = fc.film_id
JOIN category c
ON c.category_id = fc.category_id
WHERE c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
ORDER BY 2,1),

t2 AS (select f.title AS film_title, COUNT(r.*) AS rental_count
FROM film f
JOIN inventory i
ON f.film_id = i.film_id
JOIN rental r
ON i.inventory_id = r.inventory_id
GROUP BY 1)

SELECT t1.film_title, t1.category_name, t2.rental_count
FROM t1
JOIN t2
ON t1.film_title = t2.film_title
ORDER BY 2,1;