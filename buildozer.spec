[app]
title = TechTok Run
package.name = techtokrun
package.domain = org.techtok
source.dir = .
source.include_exts = py
version = 0.4
requirements = python3,kivy==2.3.0
orientation = landscape
fullscreen = 1
android.permissions = VIBRATE, INTERNET, ACCESS_WIFI_STATE, ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
