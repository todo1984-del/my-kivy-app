[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source files where the let's go (relative to directory of spec)
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# explicitly use python3 and kivy
requirements = python3,kivy

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 31

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API to use for NDK.
android.ndk_api = 31

# (bool) Skip android SDK license confirmation
android.accept_sdk_license = True

# 安定してビルドしやすいようにPythonのバージョンを3.11に固定します
android.python_version = 3.11


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
