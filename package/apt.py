import subprocess
import re

def get_autoremoveable():
    process = subprocess.Popen(['sudo', 'apt', '--dry-run', 'autoremove'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True)
    stdout, stderr = process.communicate()
    
    #print(stdout, stderr)

    removeable = list() 
    for line in stdout.split("\n"):
        if "Remv" in line:
            remv_found = True
            package = line
            package = package.replace("Remv", "")
            package = package.split("[")
            removeable.append(package[0].strip())
            print("Removeable packages: \n", removeable)
        else:
            remv_found = False
    if remv_found:
        return removeable
    else:
        print("No packages to remove")
        return False
        