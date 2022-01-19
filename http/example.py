import os.path

from botcity.plugins.http import BotHttpPlugin

URL = 'https://httpbin.org'

http = BotHttpPlugin(URL + '/get')
http.set_params({'user': '12345678'})
http.add_param('Authorization', 'Bearer xD')

print(http.get().text)
print(http.get_as_json())

HOME_PATH = os.path.expanduser('~')
FILE_PATH = os.path.join(HOME_PATH, 'file.json')
print(http.get_as_file(FILE_PATH))

http = BotHttpPlugin(URL + '/post')
http.set_params({'user': '12345678'})
http.add_param('Authorization', 'Bearer xD')
print(http.post().text)
