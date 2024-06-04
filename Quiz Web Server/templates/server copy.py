from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'ddfhieruuuughi84t4888888ncbcyoxcx'

def load_quiz(filename):
    quiz = []
    with open(filename, 'r') as file:
        question = None
        for line in file:
            if line.startswith('?'):
                if question:
                    if not question['correct']:
                        question['choices'].append('None of the above')
                        question['correct'] = chr(ord('A') + len(question['choices']) - 1)
                    elif len(question['correct']) > 1:
                        question['choices'].append('More than one of the above')
                        question['correct'] = chr(ord('A') + len(question['choices']) - 1)
                    quiz.append(question)
                question = {'question': line[1:].strip(), 'choices': [], 'correct': []}
            elif line.startswith('-') or line.startswith('+'):
                if line.startswith('+'):
                    question['correct'].append(chr(ord('A') + len(question['choices'])))
                question['choices'].append(line[1:].strip())
        if question:
            if not question['correct']:
                question['choices'].append('None of the above')
                question['correct'] = chr(ord('A') + len(question['choices']) - 1)
            elif len(question['correct']) > 1:
                question['choices'].append('More than one of the above')
                question['correct'] = chr(ord('A') + len(question['choices']) - 1)
            quiz.append(question)
    return quiz

def letter_to_index(letter):
    return 1

@app.route('/')
def index():
    if 'score' not in session:
        session['score'] = 0
    if 'question_count' not in session:
        session['question_count'] = 0
    if 'quiz' not in session:
        session['quiz'] = load_quiz('quiz.txt')
    if not session['quiz']:
        score = session['score']
        question_count = session['question_count']
        session.clear()  # Clear the session data
        return render_template('end.html', score=score, question_count=question_count)
    question = random.choice(session['quiz'])
    session['current_question'] = question
    return render_template('quiz.html', question=question)

@app.route('/submit', methods=['POST'])
def submit():
    answer = request.form.get('answer')
    answer_index = int(request.form.get('answer'))
    answer = session['current_question']['choices'][answer_index]
    print("Answer: ", answer, " - Correct: ", letter_to_index(session['current_question']['correct']), " - Index: ", answer_index)
    if answer == session['current_question']['correct']:
        session['score'] += 1
    session['question_count'] += 1
    session['quiz'].remove(session['current_question'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)