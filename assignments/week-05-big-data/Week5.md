# Week 5 - Assignment Answers

## How does the Gradient-Boosted Tree Algorithm work in Classification? How does Gradient Boost differ from AdaBoost and Logistic Regression?

Gradient Boosted Tree (GBT) is an ensemble learning method for classification and regression that combines the predictions of multiple decision trees. GBT starts by training a simple decision tree on the input data, and then iteratively adds new trees, where each new tree is trained to correct the mistakes of the previous trees. The final prediction is made by combining the predictions of all the trees through a weighted majority vote.

AdaBoost is another ensemble method that is similar to GBT in that it combines the predictions of multiple weak learners to form a strong learner. However, unlike GBT, AdaBoost trains the weak learners in a sequential manner, where each new learner is trained to focus on the examples that were misclassified by the previous learners.

Logistic Regression is a generalized linear model that is commonly used for classification. It models the probability of a given input belonging to a certain class. Unlike GBT and AdaBoost, logistic regression does not involve decision trees, but instead, uses a linear combination of the input features to make predictions. Logistic regression can be trained using gradient descent optimization algorithm.

GBT and AdaBoost are both ensemble methods that can be used for classification, but GBT is more powerful and can handle more complex data. Logistic Regression is a simpler model but it can only model linear decision boundary.

## What is a Delta Lake and how does it offer a solution to building reliable data pipelines?

Delta Lake is an open-source storage layer that brings ACID (Atomicity, Consistency, Isolation, Durability) transactions to Apache Spark and big data workloads. It allows you to store large amounts of data in a distributed file system, such as HDFS or S3, and manage it using Spark.

Delta Lake offers a number of features that make it well-suited for building reliable data pipelines:

* Data versioning: Delta Lake automatically tracks and manages data versions, making it easy to recover from errors or unintended changes.

* Schema enforcement: Delta Lake allows you to define and enforce a schema on your data, which helps to prevent data quality issues caused by schema drift.

* Time Travel: Delta Lake allows you to query your data as it existed at any point in the past, which is useful for auditing and troubleshooting.

* Data Management: Delta Lake supports data management operations such as delete, update and merge, which makes it easy to handle slowly changing dimensions, upserts, and deletes.

* ACID Transactions: Delta Lake ensures that your data remains consistent and correct, even in the face of concurrent updates and deletes.

Delta lake is a good solution for building reliable data pipelines because it offers the ability to manage data versions, enforce schema, and provide transaction guarantees which are important for any data pipeline. This makes it easy to recover from errors, troubleshoot issues, and ensure data consistency.

## When working with Pandas, we use the class pandas.core.frame.DataFrame and when working with the pandas API in Spark, we use the class pyspark.pandas.frame.DataFrame, are these the same, explain why or why not?

No, they are not the same.

pandas.core.frame.DataFrame is a class provided by the pandas library and is used for data manipulation and analysis in a single machine. It allows you to work with data in a tabular format, and provides a wide range of data manipulation and analysis functionality.

On the other hand, pyspark.sql.dataframe.DataFrame is a class provided by the PySpark library, which is the Python API for Apache Spark. It is used for distributed data processing in a cluster, and allows you to work with data that is too large to fit into memory on a single machine.

Although both classes have similar functionality and a similar API, the way they handle data and perform computations is fundamentally different.

Pandas runs on single machine and uses memory to store data and perform computation. So, it is good for small to medium size data, and for data exploration, cleaning, and transformation.

In contrast, PySpark uses a distributed computing framework (Apache Spark) to process data in a cluster. It is designed to handle large-scale data processing, and can handle data that is too large to fit into memory on a single machine. It is good for large scale data processing and distributed computing.

So, while the pandas DataFrame can be used for data exploration and cleaning, the PySpark DataFrame is better suited for distributed data processing and working with large-scale data.

## What is a Machine Learning Pipeline is and why it’s important? What are the steps in a Machine Learning workflow?

A Machine Learning pipeline is a sequence of steps that are followed to build, evaluate, and deploy a machine learning model. It is a way of structuring the work of a machine learning project and it helps to automate and streamline the process, making it more efficient and easier to understand.

The main reason why pipelines are important is that they help to prevent errors and make the process more reproducible. By breaking the process down into small, modular steps, it is easy to understand what is happening at each stage and to identify and fix any errors that may occur. This can be especially useful in large projects with many different components, where it can be difficult to keep track of everything that is happening.

The steps in a machine learning workflow are:

1. Data Collection: Gathering the data that will be used to train and test the model.

2. Data Preprocessing: Cleaning and transforming the data to make it ready for modeling.

3. Feature Engineering: Creating new features from the existing data that can be used to improve the model's performance.

4. Model Selection: Choosing the appropriate algorithm and hyperparameters to use for the model.

5. Model Training: Training the model on the preprocessed data.

6. Model Evaluation: Testing the model to evaluate its performance and identify any issues.

7. Model Deployment: Deploying the model to production and monitoring its performance.

8. Model Refining: Based on the performance of the model in production, refine the model or improve the features.

A Machine Learning pipeline allows you to automate these steps and chain them together, so that the output of one step is automatically passed as input to the next step. This helps to ensure that the process is consistent and reproducible, and makes it easy to update or modify the pipeline as needed.
