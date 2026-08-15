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

# (list) List of inclusions using patternmatching
#source.include_patterns = assets/*,images/*.jpg

# (list) List of exclusions using patternmatching
#source.exclude_patterns = license,images/*.jpg

# (list) List of directory to exclude from distribution
#source.exclude_dirs = tests, bin

# (list) List of extensions to exclude from distribution
#source.exclude_exts = spec

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivymd
requirements = python3,kivy,https://github.com/kivy/python-for-android/archive/master.zip

# (str) Custom source folders for requirements
#requirements.source.dir = ../../kivy

# (list) Permissions
#android.permissions = INTERNET

# (list) Features
#android.features = android.hardware.usb.host

# (list) Target architectures
# Supported values: arm64-v8a, armeabi-v7a, x86, x86_64
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

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
#android.app_class_name = org.kivy.android.PythonActivity

# (str) Supported orientations (landscape, sensorLandscape, reverseLandscape, portrait, reversePortrait, sensorPortrait, fullSensor, user)
orientation = portrait

# (list) List of service to declare
#android.services = NAME:package.to.Activites.and.service_name

# (bool) Whether to be a service (True) or a application (False)
#android.isservice = False

# (str) The Android arch to build for, for APKs you can choose arm64-v8a, armeabi-v7a, x86, x86_64
# For aab you can include multiple separated by comma
#android.arch = arm64-v8a

# (list) Extra xml to add to the AndroidManifest.xml (uses aapt)
#android.manifest.extra_xml =

# (list) Extra xml to add to the AndroidManifest.xml (uses manifest merger)
#android.manifest.merger_extra_xml =

# (list) Extra jars to add to the libs dir
#android.gradle_dependencies =

# (str) The andriod 'ndk_path' should be automatically found if not set here.
#android.ndk_path =

# (str) The andriod 'sdk_path' should be automatically found if not set here.
#android.sdk_path =

# (str) ANT path
#android.ant_path =

# (bool) If True, then skip building python-for-android
#android.skip_build = False

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) OU = Organization Unit, O = Organization, C = Country
#android.issuer = CN=Me, OU=MyStuff, O=Me, C=FR

# (str) Keystore password
#android.keystore_password =

# (str) Key password
#android.key_password =

# (bool) Enable Android auto backup
android.uses_auto_backup = False

# (str) The format in which an APK is released, can be 'apk' or 'aab'
android.release_artifact = apk


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug command)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact, storage for downloaded packages
#bin_dir = ./bin

# (str) Path to build directory
#build_dir = ./.buildozer

# (bool) Indicate whether the build should be run in a virtualenv (ignored)
#build_venv = True
