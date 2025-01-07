# TESTING DOCUMENTATION

### Content

1. [Validation](#validation)  
    - [HTML](#html-validation)  
    - [CSS](#css-validation)  
    - [Python](#python-validation)  
2. [Lighthouse](#lighthouse)  
3. [Automated Testing](#automated-testing)  
4. [Manual Testing](#manual-testing)  
    - [Devices](#devices)  
    - [Browsers](#browsers)  
    - [Responsiveness](#responsiveness)  
    - [Feature Testing](#feature-testing)  

---

## 1. Validation <a name="validation"></a>

### HTML Validation <a name="html-validation"></a>
The HTML code was validated using the [W3C Validator](https://validator.w3.org/). This ensures that the HTML structure adheres to modern standards, free from syntax errors and compatibility issues.

**Home** (home.html)
![HTML Validator About](./testing_images/html_validator_home.png)

**Memories** (memories.html)
![HTML Validator Memories](./testing_images/html_validator_memories.png)

**Post Details** (post_detail.html)
![HTML Validator Post](./testing_images/html_validator_post.png)

**About** (about.html)
![HTML Validator About](./testing_images/html_validator_about.png)

**Favourites** (favourites_list.html)
![HTML Validator Favourites](./testing_images/html_validator_favourites.png)

**Login** (login.html)
![HTML Validator Login](./testing_images/html_validator_login.png)

**Sign up** (signup.html)
![HTML Validator Signup](./testing_images/html_validator_signup.png)

**Logout** (logout.html)
![HTML Validator Logout](./testing_images/html_validator_logout.png)

**Edit Post** (edit_post.html)
![HTML Validator Edit Post](./testing_images/html_validator_edit_post.png)

**Delete Post** (delete_post.html)
![HTML Validator Delete Post](./testing_images/html_validator_delete_post.png)

**Edit Comment** (edit_comment.html)
![HTML Validator Edit Comment](./testing_images/html_validator_edit_comment.png)

**Delete Comment** (delete_comment.html)
![HTML Validator Delete Comment](./testing_images/html_validator_delete_comment.png)


### CSS Validation <a name="css-validation"></a>
The CSS was validated using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). This process ensures proper styling practices and compatibility across browsers.

**Home** (home.css)
![CSS Validator About](./testing_images/css_validator_home.png)

**Memories** (memories.css)
![CSS Validator Memories](./testing_images/css_validator_memories.png)

**Post Details** (post_detail.css)
![CSS Validator Post](./testing_images/css_validator_post.png)

**About** (about.css)
![CSS Validator About](./testing_images/css_validator_about.png)

**Favourites** (favourites_list.css)
![CSS Validator Favourites](./testing_images/css_validator_favourites.png)

**Login** (login.css)
![CSS Validator Login](./testing_images/css_validator_login.png)

**Sign up** (signup.css)
![CSS Validator Signup](./testing_images/css_validator_signup.png)

**Logout** (logout.css)
![CSS Validator Logout](./testing_images/css_validator_logout.png)

**Edit Post** (edit_post.css)
![CSS Validator Edit Post](./testing_images/css_validator_edit_post.png)

**Delete Post** (delete_post.css)
![CSS Validator Delete Post](./testing_images/css_validator_delete_post.png)

**Edit Comment** (edit_comment.css)
![CSS Validator Edit Comment](./testing_images/css_validator_edit_comment.png)

**Delete Comment** (delete_comment.css)
![CSS Validator Delete Comment](./testing_images/css_validator_delete_comment.png)

### Python Validation <a name="python-validation"></a>
The Python code was checked for errors using [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) to ensure it follows PEP 8 standards and is free from major syntax issues or inefficiencies.

**manage.py**
![Python Validator manage.py](./testing_images/pep8_manage.png)

**models.py**
![Python Validator models.py](./testing_images/pep8_models.png)

**views.py**
![Python Validator views.py](./testing_images/pep8_views.png)

**urls.py**
![Python Validator models.py](./testing_images/pep8_urls.png)

**forms.py**
![Python Validator models.py](./testing_images/pep8_forms.png)

---

## 2. Lighthouse <a name="lighthouse"></a>
[Lighthouse](https://developers.google.com/web/tools/lighthouse/) audits were performed to evaluate the website’s performance, accessibility, best practices, and SEO. Each metric was reviewed, and adjustments were made to improve the scores where necessary.

---

## 3. Automated Testing <a name="automated-testing"></a>
Automated testing was conducted using tools like [pytest](https://docs.pytest.org/) and [Selenium](https://www.selenium.dev/). These tests covered various functionalities, ensuring key features worked as expected under different scenarios.

---

## 4. Manual Testing <a name="manual-testing"></a>

### Devices <a name="devices"></a>
The application was tested on various devices, including:  
- Mobile phones (iPhone, Android)  
- Tablets (iPad, Galaxy Tab)  
- Desktop computers  

This ensured functionality and responsiveness across a wide range of screen sizes.

### Browsers <a name="browsers"></a>
Testing was carried out on major web browsers, such as:  
- [Google Chrome](https://www.google.com/chrome/)  
- [Mozilla Firefox](https://www.mozilla.org/firefox/)  
- [Safari](https://www.apple.com/safari/)  
- [Microsoft Edge](https://www.microsoft.com/edge)  

This ensured compatibility and consistent performance across different environments.

### Responsiveness <a name="responsiveness"></a>
The website's responsiveness was assessed using both manual testing and developer tools to confirm seamless usability on screens of all sizes, including mobile, tablet, and desktop.

### Feature Testing <a name="feature-testing"></a>
Each feature of the application was manually tested to ensure it behaves as expected. This included user interactions such as:  
- Form submissions  
- Navigation links  
- Login/logout functionality  
- Data updates and retrieval
