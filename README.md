# Simple Quiz App

# Assumptions
1. The app supports only one user.
2. Each session allows the user to answer a maximum of 5 random questions.
3. Questions must already be present in the database (no UI for question creation).
4. The correct option for each question is represented as 'A', 'B', 'C', or 'D'.
5. The session data is reset after 5 questions or when the app is restarted manually.
6. This application is for demonstration purposes and does not include authentication or advanced error handling.

# Full Code Details

# Backend
1. Models:
    - Question: Stores the quiz questions with multiple options and correct answer.
    - QuizSession: Tracks user performance for a single session (e.g., total correct/incorrect).

2. Views:
    - QuizView: Manages the quiz session and displays random questions until the limit is reached.

3. URL configuration:
    - Includes a single route for the quiz (`/`).

# Frontend
1. Templates:
    - quiz.html: Displays the current question and options to the user.
    - result.html: Shows the user’s performance after completing the quiz.

# Setup Instructions
1. Install Django and set up the project: django-admin startproject quiz_app.
2. Add the app and configure it in INSTALLED_APPS.
3. Run migrations: python manage.py makemigrations and python manage.py migrate`.
4. Populate the database with questions using Django admin.
5. Start the development server: python manage.py runserver.
6. Access the app athttp://localhost:8000/.

# Testing the App
1. Visit the app and answer up to 5 questions.
2. After completing, review the results displayed on the results page.

Home page : 
![image](https://github.com/user-attachments/assets/b20aada8-a315-4cb9-957d-a2b60117ad0c)

Quiz page : 
![image](https://github.com/user-attachments/assets/7ba63e25-5a98-41d4-b3bb-a16e10029e17)

After submittion the quiz result page : 
![image](https://github.com/user-attachments/assets/bef81a96-438a-4438-81a6-cc85e0dcbb18)



