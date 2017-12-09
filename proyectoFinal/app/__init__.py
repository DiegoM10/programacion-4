from flask import Flask, render_template,redirect, request
import http.client
import json,requests

app = Flask('__name__')

@app.route('/',methods =['GET'])
def init():
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': '6f89e625709d4b11af33273c70007ae9', 'X-Response-Control': 'minified'}

    #connection.request('GET', '/v1/competitions', None, headers)
    connection.request('GET', '/v1/competitions/445/fixtures', None, headers)
    response = json.loads(connection.getresponse().read().decode())

    connection.request('GET', '/v1/competitions/455/fixtures', None, headers)
    resulbbva = json.loads(connection.getresponse().read().decode())

    connection.request('GET', '/v1/competitions/456/fixtures', None, headers)
    resulserieA = json.loads(connection.getresponse().read().decode())

    connection.request('GET', '/v1/competitions/452/fixtures', None, headers)
    resulbundes = json.loads(connection.getresponse().read().decode())

    connection.request('GET', '/v1/competitions/450/fixtures', None, headers)
    resulligue = json.loads(connection.getresponse().read().decode())

    connection.request('GET', '/v1/competitions/445/leagueTable', None, headers)
    premier = json.loads(connection.getresponse().read().decode())

    connection.request('GET', '/v1/competitions/455/leagueTable', None, headers)
    bbva = json.loads(connection.getresponse().read().decode())

    connection.request('GET', '/v1/competitions/452/leagueTable', None, headers)
    bundes = json.loads(connection.getresponse().read().decode())

    connection.request('GET', '/v1/competitions/456/leagueTable', None, headers)
    serieA = json.loads(connection.getresponse().read().decode())

    connection.request('GET', '/v1/competitions/450/leagueTable', None, headers)
    ligue = json.loads(connection.getresponse().read().decode())

    if request.method == 'GET':
        try:
            return render_template('init.html',premier = premier['standing'],bbva = bbva['standing'],
                                   bundes = bundes['standing'], serieA = serieA['standing'],ligue = ligue['standing'],response = response['fixtures'],
                                   resulbbva = resulbbva['fixtures'], resulserieA = resulserieA['fixtures'],
                                        resulbundes = resulbundes['fixtures'], resulligue = resulligue['fixtures'])
        except Exception as e:
            print(e)
    return render_template('init.html')

if __name__ == '__main__':
    app.run(debug=True)
