SELECT 
    (public_transportation_pct > 10) AS is_high_public_transport,
    COUNT(s.customer_id) * 1.0 / COUNT(DISTINCT c.customer_id) AS sales_per_customer 
FROM customers c
INNER JOIN public_transportation_by_zip t ON t.zip_code = c.postal_code
LEFT JOIN sales s ON s.customer_id = c.customer_id
WHERE public_transportation_pct >= 0
GROUP BY 1
;

