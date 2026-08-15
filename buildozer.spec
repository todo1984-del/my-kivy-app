[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source files where the include_exts is located
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,https://github.com/kivy/python-for-android/archive/master.zip

# (list) Target architectures
android.architectures = arm64-v8a, armeabi-v7a

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 31

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is typically the same as minapi.
android.ndk_api = 31

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Supported orientations
orientation = portrait

# (bool) Enable Android auto backup
android.uses_auto_backup = False

# (str) The format in which an APK is released, can be 'apk' or 'aab'
android.release_artifact = apk

# (bool) Indicate whether the screen should stay on
#android.wakelock = False

# (str) Android SDK license acceptance (重要：ここでライセンスに自動同意します)
android.accept_sdk_license = True


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug command)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
