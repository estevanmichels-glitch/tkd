# tkd

Redirecionadores dos vídeos de taekwondo (bal gisul e poomsae, 10º ao 1º gub) usados nos QR codes.

Cada QR aponta para `https://estevanmichels-glitch.github.io/tkd/<slug>/`, que redireciona para o vídeo no YouTube.
Para trocar o destino: edite `links.json`, rode `python3 build.py` e faça push. O QR impresso não precisa mudar.
