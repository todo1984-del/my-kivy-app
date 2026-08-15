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

android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.ndk_api = 21
android.accept_sdk_license = True
android.python_version = 3.11

# --- 追加：メモリ不足による強制終了を防ぐためのGradle設定 ---
android.gradle_options = -Dorg.gradle.jvmargs="-Xmx1536m" -Dorg.gradle.workers.max=1
# -------------------------------------------------------------

[buildozer]
log_level = 2
warn_on_root = 1
