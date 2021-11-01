# Median housing value prediction

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data. We have modelled the median house value on given housing data. 

The following techniques have been used: 

 - Linear regression
 - Decision Tree
 - Random Forest

## Steps performed
 - We prepare and clean the data. We check and impute for missing values.
 - Features are generated and the variables are checked for correlation.
 - Multiple sampling techinuqies are evaluated. The data set is split into train and test.
 - All the above said modelling techniques are tried and evaluated. The final metric used to evaluate is mean squared error.

## To excute the script
Firstly I made changes in the nonstandard.py file like load_housing_data was missing "()" parenthesis, then I found out that fetch_housing_data() was not called so I also rectified that.
Then I installed the conda enviornment in my system.
Then I created the new enviornment in the conda by using-> 'conda create -n mle-dev python'
Then activated conda enviornment using -> 'conda activate mle-dev'
Then I installed the python libraries like
	1. 'conda install pandas'
	2. 'conda install matplotlib'
	3. 'conda install sklearn'
	4. 'conda install scikit-learn'
And at the end I ran the python file using -> 'python nonstandard.py'.
