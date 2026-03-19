点云拟合
============================

发布日期：2026-03-20

直线拟合
------------------------
直线方程可以由$x = td + p$表示，其中d是单位长度的方向向量，p是直线上的一点。
我们可以通过最小二乘法来拟合直线：点到直线的距离的平方和最小。

$$
L = \\sum_{i=1}^n \\lvert x_i - p \\rvert^2 - ((x_i - p)^T d)^2
$$
求解的问题就是
$$
\\min_{d, p} L
$$

我们可以通过求导来求解d和p。

$$
\\frac{\\partial L}{\\partial p} = 0
$$

$$
\\begin{aligned}
dL
&= \\sum_{i=1}^n 2 (x_i - p)^T \\mathrm{d}(x_i - p) - 2 (x_i - p)^T d \\cdot \\mathrm{d}\\!\\left((x_i - p)^T d\\right) \\\\
&= \\sum_{i=1}^n -2 (x_i - p)^T \\mathrm{d}p + 2 (x_i - p)^T d \\cdot d^T \\mathrm{d}p \\\\
&= (2\\sum_{i=1}^n (x_i - p)^T (d \\cdot d^T - I)) \\mathrm{d}p 
\\end{aligned}
$$
由于$ dL =(\\frac{\\partial L}{\\partial p})^T \\mathrm{d}p $ ，所以有
$$ \\frac{\\partial L}{\\partial p} =2(d \\cdot d^T - I)\\sum_{i=1}^n (x_i - p) = 0 $$

故有
$$ p = \\frac{1}{n}\\sum_{i=1}^n x_i $$

平面拟合
------------------------

