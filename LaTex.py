#!/usr/bin/env python
# coding: utf-8

# In[9]:


from IPython.display import Latex


# In[10]:


# 数学公式的前后要加上 $ 或 \( 和 \)
Latex(r"$f(x) = 3x + 7$")


# In[11]:


# 普通字符在数学公式中含义一样，除了 # $ % & ~ _ ^ \ { }
# 若要在数学环境中表示这些符号# $ % & _ { }，
# 需要分别表示为\# \$ \% \& \_ \{ \}，即在个字符前加上\
# 上标和下标
# 用 ^ 来表示上标，用 _ 来表示下标
# 如果有多个字符做上标或下标，要用{}括起来
Latex(r"$\sum_{i=1}^n a_i=0$")


# In[16]:


Latex(r"$f(x)=x^{x^x}$")


# In[13]:


# 希腊字母
# 大写希腊字母
Latex(r"$\Gamma \Delta \Theta \Lambda \Xi \Pi \Sigma \Upsilon$")


# In[14]:


Latex(r"$\Phi \Psi \Omega$")


# In[15]:


# 小写希腊字母
Latex(r"$\alpha \beta \gamma \delta \epsilon \varepsilon \zeta \eta$")


# In[17]:


Latex(r"$\theta \vartheta \iota \kappa \lambda \mu \nu \xi$")


# In[18]:


Latex(r"$o \pi \varpi \rho \varrho \sigma \varsigma \tau$")


# In[19]:


Latex(r"$\upsilon \phi \varphi \chi \psi \omega$")


# In[20]:


# 大尺寸运算符
Latex(r"$\sum \prod \coprod \int \iint \iiint \oint$")


# In[21]:


Latex(r"$ \bigvee \bigwedge \bigoplus \bigotimes \bigodot \biguplus$")


# In[22]:


# 箭头
Latex(r"$\leftarrow \rightarrow \Leftarrow \Rightarrow \uparrow \downarrow$")


# In[23]:


Latex(r"$\nearrow \searrow \swarrow \nwarrow \leadsto$")


# In[24]:


Latex(r"$ \iff \rightleftharpoons$")


# In[25]:


# 在公式中插入文本可以通过 \mbox{text} 在公式中添加text
Latex(r"$\mbox{对任意的$x>0$}, \mbox{有 }f(x)>0. $")


# In[27]:


# 分数及开方
# \frac{numerator}{denominator} \sqrt{expression_r_r_r}表示开平方，
# \sqrt[n]{expression_r_r_r} 表示开 n 次方
Latex(r"$\frac{7x+5}{1+y^2} \sqrt{x^2+y^2} \sqrt[n]{x^n+y^n}$")


# In[28]:


# 省略号（3个点）
# \ldots 表示跟文本底线对齐的省略号；\cdots 表示跟文本中线对齐的省略号
Latex(r"$ f(x_1,x_x,\ldots,x_n)=x_1^2+x_2^2+\cdots+x_n^2 $")


# In[29]:


# 省略号（3个点）
# \ldots 表示跟文本底线对齐的省略号；\cdots 表示跟文本中线对齐的省略号
Latex(r"$ f(x_1,x_x,\ldots,x_n)=x_1^2+x_2^2+\cdots+x_n^2 $")


# In[30]:


# 省略号（3个点）
# \ldots 表示跟文本底线对齐的省略号；\cdots 表示跟文本中线对齐的省略号
Latex(r"$ f(x_1,x_x,\ldots,x_n)=x_1^2+x_2^2+\cdots+x_n^2 $")


# In[31]:


# 括号和分隔符
#() 和 [ ] 和 ｜ 对应于自己；
#{} 对应于 \{ \}；
#|| 对应于 \|。
#当要显示大号的括号或分隔符时，要对应用 \left 和 \right
Latex(r"$f(x,y,z)=3y^2z\left(3+\frac{7x+5}{1+y^2}\right). $")


# In[32]:


# \left. 和 \right. 只用与匹配，本身是不显示的
Latex(r"$\left. \frac{du}{dx} \right|_{x=0}.$")


# In[33]:


# 多行的数学公式
# 其中&是对其点，表示在此对齐。
# *使latex不自动显示序号，如果想让latex自动标上序号，则把*去掉
Latex(r"""\begin{eqnarray*}
\cos 2\theta & = & \cos^2 \theta - \sin^2 \theta \\
& = & 2 \cos^2 \theta - 1.
\end{eqnarray*}""")


# In[35]:


#矩阵
# c表示向中对齐，l表示向左对齐，r表示向右对齐
Latex(r"""The \emph{characteristic polynomial} $\chi(\lambda)$ of the
$3 \times 3$~matrix
\[ \left( \begin{array}{ccc}
a & b & c \\
d & e & f \\
g & h & i \end{array} \right)\]
is given by the formula
\[ \chi(\lambda) = \left| \begin{array}{ccc}
\lambda - a & -b & -c \\
-d & \lambda - e & -f \\
-g & -h & \lambda - i \end{array} \right|.\]""")


# In[36]:


# 导数、极限、求和、积分
Latex(r"$\frac{du}{dt} and \frac{d^2 u}{dx^2}$")


# In[37]:


# 偏导数
Latex(r"""\[ \frac{\partial u}{\partial t}
= h^2 \left( \frac{\partial^2 u}{\partial x^2}
+ \frac{\partial^2 u}{\partial y^2}
+ \frac{\partial^2 u}{\partial z^2}\right)\]""")


# In[38]:


Latex(r"$\lim_{x \to +\infty}, \inf_{x > s}$")


# In[39]:


# 极限
Latex(r"\[ \lim_{x \to 0} \frac{3x^2 +7x^3}{x^2 +5x^4} = 3.\]")


# In[40]:


# 求和
Latex(r"\[ \sum_{k=1}^n k^2 = \frac{1}{2} n (n+1).\]")


# In[41]:


# 积分
# To obtain the correct appearance one 
# should put extra space before the d, using \,
Latex(r"\[ \int_a^b f(x)\,dx.\]")


# In[42]:


Latex(r"\[ \int_0^{+\infty} x^n e^{-x} \,dx = n!.\]")


# In[43]:


Latex(r"\[ \int \cos \theta \,d\theta = \sin \theta.\]")


# In[44]:


Latex(r"""\[ \int_{x^2 + y^2 \leq R^2} f(x,y)\,dx\,dy
= \int_{\theta=0}^{2\pi} \int_{r=0}^R
f(r\cos\theta,r\sin\theta) r\,dr\,d\theta.\]""")


# In[45]:


Latex(r"\[ \int_0^R \frac{2x\,dx}{1+x^2} = \log(1+R^2).\]")


# In[46]:


# The way to improve the appearance of 
# of the integral is to use the control sequence \! 
# to remove a thin strip of unwanted space
Latex(r"\[ \int_0^1 \! \int_0^1 x^2 y^2\,dx\,dy.\]")


# In[47]:


Latex(r"\[ \int_0^1 \int_0^1 x^2 y^2\,dx\,dy.\]")


# In[ ]:




