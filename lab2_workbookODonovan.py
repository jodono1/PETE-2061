#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/lsuhpchelp/lbrnloniworkshop2019/blob/master/day1_python/intro_python.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# 
#  #  Python Data Types
# 
# ## PETE 2061 Lab 2 Workbook 
# 
# ## THIS IS DUE BY 10:20 AM TODAY
# 
# <a id='top'></a>

# <a id='variables'></a>
# ## Decline Curve Analysis
# Wells A, B, and C flow with an initial flow rate ($q_i$) of 5,000 bopd (barrels of oil per day), and have a continuous initial decline rate ($D_i$) of 20% per year. Well A declines exponentially, while well B declines hyperbolically, with a b-exponent of 0.5, and well C declines harmonically (this means that b = 0). <br><br>

# Step 1. Import the math library (so that the exponential function is available). <br>

# In[1]:


import math


# Step 2. Create variables named q_i, D_i and b, and assign them to the given initial flow rate, initial decline rate, and hyperbolic b-exponent of 0.5, respectively. <br>

# In[20]:


q_i, D_i, b = 5000, .20, math.exp(0.5)


# Step 3. Using the list() and range() functions, create a list named t, and use it store time in years; starting from 0 to 3 years, and in increments of 1 year. The first item in list t will be 0, and the last item will be 3.<br>

# In[3]:


intRange = range(0,4,1)  #Format of range() is range(start, stop, increment). 12 is not included in range
t = list(intRange)  
print(t)
type(intRange)


# Step 4. Create a list named q_A, and fill it with four zeros. <br>

# In[4]:


q_AList = [0,0,0,0]
print(q_AList)


# Step 5. Also create lists named q_B and q_C and let them store four zeros each. Note that q_A, q_B and q_C correspond to the flow rates of wells A, B and C, respectively. <br>

# In[51]:


q_BList = [0,0,0,0]
q_CList = [0,0,0,0]


# Step 6. Using the appropriate equation for well A, 
#     (a) compute the its rate at a time of 0 years, and store it in the first index of the list, q_A. Double-check that your result for this is equal to the initial flow rate.
#     (b) compute the its rate after 1 year and store it in the second index of the list, q_A.
#     (c) compute the its rate after 2 years and store it in the third index of the list, q_A.
#     (d) compute the its rate after 3 years and store it in the fourth index of the list, q_A. <br>

# In[31]:


#𝒒 = 𝒒𝒊 𝐞𝐱𝐩(−𝑫𝒊𝒕) 
#part A
q_AList[0] = q_i*math.exp(0.5)*(-D_i*0)
print(q_AList)
#part B
q_AList[1] = q_i*math.exp(0.5)*(-D_i*1)
print(q_AList)
#part C
q_AList[2] = q_i*math.exp(0.5)*(-D_i*2)
print(q_AList)
#part D
q_AList[3] = q_i*math.exp(0.5)*(-D_i*3)
print(q_AList)


# Step 7. Print out list q_A. <br>

# In[32]:


print(q_AList)


# Step 8. Using the appropriate equation for wells B and C, compute and store the corresponding four rates in q_B and q_C. This is similar to the steps in 6 (a) through (d), but with the hyperbolic and harmonic decline curve equations, respectively. <br>

# In[55]:


# Hyperbolic equation = q_i/((1.0+b*D_i*t)**(1.0/b))
# Harmonic equation = q_i/((1.0+D_i*t) q_C[0] = q_i/((1.0+D_i*0)

q_BList[0] = q_i/((1.0+b*D_i*0)**(1.0/b))
q_BList[1] = q_i/((1.0+b*D_i*1)**(1.0/b))
q_BList[2] = q_i/((1.0+b*D_i*2)**(1.0/b))
q_BList[3] = q_i/((1.0+b*D_i*3)**(1.0/b))
print(q_BList)

q_CList[0] = q_i/((1.0+D_i*0))
q_CList[1] = q_i/((1.0+D_i*1))
q_CList[2] = q_i/((1.0+D_i*2))
q_CList[3] = q_i/((1.0+D_i*3))


# Step 9. Print out lists q_B and q_C <br>

# In[56]:


print(q_BList); print(q_CList)


# Step 10. Using all that you have learned so far, compute the corresponding cumulative production (Q_A, Q_B and Q_C) using the analytical expressions in your lecture notes. Print out the four items in each of these three lists. <br>

# In[60]:


#Corresponding cumulative production 𝑸_𝒑 = (𝒒_𝒊−𝒒)/D_𝒊
Q_A = [0,0,0,0]
Q_A[0] = (q_i - q_AList[0])/D_i
Q_A[1] = (q_i - q_AList[1])/D_i
Q_A[2] = (q_i - q_AList[2])/D_i
Q_A[3] = (q_i - q_AList[3])/D_i

Q_B = [0,0,0,0]
Q_B[0] = (q_i - q_BList[0])/D_i
Q_B[1] = (q_i - q_BList[1])/D_i
Q_B[2] = (q_i - q_BList[2])/D_i
Q_B[3] = (q_i - q_BList[3])/D_i

Q_C = [0,0,0,0]
Q_C[0] = (q_i - q_CList[0])/D_i
Q_C[1] = (q_i - q_CList[1])/D_i
Q_C[2] = (q_i - q_CList[2])/D_i
Q_C[3] = (q_i - q_CList[3])/D_i

print(Q_A); print(Q_B); print(Q_C)


# Step 11. Using the Trapezoidal rule for well A, compute the volume of oil (in barrels) produced between:
#     (a) time = 0 and time = 1 year
#     (b) time = 1 and time = 2 years
#     (c) time = 2 and time = 3 years. <br>

# In[64]:


#A = .5(Q_A[0]+Q_A[1])(t)
#part A
AreaQ_A = [0,0,0]
AreaQ_A[0] = .5*(Q_A[0] + Q_A[1])*(1)
#part B
AreaQ_A[1] = .5*(Q_A[1] + Q_A[2])*(1)
#part c
AreaQ_A[2] = .5*(Q_A[2] + Q_A[3])*(1)


# Step 12. Add up the three results from 11(a), (b) and (c) to obtain the cumulative production for well A after 3 years. <br>

# In[67]:


AreaA = AreaQ_A[0] + AreaQ_A[1] + AreaQ_A[2]
print(AreaA)


# Step 13. Compare the result from Step 12 (a numerical integration) to the result stored in the last item in list Q_A (an exact integration). Compute the relative error (in %) of the numerical integration. <br>

# In[70]:


# 𝐸𝑡 = 𝑡𝑟𝑢𝑒 𝑣𝑎𝑙𝑢𝑒 − 𝑎𝑝𝑝𝑟𝑜𝑥𝑖𝑚𝑎𝑡𝑒 𝑣𝑎𝑙𝑢𝑒 
# 𝜖𝑟𝑒𝑙 = E_t/true value
E_t = Q_A[3] - AreaA
E_rel = E_t / Q_A[3]
print(f"{E_rel} %")

