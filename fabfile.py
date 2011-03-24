from fabric.api import hosts, run, sudo, local
from fabric.contrib.console import confirm
from fabric.utils import puts,warn

DEV_PROVISIONING_UUID = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
DEV_SIGN = "Mobi Ten"
DEV_APP_NAME = "Gym Mama"
DEV_APP_ID = 'com.mobiten.gym_mama'

TITANIUM_SDK_VERSION = '1.5.1'
IPHONE_SDK_VERSION = '4.2'
DEVICE_FAMILY = 'iphone'
BUILDER = "/Library/Application\ Support/Titanium/mobilesdk/osx/%s/iphone/builder.py" % (TITANIUM_SDK_VERSION)


def coffee():
	local("coffee --watch -o Resources/js/ --compile App/*.coffee ", False)

def debug():
	local("%s simulator %s ./ %s %s %s" % (BUILDER,IPHONE_SDK_VERSION,DEV_APP_ID,DEV_APP_NAME,DEVICE_FAMILY), False)

def device():
	local("%s install %s ./ %s %s %s" % (BUILDER,IPHONE_SDK_VERSION, DEV_APP_ID, DEV_APP_NAME, DEV_PROVISIONING_UUID, DEV_SIGN))

def package():
	print "nothing"
	
def clean():
	if confirm("Clean will delete any files that is ignored by gitignore\nand also any files that not yet tracked by git.\nAre your sure you want to continue ?",default=False):
		warn("Deleting Untracked and Ignore Files, you have been WARNED!")
		local("git clean -d -f")
		local("mkdir -p build/iphone")
		
		puts("Project is now clean.")
	else:
		warn("CLEAN IS CANCELLED.") 
