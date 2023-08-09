# campus_placement_prediction
Campus Placement is a strategy for sourcing, engaging and hiring young talent for internship and entry-level positions. College recruiting is typically a tactic for medium- to large-sized companies with high-volume recruiting needs, but can range from small efforts (like working with university career centers to source potential candidates) to large-scale operations (like visiting a wide array of colleges and attending recruiting events throughout the spring and fall semester).
Campus recruitment often involves working with university career services centers and attending career fairs to meet in-person with college students and recent graduates. We will be using algorithms such as KNN, SVM and ANN. We will train and test the data with these algorithms. From this the best model is selected and saved in .pkl format. We will be doing flask integration and IBM deployment.

Project Flow: 
User interacts with the UI to enter the input.
Entered input is analyzed by the model which is integrated.
Once model analyzes the input the prediction is showcased on the UI.
We are building a flask application which needs HTML pages stored in the templates folder and a python script app.py for scripting.
rdf.pkl is our saved model. Further we will use this model for flask integration. 
Training folder contains a model training file.
