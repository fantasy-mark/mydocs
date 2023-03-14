[TOC]

> 基本语法 `$$` 公式 `$$`

### 常用符号

##### 上下标、正负无穷

* $x^2$ : `x^2`

* $y_1$ : `y_1`
* $\infty$ : `\infty`

---

##### 加减乘除，根号，省略号

$a+b-c*d$ : `a+b-c*d`

$a\div{b}$ : `a\div{b}`

$a\pm{b}$ : `a\pm{b}`

$\frac{a}{b}$ : `\frac{a}{b}`

$\cdots$ : `\cdots`

---

##### 三角函数

$\sin{\theta}$ : `\sin{\theta}`

$\cos{\theta}$ : `\cos{\theta}`

$\tan{\theta}$ : `\tan{\theta}`

---

##### 矢量、累加累乘、极限

$\vec{F}$ : `\vec{F}`

$\sum_{i=1}^{n}a_i$ : `\sum_{i=1}^{n}a_i`

$\prod_{i=1}^na_i$ : `\prod_{i=1}^{n}a_i`

$\lim_{a\rightarrow+\infty}{a+b}$ : `\lim_{a\rightarrow+\infty}{a+b}`

---

##### 关系运算符

$\le$ : `\le`

$\ge$ : `\ge`

---

##### 希腊字母

$\alpha$ : `\alpha`

$\beta$ : `\beta`

$\gamma$ : `\gamma`

$\delta$ : `\delta`

$\epsilon$ : `\epsilon`

$\varepsilon$ : `\varepsilon`

$\eta$ : `\eta`

$\theta$ : `\theta`

$\kappa$ : `\kappa`

$\iota$ : `\iota`

$\zeta$ : `\zeta`

$\lambda$ : `\lambda`

$\mu$ : `\mu`

$\phi$ : `\phi`

$\pi$ : `\pi`

$\rho$ : `\rho`

$\xi$ : `\xi`

$\nu$ : `\nv`

$\varphi$ : `\varphi`

$\chi$ : `\chi`

$\psi$ : `\psi`

$\omega$ : `\omega`

---

### 矩阵

##### 简单矩阵

```latex
\begin{matrix}
1 & 2 \\
4 & 5
\end{matrix}
```

$$
\begin{matrix}
1 & 2 \\
4 & 5
\end{matrix}
$$

---

##### 小括号

```latex
\left(
\begin{matrix}
1 & 2 \\
4 & 5
\end{matrix}
\right)\tag{2}
```

$$
\left(
\begin{matrix}
1 & 2 \\
4 & 5
\end{matrix}
\right)\tag{2}
$$



---

##### 中、大括号

```latex
\begin{bmatrix}
1 & 2 \\
4 & 5
\end{bmatrix}
```

$$
\begin{bmatrix}
1 & 2 \\
4 & 5
\end{bmatrix}
$$

```latex
\begin{Bmatrix}
1 & 2 \\
4 & 5
\end{Bmatrix}\tag{5}
```

$$
\begin{Bmatrix}
1 & 2 \\
4 & 5
\end{Bmatrix}\tag{5}
$$

---

##### 包含希腊字母和省略号

```latex
\left\{
 \begin{matrix}
 1      & 2        & \cdots & 5        \\
 6      & 7        & \cdots & 10       \\
 \vdots & \vdots   & \ddots & \vdots   \\
 \alpha & \alpha+1 & \cdots & \alpha+4 
 \end{matrix}
 \right\}
```

$$
\left\{
 \begin{matrix}
 1      & 2        & \cdots & 5        \\
 6      & 7        & \cdots & 10       \\
 \vdots & \vdots   & \ddots & \vdots   \\
 \alpha & \alpha+1 & \cdots & \alpha+4 
 \end{matrix}
 \right\}
$$

---

### 表格

##### 简易表格

```latex
\begin{array}{|c|c|c|}
	\hline 2&9&4\\
	\hline 7&5&3\\
	\hline 6&1&8\\
	\hline
\end{array}
```

$$
\begin{array}{|c|c|c|}
	\hline 2&9&4\\
	\hline 7&5&3\\
	\hline 6&1&8\\
	\hline
\end{array}
$$

---

##### 真值表

```latex
\begin{array}{cc|c}
	       A&B&F\\
	\hline 0&0&0\\
	       0&1&1\\
	       1&0&1\\
	       1&1&1\\
\end{array}
```

$$
\begin{array}{cc|c}
	       A&B&F\\
	\hline 0&0&0\\
	       0&1&1\\
	       1&0&1\\
	       1&1&1\\
\end{array}
$$

---

##### 多行等式对齐

```latex
\begin{aligned}
a &= b + c \\
  &= d + e + f
\end{aligned}
```

$$
\begin{aligned}
a &= b + c \\
  &= d + e + f
\end{aligned}
$$

---

### 方程式、条件表达式

##### 方程式

```latex
\begin{cases}
3x + 5y +  z \\
7x - 2y + 4z \\
-6x + 3y + 2z
\end{cases}
```

$$
\begin{cases}
3x + 5y +  z \\
7x - 2y + 4z \\
-6x + 3y + 2z
\end{cases}
$$

---

##### 表达式

```latex
f(n) =
\begin{cases} 
n/2,  & \text{if }n\text{ is even} \\
3n+1, & \text{if }n\text{ is odd}
\end{cases}
```

$$
f(n) =
\begin{cases} 
n/2,  & \text{if }n\text{ is even} \\
3n+1, & \text{if }n\text{ is odd}
\end{cases}
$$

---

### 补充

**紧贴 + 无空格 + 小空格 + 中空格 + 大空格 + 真空格 + 双真空格**

```latex
a\!b + ab + a\,b + a\;b + a\ b + a\quad b + a\qquad b
```

$$
a\!b + ab + a\,b + a\;b + a\ b + a\quad b + a\qquad b
$$

