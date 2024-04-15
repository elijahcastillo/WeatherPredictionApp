![image] (./interface.png)

For our project, we created a weather prediction app that will give you a weather readout depending on user input.
This app will prompt the user to select what type of weather they want to predict, and then ask the user to input data for the categories to make a prediction. 
Data used:
  - Quantative data
  - CSV file with data on weather
Technologies used:
  - flask
  - html
  - css
  - Javascript
Milestones:
  - Created a shared notebook
  - Model exploration to see which type of model is optimal
  - Start web development
  - Complete optimal model development
  - Apply optimal models to website
  - Stress tested website with integrated models
  - Clean up code with comments to make it legible
Report of Implementation:
  - At first we tried making an SVM model and faced difficulties. This is because they had poor training times & accuracy
  - Then we tried making a decision tree and faced the same problems
  - We then created an MLP model for each category/feature of the dataset
  - Took a while to train, but yielded higher accuracy
