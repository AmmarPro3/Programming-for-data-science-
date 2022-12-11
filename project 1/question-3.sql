```
question set 1

                Question 3:
                    provide a table with the family-friendly film category, each of the quartiles, and the 
                    corresponding count of movies within each combination of film category for each 
                    corresponding rental duration category. The resulting table should have three columns:

                       - Category
                       - Rental length category
                       - Count

```

WITH t1
AS (SELECT
  title,
  c.name,
  NTILE(4) OVER (ORDER BY f.rental_duration) AS standard_quartile
FROM category c
JOIN film_category fc
  ON c.category_id = fc.category_id
JOIN film f
  ON f.film_id = fc.film_id
WHERE name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music'))

SELECT
  t1.name,
  t1.standard_quartile,
  COUNT(t1.title)
FROM t1
GROUP BY 1,
         2
ORDER BY 1, 2;

