import streamlit as st
from time import sleep

# Optional - add Scrum Master last!
teammates = ["Alice", "Bob", "Charlie", "Danielle", "Edward", "Scrum Master"]

start_standup = st.checkbox(label="Start the standup", key="cb_start")
name_badge = st.empty()
time_remaining = st.empty()

# frequency at with the clock and progress bar update. NOT SCIENTIFICALLY ACCURATE!
scale = 100
patience = st.sidebar.slider(
    label="How long does everyone get?", min_value=0, max_value=120, value=120
)

my_bar = st.progress(0)
if start_standup:
    for teamname in teammates:
        chk = st.checkbox(teamname, False, teamname)
        name_badge.header(teamname)

        for i in range(0, patience * scale):
            if chk:
                break
            time_remaining.header(f"{round(patience-i/scale, 2)}")
            my_bar.progress(1 - i / (patience * scale))
            sleep(1 / scale)

    # Optional - add a less cheesy message or even a hilarious cat meme
    name_badge.header("All Done - Have a great day!")
