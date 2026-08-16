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

# (list) Source files to exclude (let it empty to exclude all files)
#source.exclude_exts = spec

# (list) List of directory to exclude (let it empty to exclude all files)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,pyjnius

# (list) Custom source folders for requirements
#requirements.source.dirname =

# (list) Permissions
#android.permissions = INTERNET

# (list) Keywords
#keywords =

# (str) Source orientation (portrait, landscape or all)
orientation = portrait

# (list) List of services
#android.services =

#
# Android specific
#

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.min_api = 21

# (str) Android SDK version to use
android.sdk = 33

# (str) Android build tools version to use
android.build_tools_version = 33.0.2

# (str) Android NDK version to use
#android.ndk = 25b

# (bool) Indicate if the application should be background service or not
#android.service = False
