"""
This is a program which scraps the FRIENDS transcript from a webite and creates a folder with all the dialouges in seperate episode files.
When the user enters a dialouge or even a PART of a dialouge, it will first check if all the episodes are present and then ask the user to enter the dialogue. If the dialouge is present, it will show the episode title and the season number and episode number.
If the dialouge is not found, it will show an appropriate message. 
"""

# Trying to install required modules and importing them.
for ch in list(range(2)):
	try:
		import os
		import glob
		import requests
		from lxml import html,etree
	except ImportError:
		os.system('python -m pip install requests')
		os.system('python -m pip install lxml')

# Checking the path where the episode files are to be saved.
def checkpath():
    try:
        currentpath=os.getcwd()
        if 'transcript' in os.listdir(currentpath):
            os.chdir("transcript")
        else:
            if 'transcript' in os.listdir(os.chdir("..")):
                os.chdir(os.getcwd()+'\\transcript')
            else:
                os.mkdir(currentpath+'\\transcript')
                os.chdir(currentpath+'\\transcript')
    except Exception as e:
        print(e)

# Accepting the dialouge and performing a search in all the log files.
def finddialogue():
    flag=0
    dialogue=input("Enter The Dialogue!!!\t -->  ").lower()
    for item in glob.glob("*.log"):
        try:
            file=open(item,"r",encoding="utf8")
            file.seek(0)
            titleepisode=file.readline().split("\t")[0]
            for line in file:
                if dialogue in line:
                    flag=1
                    print(f"\n\"{line}\", will appear in \"{titleepisode}\" which is in Season = {item[:2]}, Episode = {item[2:4]}")
                else:
                    pass
        except Exception as e:
            print(e)
    if flag==0:
        print("Are you sure it's a F.R.I.E.N.D.S dialouge?")
        finddialogue()

# Downloading all the log files.
def downloadalllogs():
    baseurl="https://fangj.github.io/friends/"
    homepage=requests.get(baseurl)
    homepagetree=html.fromstring(homepage.content)
    allepisodes=homepagetree.xpath("//*/a")
    episodelist=[]
    for episode in allepisodes:
        episodelist.append(episode.values())
    print("Downloading all logs")
    for i in range(len(episodelist)):
        seaepi=episodelist[i][0].split("/")[1].split(".")[0]
        season=seaepi[:2]
        episode=seaepi[2:]
        print(f"Fetching : {season}.{episode}")
        episodepage=requests.get(baseurl+episodelist[i][0])
        episodetree=html.fromstring(episodepage.content)
        episodecontent=episodetree.xpath("//p")
        pagetitle=episodetree.xpath("//title/text()")
        myfile=open(season+episode+".log","w+",encoding="utf-8")
        myfile.write("Episode Title : "+''.join(pagetitle)+"\t")
        for p in episodecontent:
            myfile.write((p.text_content()).lower()+"\n")
        print(f"{season}.{episode} Done!")
        myfile.close()
    print("All Files Present Finding Dialogue")

# Upcoming feature!
def downloadmissinglogs():
    print("Downloading missing logs (future implementation)")

# Main function
checkpath()
if(228==len(glob.glob("*.log"))):
    finddialogue()
elif(len(glob.glob("*.log"))<228 and len(glob.glob("*.log"))!=0):
    downloadmissinglogs()
    finddialogue()
else:
    downloadalllogs()
    finddialogue()
input("Exit")
