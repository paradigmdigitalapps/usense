# usense
intelligent news recommendation for business decision makers

# About the application

Usense web application presents fresh weekly news to managers about workforce mobility so they can have better decision on this topic without making heavy search process themselves.
The news are presented in 3 different groups (in sub sections) 3 news in each sections. In each section they can see a small fraction of the news. If they get interested, it is possible to read a longer header and finally they can also click and open the whole news in a new browser window.
A free text search also support the quick assessment of the content. This function is available separately for each sub section.
For more advanced users additional services are available after registration with their Google account. Additional services are statistics about top-words, distribution of active users by professional area, feed-back about the service that will be used for later customization.
The news information is collected by a separate service and the result is loaded as a ready-made content to this part of the service. No automation, no interface is developed for feed-in the news.

This code is uploaded and maintained in GitHub and available only for invited contributors.

Overview of the applied technology framework:<br/>
- Enviroment: Google Application Engine<br/>
- Web application: Webapp2 / Paython2<br/>
- DB: Google Datastore<br/>
- Template handling: Jinja2<br/>
- Font-end: Bootstrap3, CSS and Javasript<br/>

The structure of the code is briefly described below.

./sd_vote.py server site applcation script written in Python
./template/ html code of the site, this is a one page design
./js/ this is the folder of .js code
./img/ this is the folder of image resources

User input is sent to server storage with ajax function with help of http post transaction.

