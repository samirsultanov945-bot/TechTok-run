[app]

title = TechTok Run
package.name = techtokrun
package.domain = org.techtok

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav

version = 0.4

requirements = python3,kivy

orientation = landscape
fullscreen = 1

android.permissions = VIBRATE,INTERNET,ACCESS_WIFI_STATE,ACCESS_NETWORK_STATE

android.api = 34
android.minapi = 21
android.accept_sdk_license = True

[buildozer]
log_level = 2
