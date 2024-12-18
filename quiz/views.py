from django.shortcuts import render, redirect
from .models import Question
import random

# Global user data (reset per quiz)
user_data = {
    'questions_asked': [],
    'correct_count': 0,
    'total_attempted': 0,
}

def start_quiz(request):
    # Reset user data
    user_data['questions_asked'] = []
    user_data['correct_count'] = 0
    user_data['total_attempted'] = 0
    return render(request, 'quiz/start.html')


def get_question(request):
    # Check if 5 questions have been asked
    if len(user_data['questions_asked']) >= 5:
        return redirect('results')

    # Fetch a random question not already asked
    questions = Question.objects.exclude(id__in=user_data['questions_asked'])
    if not questions.exists():
        return redirect('results')  # No more questions available

    question = random.choice(list(questions))
    user_data['questions_asked'].append(question.id)

    # Debug print to confirm data is passed to the template
    print("Question Text:", question.question_text)
    print("Option A:", question.option_a)
    print("Option B:", question.option_b)
    print("Option C:", question.option_c)
    print("Option D:", question.option_d)

    # Pass the question to the template
    return render(request, 'quiz/question.html', {'question': question})


def submit_answer(request, question_id):
    if request.method == 'POST':
        selected_option = request.POST.get('option')
        question = Question.objects.get(id=question_id)

        # Update user stats
        user_data['total_attempted'] += 1
        if selected_option == question.correct_option:
            user_data['correct_count'] += 1

        # Check if the quiz is over
        if len(user_data['questions_asked']) >= 5:
            return redirect('results')

        return redirect('get_question')


def show_results(request):
    return render(request, 'quiz/results.html', {
        'total_attempted': user_data['total_attempted'],
        'correct_count': user_data['correct_count'],
        'incorrect_count': user_data['total_attempted'] - user_data['correct_count'],
    })
