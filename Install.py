#!/usr/bin/env python3

import os
import pwd
import sys

try:
    os.system('figlet -f cosmic "START " | lolcat')
except Exception:
    print("""
     .::::::.:::::::::::::::.    :::::::.. ::::::::::::
    ;;;`    `;;;;;;;;'''';;`;;   ;;;;``;;;;;;;;;;;;''''
    '[==/[[[[,    [[    ,[[ '[[,  [[[,/[[['     [[
      '''    $    $$   c$$$cc$$$c $$$$$$c       $$
     88b    dP    88,   888   888,888b "88bo,   88,
      "YMmMY"     MMM   YMM   ""` MMMM   "W"    MMM
    """)


def get_username():
    return pwd.getpwuid(os.getuid())[0]

requirement = "requirements.txt" # the real requiremet file is too long so I use testrequirement.txt for testing 
user        = get_username()
parent_dir  = "/home/"+user
config      = ".config"
build       = ".build"
local       = ".local"
fonts       = ".fonts"
vim         = ".vim"
icons       = ".icons"
Icons       = "icons"
rofi        = "rofi"
polybar     = "polybar"
i3          = "i3"
mpd         = "mpd"
sub_build   = "build"
bkchanger   = "bkchanger"
runcpp      = "runcpp"
luky        = "luky.sh"
printscreen = "printscreen.sh"
Bin         = "bin"
scripts     = "scripts"
share       = "share"

# email    = input("[needed to config git!]What is your email : ")
# username = input("[needed to config git!]What is your username : ")
email      = "modymu9@gmail.com"
username   = "mmubarak0"

config_directory        = os.path.join(parent_dir, config)
build_directory         = os.path.join(parent_dir, build)
local_directory         = os.path.join(parent_dir, local)
rofi_directory          = os.path.join(build_directory, rofi)
polybar_directory       = os.path.join(build_directory, polybar)
rofi_build_directory    = os.path.join(rofi_directory, sub_build)
polybar_build_directory = os.path.join(polybar_directory, sub_build)
i3_conf                 = os.path.join(config_directory, i3)
mpd_conf                = os.path.join(config_directory, mpd)
polybar_conf            = os.path.join(config_directory, polybar)
rofi_conf               = os.path.join(config_directory, rofi)
local_bin               = os.path.join(local_directory, Bin)
local_share             = os.path.join(local_directory, share)


def current_path():
    return (os.getcwd())

DowPath                 = current_path()
dow_local               = os.path.join(DowPath, local)
dow_local_share         = os.path.join(dow_local, share)
scripts_directory       = os.path.join(DowPath, scripts)

# # Changing the CWD
# os.chdir('../')
# # If any of the intermediate level
# # directory is missing
# os.makedirs() method will create them
# # Get the list of all files and directories
# # in the root directory
# path = "/"
# dir_list = os.listdir(path)
# print(dir_list)
# # output Files and directories in ' / ' :
# # ['sys', 'run', 'tmp', 'boot', 'mnt', 'dev', 'proc', 'var', 'bin', 'lib64', 'usr',
# # 'lib', 'srv', 'home', 'etc', 'opt', 'sbin', 'media']
# # get size of file
# os.path.getsize("filename")


# Printing CWD after
print("the current working directory is : \n")
print(DowPath)
print("\nWarning this must have to match '~/path/to/My_Dot_Files/' Directory")
print("press any key to continue")
unix = input("Do you want to continue ?  ")

if (unix != 'y' and unix != 'yes'):
    print("Stop Installing process please make sure to type (yes) or (y) to continue")
    sys.exit("If User home directory dosen't match please refer to https://example.com")
else:
    print("Continue ... ")


# install missing package or requierd by install script
with open(requirement, 'r') as requierd_package:
    data = requierd_package.read()

install = []
miss = []
print("you can just hit enter to say yes")
for i in list(data.split("\n")):
    ans = input("Do you want to install "+i+" ? [y/n]")
    if (ans == "y" or ans == ""):
        install.append(i)
    else:
        miss.append(i)
print("the following package will not be installed type\
   the full name to package you want to add seperated by spaces or just pass")
print(miss)
addmiss = input("What do you wanna add : ")
try:
    os.system('figlet -f NScript "wait ..." | lolcat')
except Exception:
    print("""
                                                                
                                        I8                      
                                        I8                      
                                gg  88888888                   
                                ""     I8                      
  gg    gg    gg     ,gggg,gg   gg     I8                      
  I8    I8    88bg  dP"  "Y8I   88     I8                      
  I8    I8    8I   i8'    ,8I   88    ,I8,                     
  ,d8,  ,d8,  ,8I  ,d8,   ,d8b,_,88,_ ,d88b,      d8b  d8b  d8b 
  P""Y88P""Y88P"   P"Y8888P"`Y88P""Y888P""Y88     Y8P  Y8P  Y8P 
                                                              
          """)
# installing the package
c = ' '.join(map(str, install))
print('sudo apt install %s %s' %(c, addmiss))
os.system('sleep 3')
os.system('sudo apt install %s %s' %(c, addmiss))

# # package that require build from source
# check if build directory is exist
if os.path.exists(build_directory):
    print("build directory is already have been created continue ...")
else:
    os.makedirs(build_directory)

# changing the working directory to build directory
os.chdir(build_directory)

# # # # # # # # # #  rofi  # # # # # # # # # #
# replace print with os.system               #
def rofi_is_installed():
    return os.path.exists(rofi_directory)

if rofi_is_installed():
    print('rofi installation was founded pass ')  # Finish
else:
    print('git clone --recursive https://github.com/davatorium/rofi.git')
    os.system('git clone --recursive https://github.com/davatorium/rofi.git')
    print("done ")

    if os.path.exists(rofi_build_directory):
        pass
    else:
        os.makedirs(rofi_build_directory)

    # switch to rofi directory
    os.chdir(rofi_directory)

    print('git pull')
    os.system('git pull')
    print('done ')  # Done
    print('git submodule update --init')
    os.system('git submodule update --init')
    print('done ')  # Done
    print('autoreconf -i')
    os.system('autoreconf -i')
    # switch to rofi build directory
    os.chdir(rofi_build_directory)
    print(current_path())

    print('../configure --disable-check')
    os.system('../configure --disable-check')
    print('done ')  # Done
    print('make')
    os.system('make')
    print('done ')  # Done
    print('sudo make install')
    os.system('sudo make install')
    print('finished rofi is installed succesfully ')  # Finish
os.system('sleep 3')

# changing the working directory to build directory
os.chdir(build_directory)

# # # # # # # # # #  polybar  # # # # # # # # # #
# replace print with os.system                  #
def polybar_is_installed():
    return os.path.exists(polybar_directory)

print(current_path())
if polybar_is_installed():
    print('polybar installation was founded pass ')  # Finish
else:
    print('git clone --recursive https://github.com/polybar/polybar')
    os.system('git clone --recursive https://github.com/polybar/polybar')
    print("done ")

    if os.path.exists(polybar_build_directory):
        pass
    else:
        os.makedirs(polybar_build_directory)

    # switch to polybar build directory
    os.chdir(polybar_build_directory)

    print('cmake ..')
    os.system('cmake ..')
    print('done ')  # Done
    print('make -j(nproc)')
    os.system('make -j(nproc)')
    print('done ')  # Done
    print('sudo make install')
    os.system('sudo make install')
    print('finished polybar is installed succesfully ')  # Finish
os.system('sleep 3')

# # # # # # # # # #  mpd  # # # # # # # # # #
# TODO config mpd to work properly          #
print('sudo systemctl disable mpd')
print('sudo systemctl stop mpd.service')
print('sudo systemctl stop mpd.socket')


# # # # # # # # # #  git  # # # # # # # # # #
# TODO config git to work properly          #
print('git config user.email "%s"' % email)
print('git config user.name "%s"' % username)


# |copy| [i3, mpd, polybar, rofi] TODO : [fish, omf] to ~/.config/ folder

# switch to download path where config file is alocated
os.chdir(DowPath)
# create a backup directory
backup_dir = "your_old_conf_backup"
if os.path.exists(backup_dir):
	print(backup_dir)
else:
	os.makedirs(backup_dir)

if os.path.exists(config_directory):
	print(config_directory)
else:
	os.makedirs(config_directory)

# check for old configuration if exists remove it from indx 
# then backup indx folders
indx = [i3, mpd, polybar, rofi]
appendx = [i3, mpd, polybar, rofi]
for File in os.listdir(config_directory):
	if File in indx:
		indx.remove(File)
for i in indx:
	os.makedirs(os.path.join(config_directory, i))
for i in appendx:
	if i not in indx:
		print('cp -R %s %s' %((os.path.join(config_directory, i)), backup_dir))
        os.system('cp -R %s %s' %((os.path.join(config_directory, i)), backup_dir))
print(" Backups Done ☯  ☻  ☯ ")
os.system('sleep 10')

# copy config folders to .config folder
print('cp -R %s %s' %(i3, config_directory))
os.system('cp -R %s %s' %(i3, config_directory))
print('cp -R %s %s' %(mpd, config_directory))
os.system('cp -R %s %s' %(mpd, config_directory))
print('cp -R %s %s' %(polybar, config_directory))
os.system('cp -R %s %s' %(polybar, config_directory))
print('cp -R %s %s' %(rofi, config_directory))
os.system('cp -R %s %s' %(rofi, config_directory))
print(" configrations Done ☯  ☻  ☯ ")
os.system('sleep 3')



# |copy| scripts to ~/.local/bin/

# switch to scripts path where config file is alocated
os.chdir(scripts_directory)

if os.path.exists(local_bin):
	print(local_bin)
else:
	os.makedirs(local_bin)

print('cp -R %s %s' %((os.path.join(scripts_directory, bkchanger)), local_bin))
os.system('cp -R %s %s' %((os.path.join(scripts_directory, bkchanger)), local_bin))
print('cp -R %s %s' %((os.path.join(scripts_directory, runcpp)), local_bin))
os.system('cp -R %s %s' %((os.path.join(scripts_directory, runcpp)), local_bin))
print('cp -R %s %s' %((os.path.join(scripts_directory, luky)), local_bin))
os.system('cp -R %s %s' %((os.path.join(scripts_directory, luky)), local_bin))
print('cp -R %s %s' %((os.path.join(scripts_directory, printscreen)), local_bin))
os.system('cp -R %s %s' %((os.path.join(scripts_directory, printscreen)), local_bin))
print(" scripts Done ☯  ☻  ☯ ")
os.system('sleep 3')




# |copy| .fonts & .icons TODO .vim to ~/
# Then running install script to some vim plugins

# switch to download path where config file is alocated
os.chdir(DowPath)

# check for old .files if exists remove it from indx 
# then backup indx folders
indx = [fonts, vim, icons]
appendx = [fonts, vim, icons]
for File in os.listdir(parent_dir):
	if File in indx:
		indx.remove(File)
for i in indx:
	os.makedirs(os.path.join(parent_dir, i))
for i in appendx:
	if i not in indx:
		print('cp -R %s %s' %((os.path.join(parent_dir, i)), backup_dir))
print(" Backups Done ☯  ☻  ☯ ")
os.system('sleep 10')

# copy dot folders to home folder
print('cp -R %s %s' %(icons, parent_dir))
os.system('cp -R %s %s' %(icons, parent_dir))
print("  ")
# ------------------------- FIX Not impelented yet --------------- #
#   For Now copy them manually the size is too big                 #
#   print('cp -R %s %s' %(fonts, parent_dir))                      #
#   print('cp -R %s %s' %(vim, parent_dir))                        #
#   print(" Should I add those to the script ?  ")                #





# TODO |copy| icons to ~/.local/share/   $$ I am not sure if this is necessary

# switch to download path where config file is alocated
os.chdir(DowPath)

if os.path.exists(local_share):
	print(local_share)
else:
	os.makedirs(local_share)

indx = [Icons]
appendx = [Icons]
for File in os.listdir(local_share):
	if File in indx:
		indx.remove(File)
for i in indx:
	os.makedirs(os.path.join(local_share, i))
for i in appendx:
	if i not in indx:
		print('cp -R %s %s' %((os.path.join(local_share, i)), backup_dir))
print(" Backups Done ☯  ☻  ☯ ")
os.system('sleep 10')

# copy icons folders to home folder
os.chdir(dow_local_share)
print('cp -R %s %s' %(Icons, local_share))
os.system('cp -R %s %s' %(Icons, local_share))
print("  ")




try:
    os.system('figlet -f NScript "END" | lolcat')
except Exception:
    print("""

         ***** **         ***** *     **          ***** **
      ******  **** *   ******  **    **** *    ******  ***
     **   *  * ****   **   *  * **    ****   **    *  * ***
    *    *  *   **   *    *  *  **    * *   *     *  *   ***
        *  *             *  *    **   *          *  *     ***
       ** **            ** **    **   *         ** **      **
       ** **            ** **     **  *         ** **      **
       ** ******        ** **     **  *         ** **      **
       ** *****         ** **      ** *         ** **      **
       ** **            ** **      ** *         ** **      **
       *  **            *  **       ***         *  **      **
          *                *        ***            *       *
      ****         *   ****          **       *****       *
     *  ***********   *  *****               *   *********
    *     ******     *     **               *       ****
    *                *                      *
     **               **                     **


            """)
os.system('sleep 3')
os.system('i3 restart')
