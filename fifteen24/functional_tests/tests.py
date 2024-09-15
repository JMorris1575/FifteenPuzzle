from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import login
from django.contrib.auth.models import User

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import os, time


class InitialVisitTests(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        online_server = os.environ.get('ONLINE_SERVER')
        if online_server:
            self.live_server_url = 'http://' + online_server        # this may need to change to "https://"

    def tearDown(self):
        self.browser.quit()

    def test_authentication(self):
        # Charlie has decided to try out the Fifteen Puzzle program and goes to its homepage
        self.browser.get(self.live_server_url)

        # He comes to a login page
        self.assertIn('Login', self.browser.title)

        # He notices two entry boxes, one with "username" and the other with "password" as their placeholder texts
        username_inputbox = self.browser.find_element(By.ID, "username_input")
        password_inputbox = self.browser.find_element(By.ID, "password_input")
        self.assertEqual(username_inputbox.get_attribute("placeholder"), "Enter username")
        self.assertEqual(password_inputbox.get_attribute("placeholder"), "Enter password")

        # Uncle Jim sent him his login information but, because it is unusual, he makes a small mistake in entering the
        # password and is returned to the login page that includes a friendly message encouraging him to try again
        charlie = User.objects.create_user("Charles", password="password")
        username_inputbox.send_keys('Chales')
        password_inputbox.send_keys('pAssword')
        login_button = self.browser.find_element(By.ID, 'login_button')
        login_button.click()
        self.assertIn('Login', self.browser.title)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertIn("Sorry, I'm pretty finicky about usernames and passwords.", page_text)

        # He tries again and enters the correct username and password and arrives at the games entry page
        username_inputbox = self.browser.find_element(By.ID, "username_input")
        password_inputbox = self.browser.find_element(By.ID, "password_input")
        username_inputbox.send_keys('Charles')
        password_inputbox.send_keys('password')
        login_button = self.browser.find_element(By.ID, "login_button")
        login_button.click()
        self.assertIn('Fifteen Entry', self.browser.title)

    def test_anonymous_user_cannot_reach_entry_page(self):
        # A friend of Charlies sees him playing the game and thinks he can get in by going directly to /fifteen/entry/
        # but he is redirected back to the login page.
        self.browser.get(self.live_server_url + '/fifteen/entry/')
        self.assertIn('Login', self.browser.title)

    def test_appearance(self):
        # Charlie pauses to notice the appearance of the web page.
        # There is a header at the top giving the title of the game
        charlie = User.objects.create_user("Charles", password="password")
        login('/fifteen/entry/', charlie)
        self.browser.get('/fifteen/entry/')
        self.browser.find_element(By.TAG_NAME, 'header')

        # and a greeting that welcomes him by name.

        # there is also a logout button next to his name.

        # Finally, there is a footer at the bottom giving some information about who wrote the program.

    def test_logout(self):
        # After playing the game for a while he decides to log out so his Dad can play it at the same computer.
        # He sees a "Logout" button in the header at the top of the screen.
        pass

