
 **📘 Assignment 04 – Regression Exercises**

🎲 Exercise 01: Regression to the Mean

4) What do you observe? You may need to run the loop a few times to see it.
   
When the number of dice throws is small the histogram looks uneven and some sums may appear more than expected just by chance. As we increase the number of throws, the bars in the histogram begin to smooth out and settle into the well-known probability distribution for two dice: the middle value (7) appears most often, while extreme values like 2 and 12 are the least frequent. With very large numbers of throws the histogram becomes very close to the theoretical probabilities.

5) How is this related to "regression to the mean"?
   
Regression to the mean means that extreme or unusual results tend to move closer to the average when more data is collected. In our dice experiment, small samples can show unusual results. But as we increase the number of trials these extreme deviations balance out and the overall distribution returns to the expected pattern centered around the mean value of 7..

📈 Exercise 02: Regression Model

6) Assess the quality of the regression (visually and using numbers) in your own words.
   As the output is: 

 - Coefficient or slope  : 7.717287640785383
 - Root Mean Squared Error (RMSE): 12.218571272826035
 - Mean Absolute Error (MAE): 9.746718764605346
 - R-squared (R²): 0.8551742120609958

The scatter plot shows a clear upward trend as the taller people generally have more weight. A straight-line model fits this relationship quite well. The regression line suggests that on average for increase in 1 inch the weight is increased by 7.7172. 

The model isn’t perfect because People’s weights depends upon various  reasons besides height. SO, the predictions can be off by around 12.218. Still, the R² value of about 0.855 tells us that height alone explains most of the variation in weight.




 



