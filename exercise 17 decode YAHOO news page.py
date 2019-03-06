#sandygcabanes
#practicepython.org
#exercise 17 decode YAHOO news page
"""Decode A Web Page
This is the first 4-chili exercise of this blog! We’ll see what people think,
and decide whether or not to continue with 4-chili exercises in the future.
Exercise 17 (and Solution)
Use the BeautifulSoup and requests Python packages to print out a list of all
the article titles on the YAHOO news page.
"""

#url https://news.yahoo.com/
import requests
url = 'https://news.yahoo.com/'
r = requests.get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text)

for story_heading in soup.find_all(class_="Lh(15px) Fw(b) LineClamp(3,45px) D(i)--sm1024 Pend(10px)--sm1024"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())

"""
Output March 6, 2019 10 am UTC +8
UserWarning: No parser was explicitly specified, so I'm using the best
available HTML parser for this system ("lxml"). This usually isn't a problem,
but if you run this code on another system, or in a different virtual
environment, it may use a different parser and behave differently.

The code that caused this warning is on line 18 of the file ...
exercise 17 decode YAHOO news page.py.
To get rid of this warning, pass the additional argument 'features="lxml"'
to the BeautifulSoup constructor.
  soup = BeautifulSoup(r.text)

'I thought I was gone': This Alabama woman didn't think she'd make it out of the tornado alive
'I Thank The Lord.' 72-Year-Old Thankful After Tornado Destroyed Her House in Beauregard, Alabama
House Democrats to call for vote on condemning 'anti-Semitic' Ilhan Omar comments
Rep. Steve Scalise: Nancy Pelosi has to remove Rep. Ilhan Omar from the Foreign Affairs Committee
80 arrests made, including a reporter and 3 clergy members, during Sacramento police shooting protest
California attorney general will not charge Sacramento police officers in shooting death of Stephon Clark
What's Next for U.S.-North Korea Negotiations?
America Must Move Past Its “Sputnik” Moment on North Korea—Or Else
Rep your favorite MLB team with St. Patrick's Day-inspired gear
Get lucky: Affordable St. Patrick's Day decor for every room in the house
Joanna Gaines' Diet Is Surprisingly Easy to Follow
J.Lo Invites Joanna Gaines to Tour Her New Home After She 'Fangirled' Over the Fixer Upper Star
See Meghan Markle and Kate Middleton Reunite at the Queen's Palace Party for Prince Charles
From Beach Dresses to Ballgowns, Meghan Markle's Maternity Style Is Totally on Point
The Morgan Plus Six in Photos
2020 Morgan Plus Six Brings Traditional Styling Together With BMW Z4 Power
'Alarming' number of migrants crossing border: Official
Arrests on US-Mexico border spike as critics warn Trump approach to security 'encourages illegal migration'
Pro-Israel and Jewish groups demand Rep. Ilhan Omar be removed from Foreign Affairs Committee
Bari Weiss on anti-Semitism in America
How Warren Buffett Views Kraft Heinz after the Fall
Kraft Heinz (KHC) to Expand Customer Base With Farmstead Deal
President Trump vows to sign an executive order to guarantee free speech at colleges and universities
Trump's plan to protect free speech on college campuses
Sisters found alive after weekend lost in Humboldt County wilderness
Young sisters found alive after 2 days in the woods
Tesla blames misprinted label for China customs hiccup
Tesla shifts gears, leaving fate of St. Louis stores uncertain
We will have the 'Southwest Effect' for Hawaii flights, says Southwest CEO
Tickets on sale now for new Southwest Airlines Hawaii flights beginning March 17
Ghosn lawyer says he's optimistic former Nissan head could soon win bail
Carlos Ghosn: Ex-Nissan boss granted 1 billion yen bail by Japanese court
Correction: Vatican-Pius XII story
Pope Pius XII: Vatican to open secret archives on WWII-era pontiff accused of silence on Holocaust
Trump Counterpunches Sweeping Democratic House Probe: 'They Didn't Give One Letter of the Requests'
Sean Spicer on reports he is on list of people Democrats want documents from to investigate Trump
World's first electric 'hypercar' unveiled, and it's the most powerful road legal car ever
A new $2 million all-electric 'hypercar' accelerates faster than an F-16 jet
U.S. Closes Jerusalem Consulate and Downgrades Its Diplomatic Mission to Palestine
Flag comes down on U.S. Palestinian mission in Jerusalem
Maryland Man Claimed Panhandler Killed Good Samaritan Wife, but Now He and Daughter Are Charged
Husband, step-daughter charged in slaying to be extradited
"""

