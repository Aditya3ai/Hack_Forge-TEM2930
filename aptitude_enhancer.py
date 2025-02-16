import streamlit as st
import random
import pandas as pd
import plotly.express as px

# Define aptitude topics
modules = [
    "Quantitative Aptitude", "Logical Reasoning", "Verbal Ability", "Data Interpretation", "General Knowledge"
]

# Sample questions database with real questions and correct answers
questions_db = {
    "Quantitative Aptitude": [
        {"question": "What is 25 + 30?", "options": ["A. 55", "B. 60", "C. 65", "D. 70"], "correct": "A"},
        {"question": "What is 12 * 8?", "options": ["A. 96", "B. 104", "C. 108", "D. 112"], "correct": "A"},
        {"question": "What is 15% of 200?", "options": ["A. 30", "B. 25", "C. 35", "D. 40"], "correct": "A"},
        {"question": "What is the square root of 144?", "options": ["A. 10", "B. 12", "C. 14", "D. 16"], "correct": "B"},
        {"question": "What is the value of 3^4?", "options": ["A. 81", "B. 64", "C. 72", "D. 48"], "correct": "A"},
        {"question": "What is 72 ÷ 9?", "options": ["A. 8", "B. 6", "C. 7", "D. 5"], "correct": "B"},
        {"question": "What is 120 ÷ 15?", "options": ["A. 8", "B. 9", "C. 10", "D. 11"], "correct": "C"},
        {"question": "If x = 5, what is the value of 3x + 2?", "options": ["A. 17", "B. 15", "C. 18", "D. 16"], "correct": "A"},
        {"question": "How many hours are in 3 days?", "options": ["A. 60", "B. 72", "C. 80", "D. 90"], "correct": "B"},
        {"question": "What is the LCM of 6 and 8?", "options": ["A. 24", "B. 48", "C. 36", "D. 18"], "correct": "A"},
    ],
    "Logical Reasoning": [
        {"question": "If all roses are flowers, and some flowers fade quickly, can we conclude that some roses fade quickly?", "options": ["A. Yes", "B. No", "C. Can't be determined", "D. None of the above"], "correct": "A"},
        {"question": "If some cats are animals, and all animals are pets, can we conclude that some cats are pets?", "options": ["A. Yes", "B. No", "C. Can't be determined", "D. None of the above"], "correct": "A"},
        {"question": "If A > B and B > C, what can we conclude about A and C?", "options": ["A. A > C", "B. A < C", "C. A = C", "D. Can't be determined"], "correct": "A"},
        {"question": "If two statements are true, what can be said about their conclusion?", "options": ["A. True", "B. False", "C. Uncertain", "D. Both can be true"], "correct": "A"},
        {"question": "If 4 people can complete a task in 5 days, how many days will it take for 8 people?", "options": ["A. 2.5", "B. 5", "C. 7", "D. 10"], "correct": "A"},
        {"question": "If a train is moving at 60 km/h, how much distance will it cover in 2 hours?", "options": ["A. 100 km", "B. 120 km", "C. 150 km", "D. 160 km"], "correct": "B"},
        {"question": "Which comes next in the series: 2, 4, 8, 16, ?", "options": ["A. 24", "B. 32", "C. 30", "D. 20"], "correct": "B"},
        {"question": "Which of the following is the opposite of 'Increase'?", "options": ["A. Boost", "B. Reduce", "C. Elevate", "D. Raise"], "correct": "B"},
        {"question": "If all squares are rectangles, and all rectangles have four sides, can we conclude that all squares have four sides?", "options": ["A. Yes", "B. No", "C. Can't be determined", "D. None of the above"], "correct": "A"},
        {"question": "If two pencils are twice the length of one pencil, what is the ratio of the lengths?", "options": ["A. 1:2", "B. 2:1", "C. 3:1", "D. 1:1"], "correct": "B"},
    ],
    "Verbal Ability": [
        {"question": "Select the synonym for 'Happy'", "options": ["A. Joyful", "B. Sad", "C. Angry", "D. Excited"], "correct": "A"},
        {"question": "Select the antonym for 'Success'", "options": ["A. Failure", "B. Achievement", "C. Victory", "D. Glory"], "correct": "A"},
        {"question": "Choose the correct spelling:", "options": ["A. Accomodation", "B. Accommodation", "C. Accomadation", "D. Acommodation"], "correct": "B"},
        {"question": "Which word is similar to 'Secure'?", "options": ["A. Safe", "B. Open", "C. Exposed", "D. Unsafe"], "correct": "A"},
        {"question": "What is the opposite of 'Unhappy'?", "options": ["A. Joyful", "B. Content", "C. Cheerful", "D. All of the above"], "correct": "D"},
        {"question": "Find the error in the sentence: 'She can sings well.'", "options": ["A. Sings", "B. She", "C. Well", "D. No error"], "correct": "A"},
        {"question": "Which of these is a preposition?", "options": ["A. Quickly", "B. Under", "C. Happy", "D. Sing"], "correct": "B"},
        {"question": "Choose the word that is related to 'Weather':", "options": ["A. Rain", "B. Storm", "C. Forecast", "D. All of the above"], "correct": "D"},
        {"question": "Select the synonym for 'Beautiful':", "options": ["A. Ugly", "B. Attractive", "C. Smart", "D. Unattractive"], "correct": "B"},
        {"question": "Which word is the antonym of 'Generosity'?", "options": ["A. Greed", "B. Kindness", "C. Charity", "D. Love"], "correct": "A"},
    ],
    "Data Interpretation": [
        {"question": "What is the average of 4, 8, and 12?", "options": ["A. 8", "B. 10", "C. 12", "D. 6"], "correct": "A"},
        {"question": "What is the percentage increase from 20 to 40?", "options": ["A. 50%", "B. 60%", "C. 100%", "D. 200%"], "correct": "C"},
        {"question": "If a car travels 60 km in 2 hours, what is its average speed?", "options": ["A. 60 km/h", "B. 50 km/h", "C. 30 km/h", "D. 40 km/h"], "correct": "A"},
        {"question": "How many grams are in 2 kilograms?", "options": ["A. 2000", "B. 1000", "C. 500", "D. 100"], "correct": "A"},
        {"question": "What is the median of the set: {3, 7, 8, 10, 15}?", "options": ["A. 7", "B. 8", "C. 10", "D. 15"], "correct": "B"},
        {"question": "What is the range of the set: {3, 7, 8, 10, 15}?", "options": ["A. 15", "B. 10", "C. 12", "D. 5"], "correct": "C"},
        {"question": "What is 15% of 300?", "options": ["A. 35", "B. 45", "C. 50", "D. 55"], "correct": "B"},
        {"question": "If a box contains 5 red balls and 3 blue balls, what is the probability of drawing a red ball?", "options": ["A. 3/8", "B. 5/8", "C. 1/2", "D. 1/4"], "correct": "B"},
        {"question": "If the total amount of a company’s sales is $5000 and the expenses are $3000, what is the profit?", "options": ["A. $2000", "B. $3000", "C. $4000", "D. $5000"], "correct": "A"},
        {"question": "What is 25% of 400?", "options": ["A. 80", "B. 100", "C. 120", "D. 50"], "correct": "A"},
    ],
    "General Knowledge": [
        {"question": "Who was the first President of the USA?", "options": ["A. George Washington", "B. Abraham Lincoln", "C. John Adams", "D. Thomas Jefferson"], "correct": "A"},
        {"question": "Which planet is known as the Red Planet?", "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"], "correct": "C"},
        {"question": "What is the capital of Japan?", "options": ["A. Tokyo", "B. Beijing", "C. Seoul", "D. Kyoto"], "correct": "A"},
        {"question": "Who wrote 'Romeo and Juliet'?", "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"], "correct": "B"},
        {"question": "What is the tallest mountain in the world?", "options": ["A. Mount Everest", "B. Mount Kilimanjaro", "C. Mount Fuji", "D. Mount Elbrus"], "correct": "A"},
        {"question": "What is the largest ocean on Earth?", "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"], "correct": "D"},
        {"question": "What is the currency of the UK?", "options": ["A. Dollar", "B. Euro", "C. Pound", "D. Yen"], "correct": "C"},
        {"question": "What is the largest continent?", "options": ["A. Africa", "B. Asia", "C. Europe", "D. North America"], "correct": "B"},
        {"question": "What is the longest river in the world?", "options": ["A. Amazon", "B. Nile", "C. Mississippi", "D. Yangtze"], "correct": "B"},
        {"question": "Who is the inventor of the light bulb?", "options": ["A. Albert Einstein", "B. Nikola Tesla", "C. Thomas Edison", "D. Alexander Graham Bell"], "correct": "C"},
    ],
}

def run_quiz(module_name):
    """Run a test for a specific module."""
    st.header(f"{module_name} Test")
    score = 0
    user_answers = {}  # Store user answers
    
    # Display questions and options
    for i, q in enumerate(questions_db[module_name], start=1):
        st.subheader(f"{i}. {q['question']}")
        with st.expander("Select an option:"):
            # Ensure no option is selected by default
            answer = st.radio("", q['options'], key=f"{module_name}_{i}", index=None)
        user_answers[i] = answer
    
    if st.button("Submit"):
        # Evaluate the score based on answers
        for i, q in enumerate(questions_db[module_name], start=1):
            selected_answer = user_answers[i]
            correct_answer = q['correct']
            if selected_answer == q['options'][ord(correct_answer) - 65]:  # Compare with the correct option
                score += 1
        st.session_state[module_name] = score
        st.success(f"Your Score: {score}/{len(questions_db[module_name])}")
        return user_answers
    return None

def show_report():
    """Generate performance report."""
    st.header("Performance Report")
    scores = {module: st.session_state.get(module, 0) for module in modules}
    df = pd.DataFrame(list(scores.items()), columns=["Module", "Score"])
    
    fig = px.bar(df, x="Module", y="Score", title="Your Performance", color="Score", height=400)
    st.plotly_chart(fig)
    
    weak_areas = [module for module, score in scores.items() if score < 8]
    if weak_areas:
        st.warning(f"Focus on: {', '.join(weak_areas)}")
    else:
        st.success("Great job! You're performing well across all modules.")

def main():
    st.set_page_config(page_title="Aptitude Test App", layout="wide")
    st.title("🧠 Aptitude Test & Performance Analytics")
    
    choice = st.sidebar.radio("Select Test Phase", modules + ["Final Test", "View Report"])
    
    if choice in modules:
        run_quiz(choice)
    elif choice == "Final Test":
        st.header("Final Test (All Modules)")
        combined_questions = sum([questions_db[m] for m in modules], [])
        random.shuffle(combined_questions)
        final_score = 0
        user_answers = {}  # Store user answers
        
        # Display questions and options
        for i, q in enumerate(combined_questions[:10], start=1):  # Limiting to 10 questions for final test
            st.subheader(f"{i}. {q['question']}")
            with st.expander("Select an option:"):
                # Ensure no option is selected by default
                answer = st.radio("", q['options'], key=f"final_{i}", index=None)
            user_answers[i] = answer
        
        if st.button("Submit Final Test"):
            # Evaluate the final score
            for i, q in enumerate(combined_questions[:10], start=1):
                selected_answer = user_answers[i]
                correct_answer = q['correct']
                if selected_answer == q['options'][ord(correct_answer) - 65]:  # Compare with the correct option
                    final_score += 1
            st.session_state["Final Test"] = final_score
            st.success(f"Your Final Score: {final_score}/10")
    elif choice == "View Report":
        show_report()

if __name__ == "__main__":
    main()
