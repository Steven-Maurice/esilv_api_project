import requests
from pydantic import BaseModel, Field
from typing import Optional


class Request(BaseModel):
    article_number: int = Field(description="Assigning a Number to a fetched article")
    article_url: Optional[str] = Field(
        default="https://www.datarobot.com/blog/",
        description="Url of the desired article, by default the url of datarobot blog about AI and ML",
    )

    def get_html(self):
        response = requests.get(self.article_url)

        if response.status_code == 200:
            html_content = response.text

            with open(
                f"./windows/article_{self.article_number}.html", "w", encoding="utf-8"
            ) as file:
                file.write(html_content)
