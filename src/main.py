from channels import CHANNELS
from collector import get_feed
from history import mark_as_sent
from mailer import send_newsletter
from newsletter import generate_html


def main():

    all_videos = []

    for name, config in CHANNELS.items():
        all_videos.extend(get_feed(name, config))

    if not all_videos:
        print("Nenhum vídeo novo encontrado. Nenhum e-mail foi enviado.")
        return

    html = generate_html(all_videos)

    with open("newsletter.html", "w", encoding="utf-8") as file:
        file.write(html)

    send_newsletter(html)
    mark_as_sent([video["video_id"] for video in all_videos])

    print(f"{len(all_videos)} vídeos encontrados e enviados por e-mail.")


if __name__ == "__main__":
    main()
