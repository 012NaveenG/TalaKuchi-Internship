import os
from decompile import decompile_apk_with_apktool
from recompile import recompile_apk_with_apktool
from take_Screenshot import take_screenshot
from modify_code import modify_file_content

search_words = [
    'android:debuggable="true"', 'android:allowBackup="true"', 'android:usesCleartextTrafic="true"', 'android:exported="true"',
    '.setJavaScriptEnabled(true)', '"google_api_key"', '"Google_Api_Key"', '"google_crash_reporting_api_key"',
    'websettings.setAllowFileAccess(true)', 'setPloginState()',  
    '.firebaseio.com']


# Specify the path to your APK
apk_path = input("Enter the path of the application: ")
decompiled_apk_dir = os.path.splitext(os.path.basename(apk_path))[0]

# Decompile the APK
decompile_apk_with_apktool(apk_path)

root_directory = f"./{decompiled_apk_dir}"

# Assuming other search words are intended for screenshot only and not for modification
screenshot_dir = f"./{decompiled_apk_dir}_Screenshots"

# Check and create the screenshot directory if not exists
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)


# take the screenshots from the resulting files 
for dirpath, _, filenames in os.walk(root_directory):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
      
        with open(filepath, "r", encoding="utf-8", errors="replace") as file:
            for line_number, line in enumerate(file, start=1):
                for search_word in search_words:
                    if search_word in line:
                        take_screenshot(filepath, screenshot_dir, line_number, search_word)

# Modify the content from the resulting files 
for dirpath, _, filenames in os.walk(root_directory):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
      
        with open(filepath, "r", encoding="utf-8", errors="replace") as file:
            for line_number, line in enumerate(file, start=1):
                for search_word in search_words:
                    if search_word in line:
                        modify_file_content(filepath)
                        

# Recompile the APK
# recompile_apk_with_apktool(decompiled_apk_dir)

print("Process completed!!")
