import os
import psutil
import platform

def get_shell():
    current_process = psutil.Process()
    parent = current_process.parent()
    parent_name = parent.name().lower()
    
    # windows
    # todo: untested
    if platform.system() == 'Windows':
        if 'powershell' in parent_name:
            return 'powershell'
        elif 'cmd' in parent_name:
            return 'cmd'
        elif 'bash' in parent_name or 'git-bash' in parent_name:
            return 'bash'
        elif 'wsl' in parent_name:
            return 'wsl'
        else:
            return parent_name.replace('.exe', '')
    else:
        return parent_name

if __name__ == "__main__":
    shell = get_shell()
    print(f"current shell: {shell}")