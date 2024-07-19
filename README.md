# Technical Screening for Software Engineers
Repo to provide a technical interview screening for software engineers. The goal is to limit the time to one hour. Instructions are documented below.


## Requirements
- Clone this repository to your Github account and make it public so it can be reviewed.
- Create a new branch from the main branch with the date of the screening interview with feature as the prefix
  - Example: feature-2024-07-19
- Create a docker-compose file to run the application with these services:
  - Python 3.10 image (Data Collector)
    - This container shoould have a custom shell script that produces an exit code on a condition that you define.
    - The shell script should be executed every 5 seconds to determine the health of the container.
  - Python 3.9 image (IP Address Service)
    - This container should not run unless the Data Collector container is healthy.
  - All containers should have a volume mounted to the source code folder for each service.
    - Do not copy files into the working directory
    - Changes to source code should be reflected in the container without having to rebuild the image
    - Each container should have its own Dockerfile in the source code folder executed by the docker-compose file
- For Data Collector service create python code that meets these requirements:
  - Calls the SQLite database file database/customers.db and retrieves all records from the customers table.
  - Rename the job column to occupation.
  - Write the records to a CSV file named customers.csv in the output folder if the file doesn't already exist
    - If the file exists, diff the records and only write the new records to the file
  - Write the data to a second csv file and ensure this second file is not pushed to Github via Git
  - The python code should run every 5 minutes
- For IP Address Service create python code that meets these requirements:
  - Retreives the prefixes in the database file database/prefixes.db
  - Determines which prefixes have a parent prefix
  - Write the prefixes to a json file named prefixes.json in the output folder
  - Ensure the json file has a new key named parent_prefix that contains the parent prefix if it exists
  - Use pytest to write a test for the parent prefix function and pycoverage to determine the code coverage
    - The tests should be in a folder in the source code of the container
    - The coverage results should be output to a coverage_results file
- Push the source code to your Github account and create a pull request to the main branch
  - Provide the link to the pull request for review to your interviewer