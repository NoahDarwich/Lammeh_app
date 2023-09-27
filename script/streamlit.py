import streamlit as st
import pandas as pd


class User:
    def __init__(self, name, offers_df, needs_df):
        self.name = name
        self.offers_df = offers_df
        self.needs_df = needs_df

    def can_help(self, other_user):
        for skill in self.offers_df.index:
            if skill in other_user.needs_df.index:
                return True
        return False

    def needs_help_from(self, other_user):
        for need in self.needs_df.index:
            if need in other_user.offers_df.index:
                return True
        return False

class Matcher:
    def __init__(self, users):
        self.users = users

    def find_matches(self):
        matches = []
        for user in self.users:
            for other_user in self.users:
                if user != other_user and user.can_help(other_user) and other_user.needs_help_from(user):
                    matches.append((user, other_user))
        return matches


def match_user(name, skills, needs):
    # Load the needs and skills datasets
    skills_df = pd.read_csv('./raw_data/skills.csv')
    needs_df = pd.read_csv("./raw_data/needs.csv")

    # Create a user object
    user = User(name, skills_df.loc[skills_df["name"] == name], needs_df.loc[needs_df["name"] == name])

    # Create a matcher object and find the matches
    matcher = Matcher([user])
    matches = matcher.find_matches()

    return matches




new_user = {}

with st.form('form'):
    name = st.text_input("What is your name?")
    submitted = st.form_submit_button("Submit")
if submitted:

    st.write(f'Hi {name}, What are you here for today?')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Offering")
        if st.button('offer'):
            st.write('offer')

    with col2:
        st.header("Need smth")
        if st.button('need'):
            st.write('need')

    with col3:
        st.header("Browse")
        if st.button('browse'):
            st.write('browse')





def ask_user_questions():
    # name =  st.text_input("What is your name?")
    # skills = st.multiselect("What are your skills?", ["programming", "design", "writing", "marketing"])
    # needs = st.multiselect("What do you need help with?", ["programming", "design", "writing", "marketing"])

    #return name, skills, needs
    pass


# def display_results(matches):
#     if matches:
#         st.write("Here are the people that can help you:")
#         for match in matches:
#             st.write(f"* {match[1].name} can help you with {match[1].skills_df.index}")
#     else:
#         st.write("Sorry, we couldn't find any matches.")


#if __name__ == "__main__":

    # Ask the user questions
    #name, skills, needs = ask_user_questions()

    # Match the user with other users
    #matches = match_user(name, skills, needs)

    # Display the results to the user
    # display_results(matches)
