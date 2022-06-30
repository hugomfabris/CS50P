import re

def main():
    print(parse(input("HTML: ")))

def parse(link):

    matches = re.search(r'src="https?:\/\/(www)?\.?youtube\.com\/embed\/(.+)"', link, re.IGNORECASE)

    if matches:
        return f"https://youtu.be/{matches.group(2)[0:11]}"

if __name__ == "__main__":
    main()

#<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
#<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#https://www.youtube.com/embed/xvFZjo5PgG0

#https://youtu.be/xvFZjo5PgG0