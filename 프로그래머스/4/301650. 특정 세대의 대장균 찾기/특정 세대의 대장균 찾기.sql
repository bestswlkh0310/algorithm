-- 코드를 작성해주세요
SELECT e3.ID FROM ECOLI_DATA e1
LEFT JOIN ECOLI_DATA e2 ON e1.PARENT_ID IS NULL AND e1.ID = e2.PARENT_ID
LEFT JOIN ECOLI_DATA e3 ON e2.ID = e3.PARENT_ID
WHERE e2.ID IS NOT NULL AND e3.ID IS NOT NULL
ORDER BY e3.ID