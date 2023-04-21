# tt2
**Beta Sensor Value**
This is a simple HTML, CSS, and JavaScript-based application that uses the device orientation sensor of a mobile device to measure the beta value and display messages based on the value. The application displays different messages based on whether the user is properly seated or not.

**Installation and Usage**
To use this application, simply open the index.html file in any modern web browser on a mobile device that supports the device orientation sensor.

When you click on the "Start" button, the application starts listening to the device orientation sensor and displaying the beta value in real-time.

The application uses the HTML5 Canvas API to display messages on the screen based on the beta value. If the user is seated properly, a message is displayed that the user is seated properly. If the user is not seated properly, a message is displayed asking them to sit properly. If the user is in an intermediate position, a message is displayed telling them that they are in an intermediate position and displaying the time for which they have been in that position.

**Code Overview**
The index.html file contains the HTML code for the application. It contains a canvas element with the id sensorCanvas and a button element with the id startButton.

The style section of the HTML file contains the CSS code to set the width and height of the canvas element to 100%.

The JavaScript code is embedded in the script section of the HTML file. It consists of the following functions:

updateCanvas(beta): This function updates the canvas with the sensor data. It takes the beta value as an input and displays the appropriate message based on the value.

startEventListeners(): This function starts the event listeners for the device orientation sensor.

An anonymous function that adds an event listener for the device orientation change event. This function gets the beta value from the sensor data and passes it to the updateCanvas(beta) function to update the canvas with the new value.

The updateCanvas(beta) function uses the getContext() method of the canvas element to get a 2D context for the canvas. It then sets the font style for displaying text on the canvas. The function then rounds the beta value to the nearest integer and displays the appropriate message based on the value.

If the rounded beta value is less than 80, the function displays a message that the user is seated properly and resets the time tracking variables.

If the rounded beta value is between 80 and 87, the function checks whether the user is seated properly or not. If the user is not seated properly, a message is displayed asking them to sit properly. If the user is in an intermediate position, a message is displayed telling them that they are in an intermediate position and displaying the time for which they have been in that position.

If the rounded beta value is greater than 87, the function displays a message that the user is in the initial seating position and resets the time tracking variables.

The startEventListeners() function adds an event listener for the deviceorientation event and sets the eventListenerAdded variable to true.

**Conclusion**
This is a simple application that demonstrates how to use the device orientation sensor of a mobile device to measure the beta value and display messages based on the value. The application can be easily customized to display different messages or perform different actions based on the sensor data.
