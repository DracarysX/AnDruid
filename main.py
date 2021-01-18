from andruid.core.parse.apk.apk import Apk


apk = Apk('/home/shahar/Workspace/Research/Android/Applications/betfair/betfair-wrapper-sportsbook.apk', 'extracted_apk_andruid')
print(apk.get_package_name())
print(apk.get_app_names())
print(apk.get_activity_names())