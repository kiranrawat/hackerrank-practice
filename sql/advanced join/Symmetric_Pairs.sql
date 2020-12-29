select f1.X, f1.Y
from Functions as f1
inner join Functions as f2 
on f1.X = f2.Y AND f1.Y=f2.X
GROUP BY f1.X, f1.Y
HAVING COUNT(f1.X)>1 or f1.X<f1.Y
ORDER BY f1.X 