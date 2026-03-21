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

另外，沿着直线方向平移基点不会改变目标函数，即对任意 $t \\in \\mathbb{R}$，
$$
p' = p + t d \\quad \\Rightarrow \\quad L(p', d) = L(p, d).
$$
完整展开证明见文末“补充材料”。

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

注意到 $d$ 是单位向量，且
$$
\\mathrm{Null}(d d^T - I) = \\mathrm{span}(d).
$$
该结论证明见文末“补充材料”。
因此由
$$
(d d^T - I)\\sum_{i=1}^n (x_i - p) = 0
$$
可知
$$
\\sum_{i=1}^n (x_i - p) = \\lambda d
$$
其中 $\\lambda \\in \\mathbb{R}$。等价地，
$$
p = \\frac{1}{n}\\sum_{i=1}^n x_i + t d, \\quad t \\in \\mathbb{R}.
$$
也就是说，$p$ 在与 $d$ 正交的平面上的投影等于样本均值的对应投影；沿 $d$ 方向存在一维自由度。

平面拟合
------------------------

补充材料
------------------------

沿直线移动不改变 $L$ 的证明
~~~~~~~~~~~~~~~~~~~~~~~~~~~

令
$$
p' = p + t d,
$$
则
$$
\\begin{aligned}
L'
&= \\sum_{i=1}^n \\left(\\lvert x_i - p' \\rvert^2 - ((x_i - p')^T d)^2\\right) \\\\
&= \\sum_{i=1}^n \\left(\\lvert (x_i - p) - t d \\rvert^2 - \\left(((x_i - p)^T d) - t\\right)^2\\right) \\\\
&= \\sum_{i=1}^n \\left(\\lvert x_i - p \\rvert^2 - 2t (x_i - p)^T d + t^2 - \\left((x_i - p)^T d\\right)^2 + 2t (x_i - p)^T d - t^2\\right) \\\\
&= \\sum_{i=1}^n \\left(\\lvert x_i - p \\rvert^2 - ((x_i - p)^T d)^2\\right) = L.
\\end{aligned}
$$
因此，$p$ 只在法向平面上的分量会影响 $L$，沿 $d$ 方向的分量不可辨识。

$d d^T - I$ 的零空间证明
~~~~~~~~~~~~~~~~~~~~~~~~

要证
$$
\\mathrm{Null}(d d^T - I) = \\mathrm{span}(d).
$$

对任意向量 $v$，若 $(d d^T - I)v = 0$，则
$$
d(d^T v) = v,
$$
从而
$$
v = (d^T v)d \\in \\mathrm{span}(d).
$$

反之，若 $v = \\alpha d$，则
$$
(d d^T - I)v = (d d^T - I)\\alpha d = \\alpha(d(d^T d) - d) = 0
$$
（利用 $d^T d = 1$）。

故得
$$
\\mathrm{Null}(d d^T - I) = \\mathrm{span}(d).
$$

$L$ 关于 $p$ 的 Hessian 分析
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在固定 $d$（且 $\\|d\\|=1$）时，梯度为
$$
\\nabla_p L = 2(d d^T - I)\\sum_{i=1}^n (x_i - p).
$$
对 $p$ 再求导，得到 Hessian
$$
\\nabla_p^2 L = 2n(I - d d^T).
$$

对任意向量 $v$，有
$$
v^T \\nabla_p^2 L\\, v = 2n\\left(\\|v\\|^2 - (d^T v)^2\\right) \\ge 0,
$$
因此 Hessian 半正定。并且当且仅当 $v \\parallel d$ 时取等号，即零空间为 $\\mathrm{span}(d)$。

这说明：

1. 在与 $d$ 正交的子空间上，$\\nabla_p^2 L$ 正定，因此驻点是严格最小值点；
2. 沿 $d$ 方向曲率为 0，因此目标函数在该方向上是平坦的；
3. 所以 $p = \\frac{1}{n}\\sum_{i=1}^n x_i + t d$（$t\\in\\mathbb{R}$）构成一条等价最小值解集。

参考资料
------------------------

1. 高翔. *自动驾驶与机器人中的SLAM技术：从理论到实践*. 机械工业出版社, 2023. 第五章 *基础点云处理*（重点小节：5.3 *拟合问题*，包含平面拟合与直线拟合）。
