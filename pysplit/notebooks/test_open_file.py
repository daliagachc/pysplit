# project name: pysplit
# created by diego aliaga daliaga_at_chacaltaya.edu.bo

# %%
import pysplit
# %%
file1 = "/Users/diego/Library/Application Support/JetBrains/Toolbox/apps/IDEA-U/ch-0/192.7142.36/IntelliJ IDEA.app/Contents/bin/~/pysplit/example_data/Archive/hysplit2014090100.traj"

print('sdf')
hydata, pathdata, header, datetime, multiple_traj = pysplit.load_hysplitfile(file1)