# Video Game Success Prediction

I chose this topic for my project because of my passion for the gaming industry. Based on past experiences, I wanted to train a Machine Learning model capable of predicting whether a video game will be a commercial success (a "Hit") based on its Metacritic score, release year, community reviews, and other key features.

## Description

I utilized the public **RAWG API** (the same database powering platforms like Discord) to extract a comprehensive dataset of video games.

During the pre-processing phase, I cleaned the data by removing irrelevant values that brought no predictive power to the model and formatted the data types to make them compatible with Machine Learning algorithms. The target variable, `este_hit` (is_hit), was explicitly defined based on the official Metacritic score threshold.

## Dataset Structure

The final dataset consists of 8 engineered features:

| Feature Name | Data Type | Description |
| :--- | :--- | :--- |
| **nume** | `String` | The unique identifier/title of the game. |
| **an_lansare** | `Integer` | The release year of the game. |
| **gen_principal** | `String` | The primary genre of the game. |
| **nr_platforme** | `Integer` | The number of platforms the game is available on. |
| **timp_joc_mediu** | `Integer` | The average playtime required to complete the game. |
| **rating_utilizatori**| `Float` | The community-provided rating. |
| **nr_recenzii** | `Integer` | The total number of user reviews. |
| **este_hit** | `Integer` | The target column (**1** for Hit, **0** for Non-Hit). |

## Model Training & Evaluation

For the predictive model, I used **Logistic Regression** via the `scikit-learn` library.

* **Data Preparation:** We split the features (X) and the target variable (y). To ensure valid training, categorical variables were encoded, and the test/train splits were strictly aligned (padding missing feature columns with zeros where necessary).
* **Performance:** After training, the model achieved an impressive **80% accuracy**—a highly robust score for predicting video game market success.
* **Confusion Matrix Insights:** * The model correctly identified **83 Non-Hits** (True Negatives) and **127 Hits** (True Positives).
  * It incorrectly predicted **27 games as Non-Hits** (False Negatives) and **26 games as Hits** (False Positives). 
  * *Context:* This margin of error perfectly mirrors reality. Often, massive AAA titles (such as certain *Assassin's Creed* releases) with years of development and hype end up disappointing both critics and fans, despite having all the statistical markers of a guaranteed hit. This real-world unpredictability makes the 80% accuracy score even more impressive.

## Conclusions

Through Exploratory Data Analysis (EDA) and model evaluation, I observed the following:

* Games with a user rating above **3.9** almost universally secure "Hit" status.
* The most appreciated games generally sit in the **3.5 to 4.2** rating range. This highlights an interesting community bias: highly anticipated titles from massive studios are often judged much more harshly by users compared to surprise indie games that exceed expectations and become viral hits.
* The high accuracy of the Logistic Regression model proves that, despite occasional exceptions, community reception and Metacritic scores share an objective correlation. This allows a well-tuned Machine Learning model to reliably predict the success or failure of a title based on historical data.
