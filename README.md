# Remember Me
![Quote](./readme_images/quote.png)
[Live Page](https://remember-me-jth-8eebce62c286.herokuapp.com/)

### **Memorial Blog for a Bereaved Child**

A heartfelt memorial blog designed to preserve the cherished memories of a parent who has passed away. This platform provides a space where family, friends, and loved ones can come together to share meaningful stories, photos, and videos, creating a collective tribute to honor the parent’s life. By capturing these personal moments and reflections, the blog serves not only as a source of comfort for the bereaved child but also as a lasting keepsake that celebrates the parent’s legacy and fosters connections among those who knew and loved them.

---


## Table of Contents

1. [Overview](#overview)
2. [User Experience (UX)](#user-experience-ux)
   - [User Stories](#user-stories)
3. [Design](#design)
   - [Colour Scheme](#colour-scheme)
   - [Typography](#typography)
   - [Components](#components)
   - [Wireframes](#wireframes)
   - [Entity-Relationship Diagram](#entity-relationship-diagram)
4. [Agile Workflow](#agile-workflow)
   - [Epics and User Stories](#epics-and-user-stories)
   - [GitHub Project Board](#github-project-board)
   - [MoSCoW Prioritization](#moscow-prioritization)
   - [Project Milestones](#project-milestones)
5. [Features](#features)
   - [Existing Features](#existing-features)
   - [Future Implementations](#future-implementations)
6. [Technologies](#technologies)
   - [Programming Languages](#programming-languages)
   - [Applications and Libraries](#applications-and-libraries)
7. [Local Development & Deployment](#local-development--deployment)
   - [Local Development](#local-development)
   - [Heroku Deployment](#heroku-deployment)
   - [Environment Variables](#environment-variables)
8. [Testing](#testing)
9. [Credits](#credits)

---

## Overview <a name="overview"></a>

### Purpose

"Remember Me" is a digital memory book created for a child who has lost a parent at a young age. It serves as a platform for family, friends, and loved ones to preserve the parent’s legacy by sharing stories, photos, and videos. This project aims to provide comfort and connection, offering the bereaved child—and others who knew the parent—a meaningful way to remember and celebrate their life.

The site is designed to capture the essence of the parent through the eyes of those who loved them, creating a lasting tribute that can be revisited and cherished over time. By preserving these memories, the platform not only honors the parent’s life but also provides an emotional connection for the child and their community of loved ones.

### Project Audience

- **Primary Audience**: The child for whom the website is dedicated, as well as family members and close friends who wish to remember and celebrate the life of the parent. 
- **Contributors**: Loved ones who want to share meaningful stories, photos, and videos of the parent, fostering a shared experience of remembrance and connection.
- **Site Admin**: Responsible for moderating content, managing user access, and ensuring the platform is secure, respectful, and accessible.

### Key Features

1. **Memory Sharing**: A central blog-like section where registered users can post stories, memories, photos, and videos about the child’s parent. Each entry helps to paint a vivid picture of the parent’s life and legacy.

2. **Commenting System**: Allows users to leave comments on posts, encouraging shared reflections and fostering community interaction.

3. **Role-Based Access**: 
   - **Public Users** can view content but must create an account to contribute.
   - **Registered Users** can add new posts, upload media, and comment on others’ entries.
   - **Admin** has permissions to approve, edit, or delete posts and comments to maintain site quality and appropriateness.

4. **Responsive and Accessible Design**: A child-friendly, warm, and inviting design that adapts seamlessly across all devices. Accessibility features ensure the site is inclusive for all users, including those with disabilities.

5. **Security and Privacy**: Comprehensive security measures to protect sensitive data, with role-based access control and encrypted authentication processes to safeguard user information.

---


## User Experience (UX) <a name="user-experience-ux"></a>

### User Stories <a name="user-stories"></a>
1. **User Registration and Login** <br>
- As a user I want to register and log in so that I can post memories and leave comments.

2. **Admin Content Management**
- As an admin I want to manage posts and comments so that the content is respectful and appropriate.

3. **Create a Memory**
- As a registered user I want to create a memory so that I can share my personal thoughts and experiences about the child's father.

4. **Browse Memories**
- As a user I want to browse through shared memories so I can read others’ experiences and reflections.

5. **Leave a Comment**
- As a user I can leave a comment on a memory so that I can engage with others' stories.

6. **Simple and Visually Appealing Design**
- As a user I can experience a simple visually appealing layout so that I feel emotionally connected to the content.

7. **Accessibility for All Users**
- As a user with accessibility needs I can navigate and use the website easily so that I can access the content effectively.

8. **Data Security and Privacy**
- As a site user I can trust my information is secure so that I feel comfortable using the platform.

9. **Structured Database Model**
- As a developer I can utilise a structured database model so that I manage users posts comments and media files effectively.

10. **Deploy Site to Cloud**
- As a developer I can deploy the site to a cloud platform so that it’s accessible online.

11. **Helpful Error Messages**
- As a user I can see helpful error messages so that I understand what I need to do if something goes wrong.

12. **Functionality Testing**
- As a developer I can test the website's functionality so that it works smoothly and without bugs.

13. **Project Documentation**
- As a developer I can reference clear project documentation so that contributors can understand the purpose and structure of the project.

14. **Wireframes**
- As a developer I can create wireframes so that I have a clear design and guide to follow during the development process.

15. **Adding and Removing Blog Posts from Favourites Page**
- As a registered user I want to add and remove blog posts from my favourites page so that I can quickly access the posts I find most valuable or interesting.

16. **Editing and Deleting Memory**
- As a registered user I want to edit and delete my memories so that I can keep my shared personal thoughts and experiences accurate and relevant.

17. **Editing and Deleting Comments**
- As a user I can edit or delete my own comments on a memory so that I can ensure my contributions are accurate or remove them if necessary.

18. **Error Pages (404 and 500)**
- As a user I can see helpful error messages for 404 and 500 errors so that I understand what went wrong and know how to proceed.

---

## Design <a name="design"></a>

### Colour Scheme <a name="colour-scheme"></a>

The website uses a calming and emotionally resonant color palette to reflect the essence of memory preservation and warmth:

- **Primary Colors**:  
  - [![Calm Green](https://img.shields.io/badge/Calm%20Green-%23188181?style=flat-square&color=188181)](#) (`#188181`): Serves as the main accent color, symbolizing growth and renewal.  
  - [![Darker Calm Green](https://img.shields.io/badge/Darker%20Calm%20Green-%230f5555?style=flat-square&color=0f5555)](#) (`#0f5555`): Used for hover effects to complement the primary accent.  

- **Text Colors**:  
  - [![Dark Grey](https://img.shields.io/badge/Dark%20Grey-%23333333?style=flat-square&color=333333)](#) (`#333333`): Ensures readability and a clean appearance.  
  - [![White](https://img.shields.io/badge/White-%23ffffff?style=flat-square&color=ffffff)](#) (`#ffffff`): Provides contrast for light-on-dark text contexts.  

- **Background Colors**:  
  - [![Light Grey](https://img.shields.io/badge/Light%20Grey-%23f5f5f5?style=flat-square&color=f5f5f5)](#) (`#f5f5f5`): Creates a soft and gentle background feel.  
  - [![Deep Navy](https://img.shields.io/badge/Deep%20Navy-%230d1b2a?style=flat-square&color=0d1b2a)](#) (`#0d1b2a`): Provides a grounded and introspective backdrop.  

- **Accent Colors**:  
  - [![Warm Yellow](https://img.shields.io/badge/Warm%20Yellow-%23ffcc00?style=flat-square&color=ffcc00)](#) (`#ffcc00`): Adds vibrant highlights to key elements.  
  - [![Soft Orange](https://img.shields.io/badge/Soft%20Orange-%23ffa500?style=flat-square&color=ffa500)](#) (`#ffa500`): Enhances hover effects with a warm, hopeful tone.  

- **Borders and Dividers**:  
  - [![Light Grey Border](https://img.shields.io/badge/Light%20Grey-%23e0e0e0?style=flat-square&color=e0e0e0)](#) (`#e0e0e0`): Subtle borders add structure without distracting from the design.  
  - [![Divider](https://img.shields.io/badge/Divider-%23f5f5f5?style=flat-square&color=f5f5f5)](#) (`#f5f5f5`): Ensures a clean and polished layout.

### Typography <a name="typography"></a>
Typography choices prioritize both elegance and readability to suit the emotional nature of the website:  

- **Primary Font**: "Inter," a modern and highly legible font, is used for most textual content, ensuring a clean and professional look.  
- **Accent Font**: "Dancing Script" is used sparingly for decorative elements, such as headings and quotes, adding a touch of personality and emotional resonance.  
- Both fonts are sourced from Google Fonts, ensuring consistent rendering across devices.  

### Components <a name="components"></a>
The website's components are designed for a seamless user experience while emphasizing emotional connection:  

1. **Navbar**: A responsive navigation bar with links to core sections: Home, Memories, About, and user authentication options.  
2. **Introductory Section**: Features a heartfelt quote overlayed on a subtle background, setting the tone for the website.  
3. **Memory Cards**: Compact, visually appealing cards displaying memory excerpts, creation dates, and authorship details. Images are included where available.  
4. **Pagination**: A clean pagination bar for browsing memories, ensuring ease of navigation through content.  
5. **Footer**: A minimal footer with an attribution link, adding a personal touch by dedicating the project to Finn.  
6. **Login/Signup Section**: Engages visitors by prompting them to contribute their own memories, with clear call-to-action buttons.  
7. **Alert System**: Integrated feedback messages for user actions, styled for clarity and prominence without being intrusive.


### Wireframes <a name="wireframes"></a>
The [wireframes](./readme_images/wireframes.pdf) have been designed to provide a visual representation of each page's layout and functionality.

### Entity-Relationship Diagram <a name="entity-relationship-diagram"></a>

![ERD](./readme_images/ERD.png)

This ER diagram models a blogging platform with four main entities:

- **User**: Represents users with attributes like username, password, and email.  
- **Post**: Represents blog posts authored by users, with attributes like title, content, and creation dates.  
- **Comment**: Tracks comments made by users on posts, storing content and timestamps.  
- **Favourites**: Tracks posts marked as favorites by users.  

The diagram illustrates relationships between these entities, such as users creating posts, commenting on them, and marking them as favorites.

---

## Agile Workflow <a name="agile-workflow"></a>

This project was developed using agile methodologies to ensure a systematic and iterative approach to achieving project goals. Here’s an overview of how the workflow was structured:


### Epics and User Stories <a name="epics-and-user-stories"></a>

**Epics**  
The foundation of the project was laid out through clearly defined epics that represented the main goals or themes. Each epic provided an outline, which helped guide the project's overall vision.  
<br>

- Example of an epic:

![Epic Example](./readme_images/epic_example.png)

**User Stories**  
Epics were broken down into user stories to capture user-centric functionality and provide actionable objectives. Each user story was documented as an issue in GitHub and included:  
- A clear **description** from the user's perspective.  
- Comprehensive **acceptance criteria** to define the "done" state.  
- **Tasks:** user stories were further subdivided into tasks, which were tracked as checklist items within their respective GitHub issues. This granular breakdown ensured every user story met the criteria and was delivered successfully.  
<br>

- Example of a user story:

![User Story Example](./readme_images/user_story_example.png)


### GitHub Project Board <a name="github-project-board"></a>

To manage and visualize the project's progress, GitHub **Kanban Board** was utilized extensively:  

The Kanban board provided a real-time overview of the project's status, categorizing tasks into columns such as "To do," "In Progress," and "Done." This facilitated effective task tracking and milestone management. 
<br><br> 
[Kanban Board](https://github.com/users/justynath/projects/10)
![Kanban Board](./readme_images/kanban.png)

### MoSCoW Prioritization <a name="moscow-prioritization"></a>

The MoSCoW prioritization method was employed to classify tasks and user stories based on their importance to the project.  

- **Must Have**: Essential features required for the MVP milestone.  
- **Should Have**: Important but not critical tasks included based on time and resources.  
- **Could Have**: Desirable enhancements for future updates.  

Each GitHub issue was labeled with its MoSCoW priority, ensuring a focus on delivering essential functionalities first.  
![MoSCoW prioritization](./readme_images/moscow.png)

### Project Milestones <a name="project-milestones"></a>

**MVP Milestone**  
The MVP milestone included all the core functionalities required for the project's initial release. It was the primary focus during the initial sprints.  
![MVP Milestone](./readme_images/MVP.png)

**Post-MVP and Enhancements**  
Subsequent milestones will cover enhancements and additional features that improved the project's overall functionality.  

---

# Features <a name="features"></a>

## Existing Features <a name="existing-features"></a>

1. **User Authentication**  
- **Sign Up**: New users can create an account to access personalized features.  
![Signup](./readme_images/signup.png)
- **Login**: Registered users can log in to access their account.  
![Login](./readme_images/login.png)
- **Logout**: Securely log out of the application.  
![Logout](./readme_images/logout.png)

2. **Memories Management**  
- **Recent Memories**: Displays the three most recent posts on the home page for quick access. 
![Recent Memories](./readme_images/recent_memories.png) 
- **View All Memories**: Explore the complete list of memories shared by users.  
![All Memories](./readme_images/all_memories.png)
- **Individual Memory Details**: View detailed content of each memory, including author and creation date.
![Memory](./readme_images/memory.png)

3. **Favorites Feature**  
- **Add to Favorites**: Users can add a memory to their favorites for easy future access.  
![Add Favourite](./readme_images/add_favourite.png)
- **View Favorites**: Dedicated page for viewing all favorited memories.  
![Favourite Memories](./readme_images/favourites.png)
- **Remove from Favorites**: Option to remove a memory from the favorites list.
![Remove Favourite](./readme_images/remove_favourite.png)

4. **Memory Creation and Management**  
- **Create Memory**: Authenticated users can contribute by sharing their memories.  
![Create Memory](./readme_images/create_memory_1.png)
![Create Memory](./readme_images/create_memory_2.png)
- **Edit Memory**: Authors can edit their submitted memories.  
![Edit Memory](./readme_images/edit_memory_1.png)
![Edit Memory](./readme_images/edit_memory_2.png)
- **Delete Memory**: Authors have the ability to delete their own memories.
![Delete Memory](./readme_images/delete_memory.png)

5. **Comment System**  
- **Add Comments**: Logged-in users can comment on individual memory posts.  
![Add Comment](./readme_images/add_comment.png)
- **Comment Moderation**: Comments require approval before being displayed.
![Display Comment](./readme_images/show_comment.png)
- **Edit Comments**: Users can modify their submitted comments.  
![Edit Comment](./readme_images/edit_comment.png)
- **Delete Comments**: Users can delete their own comments.  
![Delete Comment](./readme_images/delete_comment.png)


6. **Pagination**  
- Easily navigate through multiple pages of memories for better user experience.
![Pagination](./readme_images/pagination.png)

7. **Alerts and Feedback**  
- Dynamic feedback messages (e.g., success or error alerts) for actions such as login, memory submission, and comments.

8. **Dynamic Navigation Bar**  
- Automatically highlights the active page to improve user navigation.
![Navbar User](./readme_images/navbar_1.png)
![Navbar Register User](./readme_images/navbar_2.png)

9. **Simple Footer**
- Footer adding a personal touch.
![Footer](./readme_images/footer.png)

10. **Personal Components**
- Hero image and a quote setting the tone of the website, adding to its reflective mood.  
![Hero Image](./readme_images/hero.png)
- About section explains the purpose of the website and provides additional information to the user.  
![About](./readme_images/about.png)

11. **Share Memory/Sign up Button**
- The home page features a button to share a memory, which serves as a sign-up button for non-registered users.
![Home Share Memeory](./readme_images/home_share.png)
![Home Sign up](./readme_images/home_signup.png)


---

## Planned Features <a name="planned-features"></a>

- **User Profiles**: Allow users to customize their profiles with bio and profile pictures.  
- **Search and Filtering**: Implement advanced search functionality to locate memories easily.  
- **Tagging System**: Add tags to memories for better organization and categorization.  
- **Social Sharing**: Enable users to share memories on social media platforms.  
- **Email Notifications**: Notify users about updates like new comments on their posts.  
- **Dark Mode**: Provide an option to switch between light and dark themes.


---

## Technologies Used <a name="technologies"></a>

### Programming Languages

[![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML)  
Used to structure the application's main pages, including the layout of memories, user forms, and error pages.

[![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS)  
Employed to style the application's front-end, enhancing the visual appeal and user experience through thoughtful design.

[![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com)  
Implemented to add interactivity to the app, such as dynamic form validation and user feedback.

[![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org/)  
Used as the server-side programming language for building the back-end logic with Django.

---

### Applications and Libraries

[![Django](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com/)  
A high-level Python web framework used to create the main application structure and functionality.

[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=336791)](https://www.postgresql.org/)  
An advanced, open-source object-relational database system for storing the application’s data.

[![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com)  
Used for version control to track code changes and collaborate efficiently.

[![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com)  
Hosts the project repository and facilitates collaboration and version tracking.

[![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io)  
A cloud-based IDE used for writing and debugging code efficiently in a pre-configured development environment.

[![Gunicorn](https://img.shields.io/badge/Gunicorn-grey?logo=gunicorn&logoColor=499848)](https://gunicorn.org/)  
A Python WSGI HTTP server used to deploy the application.

[![Whitenoise](https://img.shields.io/badge/Whitenoise-grey?logo=htmx&logoColor=ffffff)](http://whitenoise.evans.io/)  
Serves static files directly from Django, simplifying deployment and improving performance.

[![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com/)  
A platform used to deploy the web application and make it accessible online.

[![Shields.io](https://img.shields.io/badge/Shields.io-grey?logo=shields&logoColor=000000)](https://shields.io/)  
Utilized for creating badges to enhance the README documentation.

[![TinyPNG](https://img.shields.io/badge/TinyPNG-grey?logo=png&logoColor=ffffff)](https://tinypng.com/)  
Optimizes image file sizes to improve web performance.

[![DrawSQL](https://img.shields.io/badge/DrawSQL-grey?logo=drawsql&logoColor=000000)](https://drawsql.app/)  
Helps design and visualize the database schema through Entity-Relationship Diagrams (ERD).

[![Psycopg2](https://img.shields.io/badge/Psycopg2-grey?logo=postgresql&logoColor=336791)](https://www.psycopg.org/)  
A PostgreSQL adapter for Python used for database interaction.

[![Dj Database URL](https://img.shields.io/badge/Dj--Database--URL-grey?logo=django&logoColor=092E20)](https://github.com/jacobian/dj-database-url)  
Simplifies database configuration by parsing the `DATABASE_URL` environment variable.

[![Balsamiq](https://img.shields.io/badge/Balsamiq-grey?logo=balsamiq&logoColor=000000)](https://balsamiq.com/wireframes/)  
Used to create wireframes and mockups for planning the layout and design of the application.

---

## Local Development & Deployment <a name="local-development--deployment"></a>

### Local Development <a name="local-development"></a>
Follow these steps to set up the project locally:

1. **Clone the Repository**:  
   - Open the repository on GitHub, click the "Code" button, and copy the repository URL.  
   - In your terminal, navigate to the directory where you want to clone the project and type:  
     ```bash
     git clone <repository_url>
     ```
2. **Set Up a Virtual Environment (Optional)**:  
   - Create a virtual environment:  
     ```bash
     python3 -m venv [virtual_environment_name]
     ```  
   - Activate the virtual environment:  
     - On Windows:  
       ```bash
       [virtual_environment_name]\Scripts\activate
       ```  
     - On macOS/Linux:  
       ```bash
       source [virtual_environment_name]/bin/activate
       ```  
3. **Install Dependencies**:  
   - Navigate to the project directory and install the required dependencies:  
     ```bash
     pip install -r requirements.txt
     ```
4. **Set Environment Variables**:  
   - Create a `.env` file in the project root directory and add the required variables (see [Environment Variables](#environment-variables) section).
5. **Database Setup**:  
   - Connect your database and apply migrations:  
     ```bash
     python manage.py migrate
     ```
   - Create a superuser for the admin panel:  
     ```bash
     python manage.py createsuperuser
     ```
6. **Load Fixtures (Optional)**:  
   - Populate the database with pre-defined data (if available):  
     ```bash
     python manage.py loaddata fixtures/[fixture_name].json
     ```
7. **Run the Development Server**:  
   - Start the server:  
     ```bash
     python manage.py runserver
     ```  
   - Open the URL provided in the terminal in your browser.

---

### Heroku Deployment <a name="heroku-deployment"></a>
Deploy the application to Heroku by following these steps:

1. **Prepare the Repository**:  
   - Ensure your project is pushed to a GitHub repository.
2. **Create a Heroku App**:  
   - Log in to the Heroku dashboard and create a new app.  
   - Specify the app name and region.
3. **Connect GitHub Repository**:  
   - In the **Deploy** tab, choose GitHub as the deployment method.  
   - Search for your repository and connect it.
4. **Add Buildpacks**:  
   - Navigate to the **Settings** tab.  
   - Under Buildpacks, add **Python**. Ensure it appears in the correct order.
5. **Set Environment Variables**:  
   - In the **Config Vars** section of the **Settings** tab, add the required variables (see [Environment Variables](#environment-variables) section).
6. **Deploy the Application**:  
   - In the **Deploy** tab, choose the branch to deploy (usually `main`).  
   - Enable automatic deploys or manually click **Deploy Branch**.
7. **Access the Deployed App**:  
   - Once deployment is complete, click **Open App** to view your live application.
   [Live Link](https://remember-me-jth-8eebce62c286.herokuapp.com/)

---

### Environment Variables <a name="environment-variables"></a>
The project requires the following environment variables:

- **SECRET_KEY**: A long, random string used for cryptographic signing in your application.  
- **DEBUG**: Set to `True` for local development and `False` for production.  
- **DATABASE_URL**: The URL of your database, including credentials and connection details.  
  Example: `postgres://USER:PASSWORD@HOST:PORT/DB_NAME`.  
- **CLOUDINARY_URL**: The URL for your Cloudinary account.  
  Example: `cloudinary://API_KEY:API_SECRET@CLOUD_NAME`.  

> **Note**: Ensure the `.env` file is added to `.gitignore` to avoid exposing sensitive information in your version control system. For Heroku deployment, set these variables in the Config Vars section on the dashboard.


---

## Testing <a name="testing"></a>
For a comprehensive guide to both manual and automated testing procedures, please check out [TESTING.md](./TESTING.md) It provides an in-depth look at all the testing scenarios and approaches implemented in the project.

---

## Credits <a name="credits"></a>

### Code Used and Tutorials 
- **Code Institute: Developing With Django**  
  This series from Code Institute provided a strong foundation for understanding the Django framework. It guided me through the process of building and deploying a Django app to Heroku.

- **[YouTube Tutorials](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)**  
  I referred to several videos from this playlist to learn how to implement various features in a Django blog. Some sections of my code are inspired by the examples demonstrated in these videos.

- ChatGPT and Stack Overflow were used for researching errors and finding suggestions to fix bugs.


### Media and Content 
- **Images**: All images used in this project are from my personal collection.  
- **Content**: Blog content (fixtures) was created using ChatGPT to efficiently generate complete and polished blog posts.

### Acknowledgments 
A special thanks to **Medale Oluwafemi**, my mentor at Code Institute, for his invaluable guidance and support throughout this project.

---
