# iiec-python-api

This project's focus is to create APIs using Python and use a Webserver as a CGI.
The four APIs used will allow a Client to interact with the OS used on the Webserver.
The APIs will allow a Client:
1. Execute simple OS-based commands which do not require special permissions eg., date, cal, etc.
2. Execute OS-based commands with root priviledge i.e., will allow to use all the commands which may or may not require root user permissions.
3. Use Docker-CE software running on the server to launch Docker Containers
4. Use any of the Docker Containers exisitng on the server for personal use cases.

The contents present in the directory 'under_html' must be copied to the Document Root of the Webserver eg., /var/www/html/ for Apache.
Make sure to make the necessary changes required in the HTML forms used. Each form must be updated with the Server-IP used.
Also required to update the Server-IP on the homepage i.e., index.html

To better understand the project view the article on the link below:
https://www.linkedin.com/pulse/creating-apis-using-python-sarthak-sharma