-- 코드를 입력하세요
SELECT 
  i.REST_ID, 
  i.REST_NAME, 
  i.FOOD_TYPE, 
  i.FAVORITES, 
  i.ADDRESS,
  ROUND(AVG(r.REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO i
LEFT JOIN REST_REVIEW r ON i.REST_ID = r.REST_ID
WHERE i.ADDRESS LIKE '서울%'
GROUP BY i.REST_NAME HAVING COUNT(r.REST_ID) > 0
ORDER BY SCORE DESC, i.FAVORITES DESC