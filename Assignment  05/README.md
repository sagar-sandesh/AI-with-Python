
# 📘Assignment 5 
----
## Problem 1: Diabetes 
### Investigate the model for predicting Diabetes disease progression by adding more explanatory variables to it in addition to bmi and s5. 
**a) Which variable would you add next? Why?** 
I am choosing 'bp' as the Next variable as it has the strongest correlation to the target after bmi and s5.

**b) How does adding it affect the model's performance? Compute metrics and compare to having just bmi 
and s5.** 
Adding 'bp' gives small but consistent improvements in test R2 and RMSE. The R2 increases slightly and
RMSE decreases slightly.

**d) Does it help if you add even more variables?** 
Include your own findings and explanations in code comments or inside triple quotes.
Each step above is worth a point. You need 2 points in order to complete this problem. 

 Using bmi and s5 as the baseline, adding bp slightly improves performance. Test metrics  R2(bmi+s5) move from 0.482 to 0.491
and RMSE(bmi+s5) decreases from 57.176 to 56.626 (bmi+s5+bp).
Adding s4 does not help: the test metrics become R2 = 0.480 and RMSE = 57.260 (bmi+s5+bp+s4), which is worse than with bp.

### CONCLUSION:
Therefore, based on these results, adding more variables is not benefiting us; three variables (bmi, s5, bp) are sufficient here.

----
