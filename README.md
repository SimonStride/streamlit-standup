# Streamlit Standup

Simple [Streamlit App](https://www.streamlit.io/) to scrum-master my AM standups for me!

Let's face it, making sure everyone sticks to 2 minutes is tedious. I'd rather be listening to the *content* of what the team are saying than clock-watching.

Plus, I have been known to sometimes forget teammates. Not intentionally, honest! Long term sleep deprivation is a PITA.

Enter the standup-helper, running on Streamlit. In the Post-Lockdown-World of sat-down-standups and zoom screen-sharing, it takes the pressure off remembering the clock. And the team.

Feel free to use or fork away - please let me know if the streamlit-standup is the saviour of your morning standup. And your team.

Maintained by Simon Stride [https://github.com/SimonStride/streamlit-standup](https://github.com/SimonStride/streamlit-standup)

## Prequisites

Python 3.6+
Streamlit ([https://www.streamlit.io/](https://www.streamlit.io/))
Tested on Windows & Linux

````powershell
# Windows
pip install streamlit

# Linux
pip3 install streamlit
````

## Running the Standup

First, clone the repo

````powershell
# Windows & Linux
git clone [https://github.com/SimonStride/streamlit-standup.git](https://github.com/SimonStride/streamlit-standup.git)
````

Next, configure **your** team members in standup.py.

````powershell
# Windows PowerShell & Linux bash
cd streamlit-standup

streamlit run standup.py
````

The standup host will start in a new browser window automatically, normally [http://localhost:8501](http://localhost:8501)

Optionally, expand the sidebar the left to change the amount of time everyone gets.

Click "Start the standup" to cycle through the team members. When the timer expires it will automatically proceed to the next available team member.

Once all teammates have been checked off the app will display "All Done - Have a great day!". I recommend replacing this message with a ridiculous meme, maybe a funny cat picture, an Arnie quote or something Die Hard's John McClane might say. It might motivate the team - who knows, YMMV.

For more info on tweaking the code or building your own Streamlit app go to [https://www.streamlit.io/](https://www.streamlit.io/)

Or read the docs at [https://docs.streamlit.io/en/latest/](https://docs.streamlit.io/en/latest/)

## Testing

Normally for production code, I'd want to Pytest this. And virtualenv of course.

But:

1. This is a pet project *just for fun*
2. It's only about 30 lines of code! Seriously, the README file is twice as long as the app itself.

Enjoy.
