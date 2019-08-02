from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized type of browser - %s" % browser)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def open_project_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and len(
                wd.find_elements_by_name("manage_proj_create_page_token")) > 0):
            wd.get('http://localhost/mantisbt-1.2.20/manage_proj_page.php')

    def stop(self):
        self.wd.quit()

