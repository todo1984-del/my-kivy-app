#
# Buildozer specification
#

[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source where the main.py lives
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern
#source.include_patterns = assets/*.png,images/*.jpg

# (list) Source files to exclude (let it empty to include all files)
#source.exclude_exts = spec

# (list) List of directory to exclude (let it empty to include all files)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern
#source.exclude_patterns = license,images/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# specify python3 and kivy as requirements
requirements = python3,kivy

# (list) Custom source folders for requirements
#requirements.source.dirname =

# (list) Permissions
#android.permissions = INTERNET

# (list) Features
#android.features = android.hardware.usb.host

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PYTHON_SCRIPT,NAME2:ENTRYPOINT_TO_PYTHON_SCRIPT

#
# OSX Specific
#

#
# author = © Your Name

# (str) Full name used for application signing
#osx.sign.identity = "Developer ID Application: Your Name (DDDDDDDDDD)"


#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (default #000000)
#android.presplash_color = #000000

# (string) Desired orientation (landscape, portrait, sensor, full-user)
#android.orientation = portrait

# (list) List of Java files to add to the android project (can be specifying a directory or a file)
#android.add_jars = foo.jar,path/to/vec/*.jar

# (list) List of gradle dependencies to add
#android.gradle_dependencies =

# (list) Add a custom java class to be called from Python
#android.add_src =

# (list) List of additional android manifest attributes
#android.manifest.attributes =

# (list) List of additional android manifest intent-filters
#android.manifest.intent_filters =

# (list) Experimental manifest placeholders, format key:value, one per line
#android.manifest.placeholders = ['key': 'value']

# (list) Gradle repositories to add {ex: maven { url 'https://oss.sonatype.org/content/repositories/snapshots/' } }
#android.gradle_repositories =

# (list) packaging options to add/exclude, if gradle merge conflict occurs
#android.packaging_options = exclude 'META-INF/NOTICE.LICENSE'

# (list) List of assets to pack with the application
#android.assets.exts =

# (list) List of custom templates for the application
#android.template =

# (str) Android NDK version to use
#android.ndk_version = 25b

# (int) Android API to use
#android.api = 33

# (int) Minimum API your APK will support
#android.min_api = 21

# (str) Android SDK version to use
#android.sdk_version = 33

# (str) ADT version to use
#android.adt_version = 20200519

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name to use for adb ubiquity
#android.app_identity = org.example.myapp

# (bool) Use AndroidX for support libraries
android.androidx = True

# (list) Pattern to whitelist for allowed files
#android.whitelist =

# (bool) If True, then skip trying to update the Android SDK
#android.skip_sdk_update = False

# (str) Path to a custom SDK
#android.sdk_path =

# (str) Path to a custom NDK
#android.ndk_path =

# (str) Path to a custom Ant
#android.ant_path =

# (str) If True, sharing libraries will be packaged as a single fat library
#android.fat_aar = True

# (str) python-for-android branch to use, if not master
#p4a.branch = master

# (str) ABC is an Python-for-android git clone to use (instead of downloading)
#p4a.src =

# (list) Additional python-for-android whitelist files
#p4a.whitelist_exclude =

# (str) Name of a master/custom distribution to use
#p4a.distribution = default

# (str) Extra command line arguments for p4a
#p4a.extra_args =

#
# Python for android (p4a) specific
#

# (str) The format in which to release your app (aab or apk)
#android.release_artifact = apk

# (str) The format in which the apk should be debug (aligned or unaligned)
#android.apk_format = signed


[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1

# (str) Path to build artifact, default is .buildozer in the dir
#bin_dir = ./bin

# (str) Path to build dependencies (CWD by default)
#build_dir = ./.buildozer

# (str) Buildozer global cache directory
#android.accept_sdk_license = True
