-- Last updated: 8/6/2026, 11:15:19 PM
# Write your MySQL query statement below
SELECT email FROM Person
GROUP BY email
HAVING COUNT(email)>1;