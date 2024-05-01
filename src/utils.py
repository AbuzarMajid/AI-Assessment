import random

def sql_get_category(n):
    list_of_categories = [
        "Explain/Analyze a Query Questions",
        "Explain SQL Concepts (differences/use cases)",
        "Debugging a Query Questions",
        "Optimization Discussion",
        "Design a Query",
        "Complete a Query",
        "Scenario-Based Questions", 
        "Handling Specific Data Challenges(What if questions)"
    ]
    
    # Choose n number of categories randomly
    selected_categories = random.sample(list_of_categories, n)
    
    return " and ".join(selected_categories)

def statistics_get_category(n):
    list_of_categories = [
        "Explain/Analyze a Statistical Concept or Result",
        "Explain Statistical Differences/Use Cases",
        "Statistical Application Problems",
        "Optimization Discussion",
        "Scenario-Based Questions", 
        "Handling Specific Data Challenges(What if questions)"
    ]
    
    # Choose n number of categories randomly
    selected_categories = random.sample(list_of_categories, n)
    
    return " and ".join(selected_categories)

def python_get_categories(n):
    list_of_categories = [
        "Explain/Analyze a Code Snippet",
        "Explain Python Concepts (Differences/Use Cases)",
        "Debugging a Code Snippet",
        "Optimization Discussion",
        "Scenario-Based Questions", 
        "Handling Specific Data Challenges(What if questions)"
    ]
    
    # Choose n number of categories randomly
    selected_categories = random.sample(list_of_categories, n)
    
    return " and ".join(selected_categories)

def categories(skill_name, number_of_questions):
    if "sql" in skill_name:
        return sql_get_category(n=number_of_questions)
    if "statistics" in skill_name:
        return statistics_get_category(n=number_of_questions)
    if "python" in skill_name:
        return  python_get_categories(n=number_of_questions)





