import requests
from pydantic import BaseModel, Field
from typing import Optional


class Request(BaseModel):
    article_number: int = Field(description="Assigning a number to a fetched article")
    article_url: Optional[str] = Field(
        default="https://www.datarobot.com/blog/",
        description="Url of the desired article, by default the url is the datarobot blog",
    )

    def get_html(self):
        """
        get_html is a method to get the html code of a given webpage, storing it in the windows folder and naming the page with a personnalized number

        self: a Request type object
        """

        response = requests.get(self.article_url)

        if response.status_code == 200:
            html_content = response.text

            with open(
                f"./windows/article_{self.article_number}.html", "w", encoding="utf-8"
            ) as file:
                file.write(html_content)
