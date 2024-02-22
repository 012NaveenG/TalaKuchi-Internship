import subprocess



def run_command(command):
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def decompile_apk_with_apktool(apk_path):
    print(f"Decompiling APK...")
    command = f"apktool d {apk_path} "
    run_command(command)

