from channels import CHANNELS
from collector import get_feed
from newsletter import generate_html


def main():

    all_videos = []

    for name, config in CHANNELS.items():
        all_videos.extend(get_feed(name, config))

    html = generate_html(all_videos)

    with open("newsletter.html", "w", encoding="utf-8") as file:
        file.write(html)

    print(f"{len(all_videos)} vídeos encontrados.")
    print("Newsletter criada com sucesso!")


if __name__ == "__main__":
    main()