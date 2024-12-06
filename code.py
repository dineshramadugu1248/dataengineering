# step 3 code
credentials_df = spark.read.table("access key table name")
access_key = credentials_df.select("Access key ID").first()[0]
secret_key = credentials_df.select("Secret access key").first()[0]
sc._jsc.hadoopConfiguration().set("fs.s3a.access.key", access_key)
sc._jsc.hadoopConfiguration().set("fs.s3a.secret.key", secret_key)
aws_region = "us-east-2"
sc._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3." + aws_region +
".amazonaws.com")
df = spark.read.csv('S3 URI',inferSchema=True,header=True)
display(df)

# step 4 code
changed_columns = [name.replace(" ", "_").replace(",", "").replace(";", "").replace("{",
"").replace("}", "").replace("(", "").replace(")", "").replace("\n", "").replace("\t",
"").replace("=", "") for name in df.columns]
df = df.toDF(*changed_columns)

# step 5 code
df.write.mode("overwrite").saveAsTable("covid_table")

# step 6
# sql queries
# Q1 CODE :
%sql select sum(Total_doses) from covid_table
# Q2 CODE :
%sql select sum(Total_doses),state from covid_table
where state not in ('India')
group by state
# Q3 CODE :
%sql select sum(Total_doses),state from covid_table
where state not in ('India')
group by state
order by sum(Total_doses) desc
limit 10;
# Q4 CODE :
%sql select sum(first_dose),sum(second_dose), state from covid_table
where state not in ('India')
group by state
order by sum(first_dose),sum(second_dose) desc