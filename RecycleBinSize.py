import os
os.chdir("C:\\")
print("CWD = "+os.getcwd())
a = os.popen('dir /s "$Recycle.Bin"').read().split("Total Files Listed:\n")[1].split("(s)")[1].split("bytes")[0].strip()
a = float("".join(a.split(",")))
print(f"{a} in bytes\n{a/1024} in Kb\n{a/(1024*1024)} in Mb\n{a/(1024*1024*1024)} in Gb")
input("Press Any Key To Exit...")
"""
https://stackoverflow.com/questions/12813826/get-folder-size-from-windows-command-line
...However, this has several problems because cmd is limited to 32-bit signed integer arithmetic. 
So it will get sizes above 2 GiB wrong...
https://www.daniweb.com/programming/software-development/code/216951/size-of-a-file-folder-directory-python
https://stackoverflow.com/questions/483864/windows-command-for-file-size-only
https://weblogs.asp.net/jongalloway/top-10-dos-batch-tips-yes-dos-batch
"""