[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = kivyapp

# (str) Package domain (needed for android packaging)
package.domain = org.kivy

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let it empty to exclude all files)
#source.exclude_exts = spec

# (list) List of directory to exclude (let it empty to exclude all files)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions from source-files
#source.exclude_patterns = license, images/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pyjnius,android

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../../kivy

# (list) Permissions
#android.permissions = INTERNET

# (list) Features
#android.features = android.hardware.usb.host

# (list) Sundry options
#android.presplash_color = #FFFFFF

# (str) Orientation of your application
orientation = portrait

# (list) The Android archs to build for, for armeabi-v7a and arm64-v8a
android.archs = arm64-v8a, armeabi-v7a

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use Android X
android.androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact, storage, output
bin_dir = ./bin
