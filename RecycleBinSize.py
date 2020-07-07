import os
os.chdir("C:\\")
print("CWD = "+os.getcwd())
bin_size = os.popen('dir /s "$Recycle.Bin"').read().split("Total Files Listed:\n")[1].split("(s)")[1].split("bytes")[0].strip()
bin_size = float("".join(bin_size.split(",")))
print(f"{bin_size} in bytes\n{bin_size/1024} in Kb\n{bin_size/(1024*1024)} in Mb\n{bin_size/(1024*1024*1024)} in Gb")
input("Press Any Key To Exit...")
