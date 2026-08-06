from datetime import datetime


def generate_html(videos):
    today = datetime.now().strftime("%d/%m/%Y")

    html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Music Weekly</title>
</head>
<body style="font-family: Arial, sans-serif; max-width: 700px; margin: 40px auto; line-height:1.6">

<h1>🎵 Music Weekly</h1>
<p>Edição de {today}</p>

<hr>
"""

    current_channel = None

    for video in videos:

        if video["channel"] != current_channel:
            current_channel = video["channel"]
            html += f"<h2>{current_channel}</h2>"

        html += f"""
<p>
<a href="{video['link']}">
{video['title']}
</a>
</p>
"""

    html += """
</body>
</html>
"""

    return html
