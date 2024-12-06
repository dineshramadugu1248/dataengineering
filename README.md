# dataengineering
Analysis of covid vaccination data
SCOPE :
Scope of the project is to analyze the covid vaccine data in data bricks using Amazon Web Services (AWS)
and extract the following 4 insights
1)T otal No.of Doses done
2)State wise dose completion
3)T op 10 States where maximum no of doses are done
4) No.of First Dose , Second dose done on each state
TECH STACK :
AWS , S3 , IAM , Data Bricks , SQL , python , spark.
STEPS :
Step 1 : Create AWS S3 bucket and upload the covid vaccine data csv file and copy the S3 URI
Step 2 : Create new user in AWS IAM and add adminstration permission and generate access keys and
download those keys in csv file
Step 3 : Create cluster and notebook in data bricks and also create table by uploading the access keys csv
file using access key table, hadoop configurations, S3 URI and mount the data from S3 to databricks and
create data frame using these data.
Step 4 : Modify the Column names by replacing the spaces , special characters with under score.
Step 5 : Convert the data frame to table.
Step 6 : Write SQL queries to generate insights
