select ROUND(abs(min(LAT_N) -  MAX(LAT_N)) + abs(min(LONG_W) - MAX(LONG_W)), 4)
FROM STATION 
