[**this file was originally located here**](https://docs.google.com/document/d/15nM9X0eWFdvy0PJBg230Rwo3XFstrA24aJVE9tW1lio/edit?usp=sharing)

---

## Day 1
studying for AP tomorrow
## Day 2
took AP
## Day 3
OK I actually accomplished things today. Went through the installation and quickstarts of both Rocket and Flask. Also drew out some wireframes of the home page. (Fig 1)
### Obstacles
I would kind of like items to come up in a preview modal when you click them on the browse page, but that’s,, a lot of work.
### Reading
* Flask quickstart: https://flask.palletsprojects.com/en/1.1.x/quickstart/
* Rocket quickstart: https://rocket.rs/v0.4/guide/getting-started/
* Rocket with sqlite: https://leonardoce.github.io/2018-03-22/rocket-tutorial-4
## Day 4
* Check-in with Candace and gang in the morning.
* Got flask running in development mode and played around with what happens when it encounters an error in development vs production modes. 
* Learned about setting environment variables on both Windows and Linux.
   * Powershell: `$env:[key] = [value]`
   * Windows: `set [key] = [value]`
   * Linux (at least bash (?)): `export [key] = [value]`
* Messed around with using WSL a bit — both in the VSCode integrated terminal and as a Remote to run a whole VSCode instance in. V fiddly, doesn’t seem worth it just to get a little comfortable with the Linux command line over the Powershell
### Questions
* Why does flask even have an option to give you a 404 if you accidentally append a trailing slash? (The docs claim is to prevent double-indexing by search engines… ??)
### Reading
* https://stackoverflow.com/questions/33241050/trailing-slash-triggers-404-in-flask-path-rule re: trailing slashes. provides global and by-route workarounds, and also explains rational a little better
* WSL stuff:
   * https://docs.microsoft.com/en-us/windows/wsl/wsl2-faq when it looks for targets, VSCode shows me “WSL (Legacy)” or something like that, so I thought I might need to upgrade?? This page talks about WSL 2
   * https://code.visualstudio.com/docs/remote/wsl talks specifically about the remote functionality
## Day 5
Continuing to work through the Flask quickstart. Wrote a run script in powershell (https://github.com/PiNerd3/i-lost-my-flask/blob/ee3e528c6749bcfcd4f36492a08e1f2e15712d7c/run.ps1) so I don’t have to set the environment variables all the time.


Flask quickstart talks about how in prod Flask should not be the program serving static files (https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files). This seems like a massive pain and something I will probably not get to. Nevertheless, marking possible TODO.


Tried to get curl working so I could hand-craft simple GET and POST requests and oh my god everything is horrible. The equivalent Powershell command is `Invoke-WebRequest`, but they do alias `curl` to it even though the syntax is completely different. And you can download an exe, but you have to put it on your PATH yourself,,, Looking at:
* https://superuser.com/questions/134685/run-curl-commands-from-windows-console
* https://superuser.com/questions/344927/powershell-equivalent-of-curl
* https://curl.haxx.se/windows/
* https://stackoverflow.com/questions/9507353/how-do-i-install-and-use-curl-on-windows
* https://devblogs.microsoft.com/commandline/tar-and-curl-come-to-windows/
and giving up for now.


Just realized that the UI I was kinda liking, with the slash and the two form inputs right on the home page, is probably confusing. You type in the name of a lost item — are you searching through the found items or adding a new lost one? And if it’s the latter, then the next page is,, the actual form, but with the first field already filled it? Except probably not correctly, bc you didn’t know how much detail to put. Hmmm.

I guess I should guide the user to searching through found items first (before reporting one lost), rather than trusting them to realize on their own that that would make sense.


Templating is kinda a lot. Still not 100% on how to turn off autoescaping with Jinja2, but as I can’t imagine I’m ever going to want to, I suppose that’s alright.


Think my next step is to go through the Flask tutorial, but build out I Lost My, rather than Flaskr. Similar type of app, so I think it should work. I do also want to do more with Rocket and explore if it might be a better idea.
Reading
* https://github.com/pallets/flask/issues/900, on Flask interpreting `%2F` in the URL as a path separator, rather than a literal `/`. Still does not feel like correct behavior to me, but whatever.
## Days, ah, 9 and 10
Took French AP this morning; had spent a bit of time earlier this week studying for it.


Early prototype is working! Copied a lot from the tutorial on creating Flaskr, but also had to diverge a bunch. 


I decided to get rid of authentication. Items will be write-once, read-only.


Trying to think of challenges I overcame. I feel like mostly where things break down is at the interfaces between different technologies and at different layers of the stack. Like, the database: I know very little about SQL, and I’m interacting with my database through the Flask wrapper of the python implementation of an SQLite3 server.


Jinja is annoying but I don’t think there’s really any better way to do it.


Not looking forward to styling. I copied the CSS from Flaskr, so it doesn’t actually look too bad, but it definitely doesn’t look right. Need to do some more brainstorming this weekend about what I want the look to be. Also kind of want to introduce a javascript framework? Vue is good, I think? I don’t like the idea of react just bc it’s by the bad blue website. I just kind of wish I could do modals for an item view instead of a separate `/item/<int:id>` route, and I don’t think rolling my own modals is the move. Something for the list.


Also spent a bunch of time today trying to get github to work?? I wanted to put this project on nhamovitz rather than PiNerd3 because I figured it would be something presentable and worthy of pride. But I’m already logged into PiNerd3 in the global git config, I guess? So you have to override it locally, but then you get to the Authentication Question, and evidently the Correct way to solve that is NOT with a Personal Access Token, even though they obviously exist so I’m not sure what’s bad about them, but by using SSL, which only requires one token (which I think is your public key?) Anyway I have an SSL key on my computer now the repo is Not pushed to github. This was another of those ultimately inconclusive hour-or-two \[dives\] into something that seems deeply weird (and likely to be black magic) to me. Probably not the most effective pedagogical or autodidactic model, but they are interesting experiences.


Also I decided on Flask with Python rather than anything else (particularly also-in-the-running was Rust with Rocket) sometime between the last entry and this one; should explain why.
1. I’m more familiar right now with Python than with Rust, despite (I think) ultimately liking Rust more
   1. ↪ Writing it out, I realize that this is a great argument for doing it with Rocket — have knowledge of two things instead of one, kickstart personal growth in a direction you’re excited about — but,, well. I would be very interested in porting it. Maybe I could even do benchmarks!
2. Flask has better getting-started documentation. (Rocket does probably have better documentation overall; I haven’t really spent time with it, but it’s Rust, and Flask’s isn’t great.)


Was just typing out some todos and I realized the doc is kinda messy. Maybe I should start a trello board!
## Day 11
Spent some time today organizing the github situation. I now only have one account! And I’m giving up on using ssh. I set up a Personal Access Token and am using that
## Day 12
Past-me left me with some fuckery around templating, so I had to fix that. I just stashed the changes and moved on.


Added mostly UX improvements, as well as “Resolved” functionality.


Thinking about the moderation and management problem(s). The way I would want this to work if it was being purpose built for MA; if it was being built for what I envision at MA but scoped to, say, high schools in general; and if it was being built as the most generic lost-and-found management possible . . . are three different designs. Not 100% sure which one I’m pursuing.


Here’s the commit at the end of today: https://github.com/nhamovitz/i-lost-my-flask/tree/f43366513ecd680d6707c55581293ba89bfc13a8

## Writeup
### Overview of project (150-250 words)
For my senior project, I chose to design and build a simple webapp, called “I Lost My ___!”, to aid in the management of a lost-and-found. My day-to-day tasks consisted mostly of writing and debugging code and designing the visual look of the webapp, taking into account user experience and aesthetics. I also spent a lot of time consulting documentation and tutorials — I had to learn a lot that I didn’t know before starting the project. I was already familiar with Python and the basics of the Flask web development framework, but I had to learn about SQL (including SQLite and the python sqlite3 module), CSS styling, and more advanced uses of Flask. There was also a lot more \[administrative\] work than I was expecting. Setting up my development environment required learning weird finicky details about Visual Studio Code, SSH keys, and authentication with Github.
### Reflection
This was a good passion project for me, for all the reasons I thought it would be. It allowed me to develop my skills in Python and in web development by working in the intersection of those two technologies. It exposed me to new concepts and required that I learn new skills. A project like this would be good for a student with an eye for detail who wants to improve their programming skills. (I don’t think it would be advisable for someone who had never programmed before, considering the not-inconsiderable level of comfort I already possessed and the amount I achieved.) Unfortunately, there were several proposed/maybe features that didn’t make it: automatic matching between the description of lost items and found items and automatic email rollups, to name two. I also wasn’t able to develop the UI as much as I would have liked. However, I’m proud of the product I do have and I think it’s a good, although rather simplistic, app. That change of mindset from the disappointment of realizing something wouldn’t be possible is one case where I had to adapt.
My favorite part of this project was being forced to reckon with the nitty-gritty details of a bold idea. This is somewhat surprising because many of those reckonings concluded with me discarding or significantly changing that original idea. There are two possible lessons to learn there: spend time really thinking about things and considering all the depth and ramifications of your plan before you execute; or get right into the doing, because flaws are always going to reveal themselves then that weren’t obvious before, and you might as well get it over with. These are at odds with each other, and I’m not sure which one I think is a better philosophy. Maybe the key is to not strike a balance? Either do very little planning, or very much; avoid doing some. If I were to do it over again, I think I’d try more planning. (But the time after that, maybe I’d try less!)