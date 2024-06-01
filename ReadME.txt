Description: For the project, I have integrated all my data into one final dataset in the form of csv files called 'Yitong_Ouyang_HW5_Data.csv'. The dataset is provided in this zip folder and are present in a folder named 'Dataset'. Both, scraping and analysis, is done in one code. Running the code in default mode will first create the dataset and then perform the analysis using those datasets. 

Note: To run the code in terminal, one needs to create a virtual environment first. The following codes need to be run in the terminal: 
python3 -m venv tutorial-env
source tutorial-env/bin/activate

Requirements: Following requirements are needed to be satisfied to run this code:
Packages to be installed:
beautifulsoup4==4.11.1
matplotlib==3.5.1
numpy==1.21.5
pandas==1.4.2
requests==2.27.1
scikit_learn==1.1.3
scipy==1.7.3
seaborn==0.11.2
statsmodels==0.13.2

To install above packages use the following command: pip install -r requirements.txt
'requirements.txt' file has a list of all the necessary packages required to run this code
Running the code:

The code can be run in two modes: default and static
Description: For the final project, I have created one dataset in the form of a csv file called 'Yitong_Ouyang_HW5_Data.csv' I collected the data of stock price of the three companies by using API to request the information.  I created the car sales of the three companies by using web scrap. And I got the U.S. gas price by downloading the data from a website. And then I integrated all the data into one dataset. The dataset is provided in this zip folder and are present in a folder named 'Dataset'. Both, scraping and analysis, is done in this zip folder and are present in a folder named 'Dataset'. Both, scraping and analysis, is done in one code. Running the code in default mode will first create the dataset and then perform the analysis using those datasets.

Running the code:
The code can be run in two modes: default and static 

Default mode: To run the code in default mode, type command- python Yitong_Ouyang_HW5_DSCI510.py
I have included this mode to only display first ten observations of all datasets. In this mode, the dataset ('Yitong_Ouyang_HW5_Data.csv') will be created along with their respective csv files. The csv files will be stored in the same folder in which our code is stored. The analysis part is also performed in the default mode after the datasets are created. In the output of default mode, the datasets is printed as soon as it is created. Some information (like rows, columns .etc) related to the datasets. The analysis part will be displayed too in the output once the dataset is successfully created.
NOTE: It takes 3 seconds for the default mode to run. It takes 1 second for the scrape mode to run. And it takes 3 seconds for the static mode to run.

Scrape Mode:  To run the scrape mode, type command- python Yitong_Ouyang_HW4_DSCI510.py --scrape
I have included this mode to only display first five observations of the dataset. In this mode, the values are actually being scraped or fetched through API but the whole dataset is not being generated. Since the code in the default mode takes a longer time to run, I have added this mode so that it can be verified that my code is working and the data is being successfully scraped. NOTE: I am not showing analysis in this mode. This mode is just to show that my dataset is being formed successfully.
Static mode: To run the code in static mode, type command- python Yitong_Ouyang_HW5_DSCI510.py --static Datasets
In this mode, I have displayed the dataset that I will be using for analysis. I am accessing the ' Yitong_Ouyang_HW5_Data.csv' which is the pre-generated dataset stored in 'Dataset' Folder. I am using read_csv method of pandas to read the csv files and displaying its contents in the static mode. Furthermore, all the analysis are also performed in this mode using the static datasets.

Maintainability: The code has certain limitations when it comes to fetching the data. When I was scrapping the data of three companies' car sales from the website, I used the regex to get data for each year. This is a sample of my regex: "id = re.compile(r'table_1812_row_(1[3-7])')" One id is for the data of one year's sale. I basically looked through all the data to find the tables I want and then find the data pattern and created the regex. However, if the researcher wants to find many years, this might be a problem. 

