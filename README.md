# Remember Me

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
   - [Wireframe](#wireframe)
4. [Entity-Relationship Diagram](#entity-relationship-diagram)
5. [Agile Workflow](#agile-workflow)
   - [Epics and User Stories](#epics-and-user-stories)
   - [GitHub Project Boards](#github-project-boards)
   - [MoSCoW Prioritization](#moscow-prioritization)
   - [Story Points](#story-points)
6. [Project Milestones](#project-milestones)
7. [Features](#features)
   - [Existing Features](#existing-features)
   - [Future Implementations](#future-implementations)
8. [Technologies](#technologies)
   - [Programming Languages](#programming-languages)
   - [Applications and Libraries](#applications-and-libraries)
9. [Local Development & Deployment](#local-development--deployment)
   - [Local Development](#local-development)
   - [Heroku Deployment](#heroku-deployment)
   - [Environment Variables](#environment-variables)
10. [Testing](#testing)
11. [Credits](#credits)
    - [Code Used and Tutorials](#code-used-and-tutorials)
    - [Acknowledgments](#acknowledgments)

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
The website employs a calming and emotionally resonant color palette that reflects the essence of memory preservation and warmth:

- **Primary Colors**: [![Calm Green](https://img.shields.io/badge/Calm%20Green-%23188181?style=flat-square&color=188181)](#) (`#188181`) as the main accent, accompanied by a darker shade for hover effects (`#0f5555`), symbolizing growth and renewal.  
- **Text Colors**: [![Dark Grey](https://img.shields.io/badge/Dark%20Grey-%23333333?style=flat-square&color=333333)](#) (`#333333`) for readability, and [![White](https://img.shields.io/badge/White-%23ffffff?style=flat-square&color=ffffff)](#) (`#ffffff`) for contrast and clarity in light-on-dark contexts.  
- **Background Colors**: [![Light Grey](https://img.shields.io/badge/Light%20Grey-%23f5f5f5?style=flat-square&color=f5f5f5)](#) (`#f5f5f5`) for a gentle feel, paired with [![Deep Navy](https://img.shields.io/badge/Deep%20Navy-%230d1b2a?style=flat-square&color=0d1b2a)](#) (`#0d1b2a`) for a grounded, introspective backdrop.  
- **Accent Colors**: [![Warm Yellow](https://img.shields.io/badge/Yellow-%23ffcc00?style=flat-square&color=ffcc00)](#) (`#ffcc00`) for highlights, transitioning to a [![Soft Orange](https://img.shields.io/badge/Soft%20Orange-%23ffa500?style=flat-square&color=ffa500)](#) (`#ffa500`) on hover, evoking feelings of joy and hope.  
- **Borders**: Subtle light grey borders (`#e0e0e0`) and dividers (`#f5f5f5`) add structure without overwhelming the design.

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


### Wireframe <a name="wireframe"></a>
Provide links or images of the wireframes.

---

## Entity-Relationship Diagram <a name="entity-relationship-diagram"></a>
Include an image or description of the ER diagram used for database modeling.

---

## Agile Workflow <a name="agile-workflow"></a>

### Epics and User Stories <a name="epics-and-user-stories"></a>
Details about epics and how user stories were mapped to them.

### GitHub Project Boards <a name="github-project-boards"></a>
Link to or describe how GitHub Project Boards were utilized.

### MoSCoW Prioritization <a name="moscow-prioritization"></a>
Details on how features were prioritized.

### Story Points <a name="story-points"></a>
Explain how story points were used for task estimation.

---

## Project Milestones <a name="project-milestones"></a>
List key project milestones and their completion status.

---

## Features <a name="features"></a>

### Existing Features <a name="existing-features"></a>
Detailed description of the implemented features.

### Future Implementations <a name="future-implementations"></a>
List features planned for future releases.

---

## Technologies <a name="technologies"></a>

### Programming Languages <a name="programming-languages"></a>
List the programming languages used in the project.

### Applications and Libraries <a name="applications-and-libraries"></a>
List the main libraries and tools with their purpose.

---

## Local Development & Deployment <a name="local-development--deployment"></a>

### Local Development <a name="local-development"></a>
Instructions on how to set up the project locally.

### Heroku Deployment <a name="heroku-deployment"></a>
Details about the deployment process on Heroku.

### Environment Variables <a name="environment-variables"></a>
List the environment variables needed and their purpose.

---

## Testing <a name="testing"></a>
Describe the testing methodologies, tools used, and include test cases if applicable.

---

## Credits <a name="credits"></a>

### Code Used and Tutorials <a name="code-used-and-tutorials"></a>
Links to code snippets and tutorials used.

### Acknowledgments <a name="acknowledgments"></a>
Mention any contributors or resources that were instrumental to the project.

---
