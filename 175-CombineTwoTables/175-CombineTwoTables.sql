-- Last updated: 7/17/2026, 11:58:06 AM
# Write your MySQL query statement below
SELECT b.firstName,
       b.lastName,
       a.city,
       a.state 
from Person b left outer join Address a 
on b.personId=a.personId;