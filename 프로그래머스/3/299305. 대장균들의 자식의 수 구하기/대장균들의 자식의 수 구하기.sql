-- 코드를 작성해주세요
SELECT e1.ID, COUNT(e2.PARENT_ID) AS CHILD_COUNT FROM ECOLI_DATA e1 -- e1: Parent
LEFT JOIN ECOLI_DATA e2 ON e2.PARENT_ID = e1.ID -- e2: Child
GROUP BY e1.ID