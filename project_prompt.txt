Your team should create a web app using Flask which uses prompt engineering to generate useful responses to specific user queries.

Due date: Sunday 19 March before midnight.

Motivation: gpt-based webapps using prompt engineering have already started to appear and this assignment is meant to help you learn how to write such apps as well as gaining experience using git for a team project.

Steps:
1) create a team repository (if you haven't already)
2) create a folder in the repository called ca01
3) copy the gptwebapp.py and gpt.py files from lesson15 to ca01
4) each team member should add a method to gpt.py which accepts some text, adds a prompt to the front, sends it to gpt, and returns the response,
     e.g. get_refactor(code) -- would add the prompt "Refactor the following Python program so that all functions have fewer than 5 lines of code: \n\n"
5) modify the gptwebapp.py to include
   a) an about page which explains what your program does
   b) a "team" page which has a short bio of each member of the team and what their role was
   c) an index page with links to each of the team-members pages
   d) a form page for each team member which ask the user for some input, then calls the appropriate GPT method to get the response, which it sends back to the browser.
6) each team member should create a short movie (1-2 minutes) showing them running the app on their computer and trying out their prompt engineering page
7) each team member uploads a link to the team github and a link to their individual movie (stored in google drive with permisions so anyone with the link can access it),