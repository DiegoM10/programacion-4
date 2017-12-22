from tweepy import Stream, OAuthHandler, API, Cursor
from tweepy.streaming import StreamListener
from tweepy.models import User
import json
import sqlite3
db = sqlite3.connect('prueba')
cursor = db.cursor()
try:
    cursor.execute('''CREATE TABLE usuario(ID INT PRIMARY KEY, nombre
    TEXT, tweets TEXT, creado TEXT)''')
except Exception as e:
    print('Tabla creada')
    pass
conKey= 'V21dzqhxiS8AyIpO7H11ihGDM'
consecret = 'L8jBC600KFnuV4T2lsVB9TcKXy8NB8buLKZBbhyIFeF99QzOGM'
atoken = '250447042-JKFlrTnX5P465AJ3FgzAiWbfBEtz2mT5e0DD1j8L'
asecret = 'rmVvWzI5OSKBWrPexilg4Yqh1W0KeEeA61Y1l46sN91qU'

auth = OAuthHandler(conKey, consecret)
auth.set_access_token(atoken,asecret)

api = API(auth)

class TLListener(StreamListener):
    def on_data(self, raw_data):
        data = json.loads(raw_data)
        status = User.parse(self.api, data)
        location = status.user['location']
        if location == None:
            location = 'No Activado'
            print(location)
        # ------------------#
        print(location)
        print(status)
        # print(status.user['name']+': '+ status.text)
        creado = status.created_at
        id = status.id
        nombre = status.user['name']
        tweet = status.text
        cursor.execute('''INSERT INTO USUARIO(ID, nombre, tweets, creado) VALUES(?,?,?,?)''', (id, nombre, tweet, creado))
        db.commit()
        return (True)

    def on_error(self, status_code):
        if status_code == 420:
            return False

try:
    twStream = Stream(auth, TLListener())
    twStream.filter(track=['#PANAMA'])
except Exception :
    pass