from jproperties import Properties

config = Properties()
file_obj = codecs.open ('C:\\Users\\Vignesh\\Cucumber_AutomationBytes\\Booking\\Config.Properties', 'rb')
with open('C:\\Users\\Vignesh\\Cucumber_AutomationBytes\\Booking\\Config.Properties', 'rb') as config_file:
    config.load(config_file)
print(config.get("user"))

items_view = config.items()
for item in items_view:
    print(item[0], '=', item[1].data)
