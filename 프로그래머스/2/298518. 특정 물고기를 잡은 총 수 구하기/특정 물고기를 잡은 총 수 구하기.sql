-- 코드를 작성해주세요
SELECT COUNT(*) AS FISH_COUNT FROM FISH_INFO f
LEFT JOIN FISH_NAME_INFO n ON f.FISH_TYPE = n.FISH_TYPE
WHERE n.FISH_NAME IN ('BASS', 'SNAPPER')