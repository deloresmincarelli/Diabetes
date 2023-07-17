#### Diabetes

The objective of this repo was to do 4 things: 
1) Auto Machine Learning
I used the H2O package to classify patients with diabetes (0/1).  The H2O package tries several classification models, and provides details on how each model performed. 
I used the best performing model to make predictions.
The output was a csv file that included all of the predictors, the official outcome, and the prediced outcome.

2) Create a sqlite database (using DBeaver software) and import the diabetes csv predictions

3) Use the OpenAI generative language model (LLM) to write natural language questions, and have the LLM translate the question into SQL to query the database.

4) Provide a web interface for the user to enter their questions, and view the answer.
