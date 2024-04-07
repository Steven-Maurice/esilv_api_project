from bs4 import BeautifulSoup


def return_5_most_recent(html_content):
    """
    return_5_most_recent scraps the content of a html code to get all the urls of Generative AI and AI in the news articles

    :html_content: The html code of the main webpage

    :return: A list of the first 5 urls in str format
    """

    soup = BeautifulSoup(html_content, "lxml")

    ai_news_urls = []

    for a_tag in soup.find_all(
        "a",
        class_="uk-card uk-card-default uk-card-hover uk-card-animation uk-flex uk-flex-column uk-overflow-hidden uk-position-relative uk-card-blog-related",
    ):
        if a_tag.find("span", string="Generative AI") or a_tag.find(
            "span", string="AI in the News"
        ):
            ai_news_urls.append(a_tag["href"])

    return ai_news_urls[:5]
