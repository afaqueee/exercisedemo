# Median housing value prediction

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data. We have modelled the median house value on given housing data. 

The following techniques have been used: 

 - Linear regression
 - Decision Tree
 - Random Forest

## Steps performed
1) We prepare and clean the data. We check and impute for missing values.

2) Features are generated and the variables are checked for correlation.
 
3) Multiple sampling techinuqies are evaluated. The data set is split into train and test.
 
4) All the above said modelling techniques are tried and evaluated. The final metric used to evaluate is mean squared error.

## To excute the script
Firstly I made changes in the nonstandard.py file like load_housing_data was missing "()" parenthesis, then I found out that fetch_housing_data() was not called so I also rectified that.
Then I installed the conda enviornment in my system.

Then I created the new enviornment in the conda by using
>conda create -n mle-dev python

Then activated conda enviornment using
>conda activate mle-dev

Then I installed the python libraries like
	1. 'conda install pandas'
	2. 'conda install matplotlib'
	3. 'conda install sklearn'
	4. 'conda install scikit-learn'
And at the end I ran the python file using
>python nonstandard.py

## Steps performed
1) We prepare and clean the data. We check and impute for missing values.

2) Features are generated and the variables are checked for correlation.
 
3) Sampling techinuqies are evaluated. The data set is split into train and test.
 
4) All the above said modelling techniques are tried and evaluated. The final metric used to evaluate is mean squared error.

 ## We have added four python files-

-ingest_data

-train

-score

-mlflowrun

## How to install and run your code using .whl and tar.gz files

1)Firstly when you have .whl and tar.gz file, run commands 
>pip install housing_package-0.0.1-py3-none-any.whl
>tar -xf housing_package-0.0.1.tar.gz 
After running the above command, all the files will appear which we included in MANIFEST.in file.

2)Move into the directory
>cd housing_package-0.0.1

3)Create new conda environment with name as per your wish using env.ymml file, command- 
>conda env create --name name_of_conda_env -f env.yml

4)Then activate conda environment using 
>conda activate name_of_conda_env

5)Install virtualenv by running 
>python3 -m pip install --user -U virtualenv

6)Then give a name to virtualenv - 
>python3 -m virtualenv env_name

7)Now activate it by 
>source env_name/bin/activate

8)After that install all the dependencies of requirements.txt using 
>pip install -r requirements.txt

9)In another terminal run
>mlflow ui

10)To display artifact and parameters in the mlflow ui an in the console, in the mle_training directory run 
>python mlflowrun.py

11)For packaging of the python modules, type 
>python -m build

12)For checking the pytest run command 
>python -m pytest

## For running docker image from Docker Hub

1) To get this image on your local system run 
>docker pull chandakanant00/housing_price_prediction

2) Now to run the image use command 
>docker run -it -d --name as_per_your_wish chandakanant00/housing_price_prediction

3) To execute the container use command 
>docker exec -ti as_per_your_wish bash

4) After that run the following command to get inside mle-training directory
>cd mle-training

5) Activate conda use command 
>source activate mle-training

6) Activate virtual env use command 
>source my_env/bin/activate

7) Open new terminal and follow steps 3 to 6 and after that run the following command on the new terminal
>mlflow ui

8) Come back to the old and run command 
>"python mlflowrun.py"
## HTML Files Location

-The output HTML files are located under docs/_build/html in mle_training directory.

## HTML Files Location

-The output HTML files are located under docs/_build/html in mle_training directory.
