SELECT Name, SUM(Amount) AS Total FROM Salesperson
JOIN Orders ON Salesperson.ID = Orders.salesperson_id
GROUP BY Name
HAVING Total > 1300

/* OR  */

SELECT Name, SUM(Amount) AS Total FROM Salesperson, Orders
WHERE Orders.salesperson_id = Salesperson.ID
GROUP BY Name
HAVING Total > 1300
