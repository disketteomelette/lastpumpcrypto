import urllib.request
import time
import requests

def enviar_telegram(mensaje_bot):
    bot_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    bot_chatid = '-XXXXXXXXX'
    url_final = 'https://api.telegram.org/botXXXXXXXXXX:' + bot_token + '/sendMessage?chat_id=' + bot_chatid + '&parse_mode=Markdown&text=' + mensaje_bot
    respuesta = requests.get(url_final)
    return respuesta.json()

# porcentaje a partir del cual el bot avisa (float)
minvariacion = 9.0
weburl = urllib.request.urlopen("http://cryptoprediction.io")
htmlsrc = str(weburl.read()).replace("<tr ", "\n").split(sep='\n')
elemento: str
resultado: str
resultado = ""

# --- DOMINANCIA ---
dom1 = urllib.request.urlopen("https://bitcoindominance.com/")
dom2 = str(str(dom1.read()).replace("<tr ", "\n").split(sep='\n'))
dom3 = dom2.split(sep='<p class="InfoBoxstyled__Content-sc-1nim0p3-2 dPHYLX">')[1].split(sep='<!--')[0] + " %"
# --- FIN DOMINANCIA ---

try:
    for elemento in htmlsrc[1:]:
        m1 = elemento.replace('<td class="text-left">', "@").replace('<span class="b"', "@").replace('<span style="color:', "@").split(sep="@")
        ca = m1[1].replace('grey">', '').replace("</span></td>", "")
        v1 = elemento.replace('" class="text-center"><span style="color:', "@").replace('</span></td>', "@").split(sep="@")[3].split(sep=";")[1]
        if float(v1.split(sep="%")[0]) >= minvariacion:
            msgalerta = "+" + str(v1) + " " + str(ca) # + " +info: " + str(link)
            resultado = resultado + msgalerta + "\n"
except:
    resultado = "📈 Cryptos subidas > " + str(minvariacion) + "% 📈 \n\n" + resultado + "\n\n" + "Dominancia BTC: " + dom3
    test = enviar_telegram(resultado)
    print(test)
    time.sleep(2600)
