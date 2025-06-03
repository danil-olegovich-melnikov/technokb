query = """
WITH product_summary AS (
  SELECT 
      p.action, 
      p.product_id, 
      SUM(p.count * CASE WHEN p.action = 'Приход' THEN 1 ELSE -1 END) AS count, 
      SUM(p.price * p.count * CASE WHEN p.action = 'Приход' THEN 1 ELSE 0 END) AS total 
  FROM product_transaction p
  GROUP BY p.product_id, p.action
),  
product_avg AS (
  SELECT *, 
         CASE WHEN count <> 0 THEN total / count ELSE NULL END AS avg 
  FROM product_summary
),  
p1 AS (
  SELECT 
      pa.action, 
      pa.product_id, 
      pa.count, 
      ROUND(COALESCE(
          (SELECT ps.avg 
           FROM product_avg ps 
           WHERE ps.product_id = pa.product_id AND ps.action = 'Приход'
           LIMIT 1), 
          pa.avg
      )) AS avg
  FROM product_avg pa
 ),
 pc AS (
   SELECt p1.product_id, SUM(p1.count) as count, SUM(p1.count * p1.avg) as total from p1
 	GROUP BY p1.product_id
 )
SELECT p.name, c.name, pc.count, pc.total
FROM pc
LEFT JOIN product_product p ON pc.product_id = p.id
LEFT JOIN product_category c ON c.id = p.category_id
WHERE pc.count > 0
ORDER BY pc.total DESC;
"""


def get_balance():
    from django.db import connection

    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    return results[0]