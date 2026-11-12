"""Gera uma página de redirecionamento por vídeo a partir de links.json.

Uso: python3 build.py  -> cria/atualiza <slug>/index.html para cada vídeo.
Para trocar o destino de um QR code, edite o campo "youtube" (ID do vídeo)
em links.json, rode o script e faça commit/push. O QR impresso não muda.
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).parent

REDIRECT = """<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>{titulo}</title>
<meta http-equiv="refresh" content="0; url={url}">
<script>location.replace({url_js});</script>
</head><body style="font-family:system-ui,sans-serif;padding:2rem">
<p>Abrindo <a href="{url}">{titulo}</a>…</p>
</body></html>
"""

PENDENTE = """<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>{titulo} - em breve</title>
</head><body style="font-family:system-ui,sans-serif;padding:2rem;max-width:32rem;margin:auto;text-align:center">
<h1 style="font-size:1.4rem">{titulo}</h1>
<p>Este vídeo estará disponível em breve. Tente novamente mais tarde.</p>
</body></html>
"""


def main():
    videos = json.loads((ROOT / "links.json").read_text(encoding="utf-8"))
    for v in videos:
        titulo = html.escape(v["titulo"])
        if v.get("youtube"):
            url = f"https://youtu.be/{v['youtube']}"
            page = REDIRECT.format(titulo=titulo, url=url, url_js=json.dumps(url))
        else:
            page = PENDENTE.format(titulo=titulo)
        out = ROOT / v["slug"] / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(page, encoding="utf-8")
    (ROOT / "index.html").write_text(
        '<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<meta name="robots" content="noindex"><title>TKD</title></head><body></body></html>\n',
        encoding="utf-8",
    )
    print(f"{len(videos)} páginas geradas")


if __name__ == "__main__":
    main()
