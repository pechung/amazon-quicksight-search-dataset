# amazon-quicksight-search-dataset
Use this script to list all Amazon QuickSight datasets, dataset owners, and insert into an Amazon DynamoDB table to make datasets searchable.

This is a workaround until AWS builds an API to search Amazon QuickSight datasets. For example, you can catalogue the datasets and their ownership by running a script every 30 minutes or so with the output going into a database. Then query that database to get the list of datasets that are available to the author. It may be out of date if the ownership has changed within the last 30 mins, but would be one way of getting the information you need. I understand this is not an ideal solution, but could be a workaround until an official API is released.
