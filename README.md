# Facial-Recognition-App

The primary objective of this bachelor's degree project, developed in the Python programming language, is to create an application that leverages facial recognition technology to streamline the process of tracking student attendance in a classroom setting. The application is designed to interact with a local database for storing student information and offers a user-friendly interface with the following key pages:

1. **Loading Page**: This initial page grants users access to the application, allowing them to prepare the system for attendance verification.

2. **Registration Page**: On this page, users can conveniently register themselves within the system, providing essential personal information.

3. **Database Management Page**: This section offers versatile options for managing the local database. Users can locate the database, create a new one if it doesn't exist, and effortlessly input student data either manually or by importing it from an external source, such as a .csv file.

4. **Facial Recognition**: Once student data is registered, the application employs sophisticated facial recognition algorithms like HOG or CNN. It captures the current camera image and compares it with images stored in the database. The application calculates the Euclidean distance between the images and, based on a specified tolerance, determines whether the student is registered for the course.

5. **Attendance Submission Page**: This page allows for the seamless recording of the presence of successfully identified students. It automatically generates attendance records, including student ID, name, surname, date, and exact time. These records are then transmitted via email to the registered email address, which typically belongs to the authorized professor or user.

This innovative project represents a forward-thinking approach to classroom attendance management, harnessing the power of facial recognition technology to improve efficiency and accuracy in the classroom environment.
