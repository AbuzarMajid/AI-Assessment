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
Common Mistakes:
Estimated Time to solve:
Grading criteria parameters: (For a specific question discuss three cases, Be specific and use function names need to be used, Green Line: "<you have to Recommend which details would optimize the quality or depth of the response>", Grey Line: <Tell about the necessary aspects or components in any way, Red Line: <Recommend which things if not added, the respond would not be correct.>)


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


Output Format:
Problem Statement: (Do not give any hints or clue to solve the question)
Answer Type: Audio or video
Topics Covered:
Estimated Time to solve:
Grading criteria parameters: (Generate one liner about the compulsory things that need to be tested for a specific question)

Do not discuss any function/command while asking question
Mimic the way a recruiter is asking in an interactive way"""

    python_assisstant_instructions = """"""

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

    sql_advanced_level_questions = """---Advanced Level Topics:

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