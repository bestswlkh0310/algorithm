-- 코드를 작성해주세요
SELECT 
  e.ID,
  CASE 
    WHEN e.PER <= 0.25 THEN 'CRITICAL'
    WHEN e.PER <= 0.5 THEN 'HIGH'
    WHEN e.PER <= 0.75 THEN 'MEDIUM'
    ELSE 'LOW'
  END AS COLONY_NAME
FROM (SELECT ID, PERCENT_RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS PER FROM ECOLI_DATA) e
ORDER BY e.ID