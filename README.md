# LinearRegression
Sample code on how to apply Linear Regression.
Linear regression is a statistical modeling technique used to establish a relationship between a dependent variable and one or more independent variables. It assumes a linear relationship between the independent variables and the dependent variable, with the objective of finding the best-fitting line that represents this relationship.

The theory behind linear regression can be explained as follows:

Model Representation:
In linear regression, we assume that the relationship between the independent variables (often denoted as X) and the dependent variable (often denoted as Y) can be represented by a linear equation of the form:
Y = b0 + b1X1 + b2X2 + ... + bn*Xn + ε
where b0, b1, b2, ..., bn are the coefficients (or weights) representing the impact of each independent variable on the dependent variable, and ε is the error term capturing the deviation of the actual values from the predicted values.

Objective Function:
The objective of linear regression is to find the values of the coefficients that minimize the sum of squared errors (SSE) between the predicted values and the actual values. The SSE is typically minimized using a method called ordinary least squares (OLS), which calculates the coefficients by minimizing the squared differences between the predicted and actual values.

Assumptions:
Linear regression makes several assumptions, including linearity, independence of errors, constant variance of errors (homoscedasticity), absence of multicollinearity (when multiple independent variables are present), and normality of the error terms. Violations of these assumptions can affect the accuracy and reliability of the regression results.

Evaluation Metrics:
To assess the performance of a linear regression model, several evaluation metrics can be used. These metrics include the coefficient of determination (R-squared), which measures the proportion of variance in the dependent variable explained by the independent variables, as well as metrics such as mean squared error (MSE) and root mean squared error (RMSE) that quantify the average squared differences between predicted and actual values
Multivariate Linear Regression:
Linear regression can be extended to multiple independent variables, known as multivariate linear regression. In this case, the linear equation takes the form:
Y = b0 + b1X1 + b2X2 + ... + bn*Xn + ε
where X1, X2, ..., Xn are the independent variables, and b1, b2, ..., bn are their respective coefficients.

Linear regression has various applications, including prediction, forecasting, and understanding the relationships between variables. It serves as a fundamental technique in statistics and is commonly used in fields such as economics, social sciences, finance, and machine learning.

It is worth noting that while linear regression assumes a linear relationship between the variables, there are other regression models, such as polynomial regression and generalized linear regression, that can capture more complex relationships between variables.
