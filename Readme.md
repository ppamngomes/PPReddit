# Data request visualizer

For many months I've been just following ThePPShow. Haven't had any time to contribute to the community,
mostly because I didn't think I had enough knowledge to contribute besides tinfoil.
Now that reddit decided to try to kill the community, I thought this is where I can actually come in and
do a little contribution.

I created this tool as a way to create an archive of the data that Reddit blocked people from seeing by 
banning the subreddit.

This tool pretty much all it does it to convert a reddit data request into a html page so that it's 
a bit easier to see the posts that were in reddit sub.

Below are the instructions on how to use the tool. If you want to use the tool but don't know how I am 
happy to help whenever I have time. Feel free to DM me on X @ArturNGomes

What you need: 
- Python
- Internet connection (to download the dependencies)
- Reddit request zip file (https://www.reddit.com/settings/data-request) - use GDPR version



Setup:
------
These are instructions for windows.

Install Python.

Using the Windows terminal to create a virtual environment and install dependencies:

````commandline
cd <project_directory>
python -m venv env 
env\Scripts\activate
pip install -r requirements.txt
````

Then all you have to do is run:
(Replace reddit_data with the name of the file from the reddit data request)
````commandline
python main.py <reddit_data> 
````

The output will be generated in a data folder. You should be able to open the file for example amngomes.html
on your browser right away. You'll only be able to see your own posts.
If you want to contribute to the archive let me know and I can add to the main repository.

