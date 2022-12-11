```
question set 1
                
                Question 2:
                    Now we need to know how the length of rental duration of these family-friendly 
                    movies compares to the duration that all movies are rented for. 

                    Can you provide a table with the movie titles and divide them into 4 levels 
                    (first_quarter, second_quarter, third_quarter, and final_quarter) based 
                    on the quartiles (25%, 50%, 75%) of the rental duration for movies across 
                    all categories? Make sure to also indicate the category that 
                    these family-friendly movies fall into.

```

SELECT
  f.title AS film_title,
  c.name
  AS category_name,
  f.rental_duration AS rental_duration,
  NTILE(4) OVER (ORDER BY f.rental_duration) AS quartiles
FROM film f
JOIN film_category fc
  ON f.film_id = fc.film_id
JOIN category c
  ON c.category_id = fc.category_id
WHERE c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
GROUP BY 1,
         2,
         3;