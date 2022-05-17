# Write your MySQL query statement below
SELECT email from (SELECT email, COUNT(email) as c from Person GROUP BY email HAVING c >= 2) AS T;