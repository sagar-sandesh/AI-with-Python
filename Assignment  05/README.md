
# 📘Assignment 5 
----
## Problem 1: Diabetes 
### Investigate the model for predicting Diabetes disease progression by adding more explanatory variables to it in addition to bmi and s5. 
**a) Which variable would you add next? Why?** 
After looking at the correlations, I decided to add blood pressure (bp) as the next variable. It shows the strongest link to the target variable after BMI and s5.

**b) How does adding it affect the model's performance? Compute metrics and compare to having just bmi 
and s5.** 
The scatter plot also supports this  as there is a clear upward trend between bp and the target.

**d) Does it help if you add even more variables?** 
Including bp in the model gives a small but consistent boost. 

 ----
----
## Explanation: 
. Starting with BMI and  s5 after adding bp improves the R2 from 0.481561 to 0.491494 and RMSE decreses from 57.1759 to 56.6256
. When adding s4 the performance is bad as R2 dropped to 0.480028 and RMSE increase to 57.260431.
. This means the s4 is not reliable predictor for this problem.

----

----

### CONCLUSION:
Adding bloop pressure(bp) helps a bit but adding s4 is rather than helping it is creating the noise. So, Adding more variable is not helping but rather its making noise. 

----

