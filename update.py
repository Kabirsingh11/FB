import os,sys



PERINTAH = """
cd $HOME
cd FB
mv data $HOME
mv results $HOME
cd
rm -rf FB
git clone https://github.com/Kabirsingh11/FB
cd $HOME
mv data FB
mv results FB
cd FB
"""

print(" |-->....")
os.system(PERINTAH)
print(' |')
print(' |')
print(' |-->Update Script done ...')
print(' |-->Please Run This Command: python main.py')
os.sys.exit()

