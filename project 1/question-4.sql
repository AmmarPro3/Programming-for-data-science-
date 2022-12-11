```
my own question 

                Question 4:
                    Who are the top 10 buying customers in 2007?

```

WITH t1
AS (SELECT
  c.customer_id,
  SUM(p.amount) AS total_payments
FROM customer c
JOIN payment p
  ON p.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY total_payments DESC
LIMIT 10)

SELECT
  DATE_TRUNC('month', payment_date) AS pay_mon,
  CONCAT(first_name, ' ', last_name) AS full_name,
  SUM(p.amount) AS payment_amount
FROM t1
JOIN customer c
  ON t1.customer_id = c.customer_id
JOIN payment p
  ON p.customer_id = c.customer_id
WHERE payment_date BETWEEN '2007-01-01' AND '2007-12-30'
GROUP BY 1,
         2
ORDER BY 2, 1;

