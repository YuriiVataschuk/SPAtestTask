# Django Comment System with Docker

This is a Dockerized Django project that implements a comment system with the ability to add, reply to, and list comments along with file attachments.

## Features

- Add comments and optionally attach images and text files.
- Reply to existing comments in a nested structure.
- List and sort comments based on different criteria.

## Docker Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-django-comment-project.git

2. Build the Docker container:
   ```bash
   docker build -t django-comment-system .

3. Run the Docker container:
   ```bash
   docker run -p 8000:8000 -d django-comment-system
4. Access the application in your web browser at http://127.0.0.1:8000/app/comment_list/

## Usage
Add a Comment: Visit the 'Add Comment' page to submit a new comment along with an optional image and text file attachment.
Reply to a Comment: You can reply to an existing comment by clicking the 'Reply' button and providing your reply text.
View Comments: Check out the 'Comment List' page to see all comments in a paginated view. You can also sort them by different criteria.

## Requirements
Docker