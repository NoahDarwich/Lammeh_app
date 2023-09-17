import streamlit as st


def ask_user_questions():
    name = st.text_input("What is your name?")
    skills = st.multiselect("What are your skills?", ["programming", "design", "writing", "marketing"])
    needs = st.multiselect("What do you need help with?", ["programming", "design", "writing", "marketing"])

    return name, skills, needs


def display_results(matches):
    if matches:
        st.write("Here are the people that can help you:")
        for match in matches:
            st.write(f"* {match[1].name} can help you with {match[1].skills_df.index}")
    else:
        st.write("Sorry, we couldn't find any matches.")


if __name__ == "__main__":
    # Ask the user questions
    name, skills, needs = ask_user_questions()

    # Match the user with other users
    matches = match_user(name, skills, needs)

    # Display the results to the user
    display_results(matches)
