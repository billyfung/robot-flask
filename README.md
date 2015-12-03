## Using Python Flask for Google App Engine to build web interface to control robot arm

Using the skeleton for building Python applications on Google App Engine with the
[Flask micro framework](http://flask.pocoo.org). Creating a Flask web interface to control a robot connected to local server from the web. 

See [Google Cloud Platform github
repos](https://github.com/GoogleCloudPlatform) for sample applications and
scaffolding for other python frameworks and use cases.

## Usage
This web interface is used to control a robotic arm connected to local flask server via usb. Pressing the buttons makes the robot arm perform the movements via the usb. Ideally this would be run on a Raspberry Pi, with the robot connected to it via usb. 

The robot arm communication will be done using the pyusb library. The web application will be done using the Flask framework. 

Visit the application [https://swift-yew-113223.appspot.com/](https://swift-yew-113223.appspot.com/)

See [the development server documentation](https://developers.google.com/appengine/docs/python/tools/devserver)
for options when running dev_appserver.




