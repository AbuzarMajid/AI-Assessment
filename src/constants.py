from dataclasses import dataclass

models = ["gpt-4-turbo", "gpt-3.5-turbo-0125"]

@dataclass
class Prompts:
    SQL_assisstant_instructions = """Role: You are an SQL expert and using your expertise in this domain you have to generate questions as per the user requirement. Using the content provided in the function generate as many questions as user wants

User will be asking for multiple number of questions to be generated. Run "generate_easy_questions", "generate_medium_questions" or "generate_advanced_level_questions" to gather the content needed to generate a variety of questions. Run functions only one time irrespective of the number of  questions asked

**For multiple questions you are allowed to switch Answer types
**When generating more than one question talk about multiple topics in different questions under Data Science domain
**Ask questions, Make scenarios all under the tree of Data Science
**Do not disclose anything in the problem statement that is needed in solution
**Please generate questions that are specifically relevant to the day-to-day scenarios and real-world problems faced by Data Scientists, particularly focusing on their use of SQL for data consumption, analysis, and model selection. The questions should reflect the context where Data Scientists primarily utilize SQL to extract and manipulate data for feeding into models, choosing the most suitable machine learning techniques, and analyzing model outputs to provide actionable insights to business stakeholders. It's crucial to note that Data Scientists are consumers of data, rarely modifying the source, and rely on SQL for exploring and preparing data for advanced analytical processes.
**Do not mention any command/helping material that you are expecting from candidate to use
**Structure the question so that it has only one answer type.
**For multiple choice questions give options too.
**For Fill in the Blanks question. USE SQL function as a blank strictly. For Entry level questions use 2 functions in as blanks, for mid level use 4 functions as blank, for advanced questions use 6 functions as blanks
**Make sure to explore wide range of topics under data science while generating multiple questions

Question Categories:
1. Explain/Analyze a Query Questions: This must includes a query  that needs to be analyzed. This type of questions can't take more than 2 minutes to be solved. Answer type could be video or audio. The query needs to be composed of at least 3 different functions. 
2. Explain SQL Concepts (differences/use cases): This type of questions can't take more than z minutes to be solved. Answer type could be video, audio, multiple choice. The explanation would focus on differences between concepts or when to use a specific function in a real-world application. 
3. Debugging a Query Questions: This type of questions can't take more than 4 minutes to be solved. Answer type could be Fill in the blanks, coding, multiple choice.' 
4. Optimization Discussion: Give a query and ask to optimize it. This type of questions can't take more than 5 minutes to be solved. Answer type could be video, audio, coding.
5. Design a Query: This type of question can't take more than 8 minutes to be solved. Answer type could be coding only. 
6. Complete a Query: Give the query with some blanks in it for candidates to fill. This type of question can't take more than 5 minutes to be solved. Answer type could be  Fill in the blanks only. The query needs to be composed of at least 4 different functions for complete and 3 for design. 
7. Scenario-Based Questions: This type of question can't take more than 10 minutes to be solved. Answer type would be coding only. Candidates will be presented with real case scenarios and a problem they need to solve with a query. 
8. Handling Specific Data Challenges(What if questions): This type of question can't take more than 5 minutes to be solved. Answer type would be video or audio. Candidates will be presented with real world scenarios and they would have to explain who they would manage the situation. 


Add this parameter at the end of each question
Common mistakes - Keep in mind when scoring responses.
- not checking the assumptions behind their solution
- not checking or discussing data quality before writing code
- Not writing a step-by-step code
- Not explaining the thought process
- Not checking the edge cases after finishing the solution
- Not discussing areas of optimization or improvement of the code

Output Format: JSON
Problem Statement: (this includes anything needed like SQL query table, question statement. Do not give a clue how to solve that. Craft a proper Problem statement)
Query: (if needed)
Database Schema and Table: (If needed)
Answer Type: Audio or video / Coding/ Fill in the blanks/ Multiple Choice (choose only one)
Topics Covered:
Estimated Time to solve:
Grading criteria parameters: (Generate one liner about the compulsory things that need to be tested for a specific question)

Do not discuss any function/command while asking question
Mimic the way a recruiter is asking in an interactive way"""

    statistics_assisstant_instructions = """Role: You are an Statistics expert and using your expertise in this domain you have to generate questions as per the user requirement that the candidates can verbally answer. Using the content provided in the function generate as many questions as user wants

User will be asking for multiple number of questions to be generated. Run "generate_easy_questions", "generate_medium_questions" or "generate_advanced_level_questions" to gather the content needed to generate a variety of questions. Run functions only one time irrespective of the number of  questions asked

** Run function for one time only no matter how many questions needs to be generated
**When generating more than one question talk about multiple topics in different questions under Statistics domain
**Ask questions, Make scenarios all under the tree of Data Science
**Do not disclose anything in the problem statement that is needed in solution
**Please generate questions that are specifically relevant to the day-to-day scenarios and real-world problems faced by Data Scientists, particularly focusing on their use of Statistics skills. 
**Do not mention any command/helping material that you are expecting from candidate to use
**Structure the question so that it has only one answer type.
**For multiple choice questions give options too.
**Make sure to explore wide range of topics under data science while generating multiple questions
**Problem statement must SHORT and CONCISE

Question Categories:
1. Explain/Analyze a Statistical Concept or Result:
Duration: Up to 2 minutes per question.
Answer Type: Video, audio
Content: Candidates explain or analyze a given statistical result or concept, which could involve discussing the output of a statistical test or explaining a graph. The discussion should incorporate at least 3 different statistical concepts or methods (e.g., explaining mean, variance, and skewness from a dataset).
2. Explain Statistical Differences/Use Cases:
Duration: Up to 2 minutes per question.
Answer Type: Video, audio
Content: Focus on articulating the differences between statistical concepts or when to use a particular statistical method in real-world applications (e.g., when to use a t-test vs. a z-test, or the appropriate scenarios for using linear regression versus logistic regression).
3. Statistical Application Problems:
Duration: Up to 4 minutes per question.
Answer Type: Video
Content: Present a problem where candidates must choose the correct statistical technique or interpret the results from statistical output (e.g., choosing the correct hypothesis test based on given data attributes).
4. Optimization Discussion:
Duration: Up to 5 minutes per question.
Answer Type: Video, audio
Content: Discuss how to optimize a statistical analysis scenario, such as selecting the most efficient statistical tests, reducing error, or improving data collection strategies to enhance the quality of statistical results.
5. Scenario-Based Questions:
Duration: Up to 10 minutes per question.
Answer Type: Video explanation.
Content: Present real-world scenarios where candidates must apply appropriate statistical methods to solve a problem (e.g., analyzing customer data to forecast sales, assessing the impact of a marketing campaign).
6. Handling Specific Data Challenges (What if questions):
Duration: Up to 5 minutes per question.
Answer Type: Video, audio.
Content: Pose hypothetical changes or challenges in data scenarios and ask candidates to explain how they would adjust their statistical approach (e.g., how to handle missing data, what to do if the data violates the assumption of normality in ANOVA).


Output Format: JSON
Problem Statement: (Do not give any hints or clue to solve the question)
Answer Type: Audio or video
Topics Covered:
Estimated Time to solve:
Grading criteria parameters: (Generate one liner about the compulsory things that need to be tested for a specific question)

Do not discuss any function/command while asking question
Mimic the way a recruiter is asking in an interactive way"""

    python_assisstant_instructions = """Role: You are an SQL expert and using your expertise in this domain you have to generate questions as per the user requirement. Using the content provided in the function generate as many questions as user wants

User will be asking for multiple number of questions to be generated. Run "generate_easy_questions", "generate_medium_questions" or "generate_advanced_level_questions" to gather the content needed to generate a variety of questions. Run functions only one time irrespective of the number of  questions asked

**For multiple questions you are allowed to switch Answer types
**When generating more than one question talk about multiple topics in different questions under Data Science domain
**Ask questions, Make scenarios all under the tree of Data Science
**Do not disclose anything in the problem statement that is needed in solution
**Please generate questions that are specifically relevant to the day-to-day scenarios and real-world problems faced by Data Scientists
**Do not mention any command/helping material that you are expecting from candidate to use
**Structure the question so that it has only one answer type.
**For multiple choice questions give options too.
**Make sure to explore wide range of topics under data science while generating multiple questions

Question categories
1. Explain/Analyze a Code Snippet: Provide a code snippet that utilizes at least three different Python functions or concepts. Candidates must analyze the code and explain its functionality, potential outputs, and any errors present. Answer type could be video or audio, allowing candidates to verbally explain their analysis.
2. Explain Python Concepts (Differences/Use Cases): Present two or more Python concepts, such as list comprehensions vs. loops or tuples vs. lists. Candidates must explain the differences between these concepts and discuss their respective use cases in real-world scenarios. Answer type could be video, audio, or multiple choice, allowing candidates to choose the correct concept for a given scenario.
3. Debugging a Code Snippet: Offer a Python code snippet with errors or missing elements. Candidates must identify and correct the errors or fill in the missing components. Answer type could be fill in the blanks, coding, or multiple choice.
4. Optimization Discussion: Provide a Python code snippet and ask candidates to optimize it for efficiency or readability. Candidates must explain their optimization strategies and implement the optimized code. Answer type could be video, audio, or coding.
5. Scenario-Based Questions: Describe a real-world scenario that requires a Python solution. Candidates must write code to address the problem presented in the scenario within a specified time limit. Answer type would be coding only.
6. Handling Specific Data Challenges (What If Questions): Present candidates with real-world data challenges and scenarios. Candidates must explain how they would use Python to manage these situations effectively. Answer type would be video or audio, allowing candidates to explain their approach.

Output Format: JSON
Problem Statement: (this includes anything needed like question statement. Do not give a clue how to solve that. Craft a proper Problem statement)
Answer Type: Audio or video / Coding/ Fill in the blanks/ Multiple Choice (choose only one)
Topics Covered:
Estimated Time to solve:
Grading criteria parameters: (Generate one liner about the compulsory things that need to be tested for a specific question)


Do not discuss any function/command while asking question
Mimic the way a recruiter is asking in an interactive way"""

    ML_assistant_instructions = """"""

@dataclass
class FunctionCallingTools:
    generate_easy_questions = {
            "type": "function",
            "function": {
                "name": "generate_easy_questions",
                "description": "generate number of easy difficulty level questions",
                "parameters": {
                    "type": "object",
                    "properties": {
                    "text": {
                        "type": "string",
                        "description": "Difficulty level: easy"
                    }
                    },
                    "required": [
                    "Difficulty and type of questions along with knowledge"
                    ]
                }
            }
        }
    
    generate_medium_questions = {
            "type": "function",
            "function": {
                "name": "generate_medium_questions",
                "description": "generate number of medium difficulty questions using the knowledge",
                "parameters": {
                    "type": "object",
                    "properties": {
                    "text": {
                        "type": "string",
                        "description": "difficulty level: medium"
                    }
                    },
                    "required": [
                    "diificulty and type of questions along with knowledge"
                    ]
                }
            }
        }
    
    generate_advanced_level_questions = {
            "type": "function",
            "function": {
                "name": "generate_advanced_level_questions",
                "description": "generate number hard questions using the knowledge",
                "parameters": {
                    "type": "object",
                    "properties": {
                    "text": {
                        "type": "string",
                        "description": "Difficulty level: hard"
                    }
                    },
                    "required": [
                    "Difficulty and type of questions along with knowledge"
                    ]
                }
            }   
        }

@dataclass
class FunctionCallingResponses:
    sql_easy_level_topics = """---Entry Level Topics
This entry level skills are needed to test candidates if they have the basic knowledge of SQL working
Basic aggregation functions (COUNT, SUM, AVG, COUNT DISTINCT)
DISTINCT ON
JOIN operations: INNER JOIN, OUTER JOIN, LEFT JOIN, RIGHT JOIN, LEFT, RIGTH, FULL OUTER), Semi joins
Filtering data with AND, OR, NOT
Using BETWEEN, IN, LIKE functions for specific filtering
Sorting data with ORDER BY
Grouping data with GROUP BY
Subqueries
Date and time functions (including MAKE_DATE(), DATE_TRUNC())
Basic error identification in SQL code
Data manipulation and transaction control: SELECT WHERE functions, INSERT INTO functions
Finding maximum and minimum with MAX and MIN functions
Extracting parts of dates with the EXTRACT function
Specifying intervals with the INTERVAL function
Limiting query results with the LIMIT clause
Rounding numerical values with the ROUND function
Concatenating strings with the CONCAT function
Math functions (ABS(), CEIL(), FLOOR())"""

    sql_medium_level_topics = """---Mid Level Topics
The medium level should challenge candidates to demonstrate more advanced SQL knowledge and problem-solving skills:

ROW_NUMBER()
RANK()
DENSE_RANK()
LEAD()
LAG()
FIRST_VALUE()
LAST_VALUE()
NTILE()
Complex Joins Involving Multiple Tables: Multi-level JOINs, Self JOINs, CROSS APPLY and OUTER APPLY (SQL Server-specific), LATERAL JOIN (PostgreSQL-specific)
Complex subqueries and nested queries
Performance tuning and query optimization
Understanding and usage of temporary tables and CTEs
Identifying and handling NULLs and data inconsistencies. Check dimensions of data quality (completeness, uniqueness, duplicated, timelines, calidy, accuracy and consistency)
Top-N Analysis using window functions
CASE WHEN
HAVING clause
Arithmetic operations (addition, subtraction, multiplication, division)
LEAD, LAG, fucntions
Edge cases
CORR(), COVAR_POP(), COVAR_SAMP() for correlation and covariance
PERCENTILE_CONT(), PERCENTILE_DISC() for percentile calculations
WITH clause for CTE definition
Ranking Functions: ROW_NUMBER(), RANK(), DENSE_RANK(), NTILE"""

    sql_hard_level_questions = """---Advanced Level Topics:

Nested SELECT statements for subqueries
Union Function vs JOIN
String Functions: CONCAT(), SUBSTRING(), CHAR_LENGTH(), LOWER(), UPPER()
Use of Non-aggregated Column in Aggregated Expressions: GROUP BY clause necessity, using window functions for aggregation without GROUP BY
UNION, EXCEPT and INTERSECT Operators
PERCENTILE_CONT or Median Function
COALESCE() Function
Cross Join

Additionally you can use the combination of 3-4 below commands/operations in order to generate 

Basic aggregation functions (COUNT, SUM, AVG, COUNT DISTINCT)
DISTINCT ON
JOIN operations: INNER JOIN, OUTER JOIN, LEFT JOIN, RIGHT JOIN, LEFT, RIGTH, FULL OUTER), Semi joins
Filtering data with AND, OR, NOT
Using BETWEEN, IN, LIKE functions for specific filtering
Sorting data with ORDER BY
Grouping data with GROUP BY
Subqueries
Date and time functions (including MAKE_DATE(), DATE_TRUNC())
Basic error identification in SQL code
Data manipulation and transaction control: SELECT WHERE functions, INSERT INTO functions
Finding maximum and minimum with MAX and MIN functions
Extracting parts of dates with the EXTRACT function
Specifying intervals with the INTERVAL function
Limiting query results with the LIMIT clause
Rounding numerical values with the ROUND function
Concatenating strings with the CONCAT function
Math functions (ABS(), CEIL(), FLOOR())
ROW_NUMBER()
RANK()
DENSE_RANK()
LEAD()
LAG()
FIRST_VALUE()
LAST_VALUE()
NTILE()
Complex Joins Involving Multiple Tables: Multi-level JOINs, Self JOINs, CROSS APPLY and OUTER APPLY (SQL Server-specific), LATERAL JOIN (PostgreSQL-specific)
Complex subqueries and nested queries
Performance tuning and query optimization
Understanding and usage of temporary tables and CTEs
Identifying and handling NULLs and data inconsistencies. Check dimensions of data quality (completeness, uniqueness, duplicated, timelines, calidy, accuracy and consistency)
Top-N Analysis using window functions
CASE WHEN
HAVING clause
Arithmetic operations (addition, subtraction, multiplication, division)
LEAD, LAG, fucntions
Edge cases
CORR(), COVAR_POP(), COVAR_SAMP() for correlation and covariance
PERCENTILE_CONT(), PERCENTILE_DISC() for percentile calculations
WITH clause for CTE definition
Ranking Functions: ROW_NUMBER(), RANK(), DENSE_RANK(), NTILE()"""

    python_easy_level_questions = """Python Syntax and Semantics:
Basic data types (int, float, string, boolean)
Arithmetic, comparison, and logical operators
The '//' operator for floor division
Control Flow:
If, elif, else statements
For loops, while loops
List comprehensions
Dictionary comprehension
Basic control flow for loops
Data Structures:
Lists: append, pop, indexing, slicing, doubly-nested loops
Tuples: immutable properties, usage
Dictionaries: creation, keys, values, items
Sets: basic operations
Arrays, strings, and linked lists
Basic Functions and Modules:
Defining and calling functions
Parameter passing and return statements
Importing and using standard libraries (math, datetime)
File Handling:
Opening and reading files, writing to files
String Manipulation:
Common string methods: .upper(), .lower(), .split(), .join()
Error Handling:
Basic try-except blocks
NumPy Basics:
Array creation, basic operations
Indexing and slicing
Pandas Basics:
DataFrame creation, reading from CSV
Basic data manipulation: filtering, sorting
Matplotlib Basics:
Creating simple plots, bar charts, histograms
Fizz_buzz_sum
Enumerate()
Extend()
"""

    python_medium_level_questions = """Advanced Data Structures:
Nested dictionaries and lists
Dictionary comprehensions
Object-Oriented Programming (OOP):
Classes and objects: defining and using
Inheritance and polymorphism
Operator Overloading
Advanced Functions:
Lambda functions
Using map, filter, reduce
File Manipulation:
Advanced file operations, working with file paths
Modules and Packages:
Creating and using custom modules
Package management with pip
Regular Expressions:
Basic pattern matching, searching, and extraction
Advanced pattern matching
Error and Exception Handling:
Advanced use of try-except-else-finally blocks
Data Cleaning and Preparation:
Handling missing data, outlier detection
Data normalization and encoding of categorical variables
Statistical Analysis:
Using libraries like SciPy or StatsModels for basic statistical modeling and hypothesis testing
Overfitting and underfitting, confounding factors
Import CSV files from a URL via Pandas
"""

    python_hard_level_questions = """Asynchronous Handling: multithreading,  multiprocessing async IO functionality and differences
Pydantic: used to define custom data types
Memory management and garbage collection
Advanced Pandas:
Merging, joining DataFrames
Advanced indexing, multi-indexing,  negative indexing
Group by operations, pivot tables
Advanced NumPy:
Broadcasting, vectorized operations
Transpose NumPy arrays
Universal functions for n-dimensional arrays
Boolean arrays, NaT handling
Universal functions for n-dimensional arrays, Boolean arrays, NaT
Machine Learning with scikit-learn:
Basic model fitting, cross-validation
Simple predictions, model evaluation techniques
Data Visualization:
Advanced plotting with Seaborn, interactive plots with Plotly
APIs and Web Scraping:
Using libraries like Requests and BeautifulSoup
Handling JSON data
Databases:
Basic SQL queries through Python
Connecting to SQL databases, reading/writing data
Performance Optimization:
Profiling code, understanding time complexity
Techniques like vectorization
Deep Learning Basics:
Introduction to frameworks like TensorFlow or PyTorch
Building simple neural network models
Natural Language Processing (NLP):
Basics of text preprocessing using libraries like NLTK or spaCy
Computer Science Fundamentals:
Data structures and algorithms: Trees, Graphs, Recursion, Sorting algorithms (quicksort, merge sort, heap sort)
Big O notation: Time and space complexity
Hash tables, queues
Graph algorithms, including greedy algorithms
Searching algorithms: Linear and Binary Search
Tree Traversals: BFS and DFS
Dynamic Programming
Additional Programming Concepts:
Decorators and Generators: Use of decorators, understanding generators with yield
Handling complex data types and structures
"""

    statistics_easy_level_questions = """Descriptive Statistics:
Central Tendency: Mean, median, mode.
Variability: Range, variance, standard deviation, interquartile range.
Frequency Distributions: Tables, histograms, frequency polygons.
Percentiles and Quartiles: Including the calculation and interpretation of quartiles.
Box Plots: Understanding the spread and outliers in data.
Probability Basics:
Rules of Probability: Addition rule, multiplication rule, complementary rule.
Conditional Probability and Independence: Understanding dependencies between events.
Random Variables: Discrete and continuous random variables.
Bayes’ Theorem: Application in predictive modeling.
Normal distribution
Uniform distribution
Bernoulli distribution
Binomial distribution
Geometric distribution
Poisson distribution
Exponential distribution
Deriving the mean and variance of distributions
Central Limit Theorem
The Birthday problem
Card probability problems
Die roll problems
Covariance and correlation
Population and sample
Nominal, ordinal and continuous, discrete data types
Outliners
The Simpson’s Paradox
Selection Bias
"""

    statistics_medium_level_questions = """Inferential Statistics:
Point and Interval Estimations: Estimating population parameters and constructing confidence intervals.
Hypothesis Testing: Null and alternative hypotheses, type I and II errors, power of a test.
Z-tests, T-tests, Chi-squared Tests: Applications and assumptions behind each test.
ANOVA and MANOVA: Analysis of variance between groups, multiple factors at once.
Non-parametric Tests: Wilcoxon, Mann-Whitney, Kruskal-Wallis tests.
Variance Test
Goodness of Fit Test for Categorical Data
Pairwise Tests
T-Test Assumptions
Hypothesis Statements
T-Test for sample means
Z-Test for proportions
Regression Analysis:
Linear Regression: Simple and multiple linear regression models.
Logistic Regression: Binary outcomes and logistic function.
Polynomial Regression: Non-linear relationships between variables.
Model Diagnostics: Residual analysis, influence measures, multicollinearity.
Model Selection and Regularization: AIC, BIC, Ridge, Lasso, Elastic Net.
OLS regression
Confidence vs prediction intervals
Regression model assumptions
R-Square vs R-Square Adjusted
CP Statistics
Model Interpretation
Experimental and Survey Design:
Sampling Techniques: Simple random, stratified, cluster, systematic sampling.
Designing Experiments: Control group, randomization, blinding, replication.
Validity and Reliability: Ensuring accurate and consistent measurements.
"""

    statistics_hard_level_questions = """Multivariate Statistics:
Factor Analysis: Reducing dimensionality, factor extraction.
Cluster Analysis: Hierarchical, k-means, and density-based clustering.
Discriminant Analysis: Classification of observations into predefined categories.
Canonical Correlation: Relationship between two sets of variables.
Multidimensional Scaling: Visualizing similarities or differences in data.
Advanced Modeling Techniques:
Generalized Linear Models (GLMs): Beyond normal regression, including Poisson and logistic models.
Mixed Effects Models: Handling both fixed and random effects in data.
Non-linear Models: Advanced algorithms for complex relationships.
Time Series Analysis: ARIMA models, seasonal decomposition, forecasting.
Survival Analysis: Techniques like Cox proportional hazards model.
Machine Learning in Statistics:
Decision Trees and Random Forests: Classification and regression trees.
Support Vector Machines: Linear and non-linear data classification.
Neural Networks: Basics of architecture, backpropagation, and applications.
Ensemble Methods: Boosting, bagging, and stacking techniques.
Dimensionality Reduction: Techniques like PCA, t-SNE.
Advanced Probability:
Stochastic Processes: Markov chains, Poisson processes.
Queuing Theory: Analyzing systems involving waiting lines or queues.
Bayesian Statistics: Prior distributions, posterior updates, Bayesian networks
"""