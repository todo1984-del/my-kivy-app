[app]

title = My Kivy App
package.name = mykivyapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# 安定動作実績のあるAPI/SDK設定
android.api = 31
android.minapi = 21
android.sdk = 31

# 互換性が最も高い NDK r23b を指定します
android.ndk = 23b
android.ndk_api = 21

android.accept_sdk_license = True
android.python_version = 3.11

[buildozer]
log_level = 2
warn_on_root = 1
