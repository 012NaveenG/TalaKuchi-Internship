import subprocess


def run_command(command):
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def recompile_apk_with_apktool(decompiled_apk_dir):
    print(f"Recompiling APK...")
    command = f"apktool b {decompiled_apk_dir} -o {decompiled_apk_dir}.apk"
    run_command(command)

