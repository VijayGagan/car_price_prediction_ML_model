# 🚗 Car Price Prediction using Machine Learning

A machine learning project that predicts the **selling price of a used car** based on different features such as car brand, manufacturing year, kilometers driven, fuel type, selling type, transmission, and number of previous owners.

The project uses **Linear Regression** for prediction and **Streamlit** to provide an interactive web application.

---

## 📌 Project Overview

Buying or selling a used car can be difficult because the appropriate price depends on several factors.

This project uses historical car data and machine learning to estimate the selling price of a car based on the information provided by the user.

The project includes:

* Data preprocessing
* Duplicate data removal
* Data analysis
* Car and bike separation
* Feature transformation
* Categorical value encoding
* Linear Regression model training
* Model prediction
* Streamlit web application

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Linear Regression**
* **Streamlit**
* **Pickle**
* **Jupyter Notebook**

---

## 📂 Project Structure

```text
Car-Price-Prediction/
│
├── app.py
├── cardata.csv
├── model.pkl
├── Untitled1.ipynb
└── README.md
```

### Files Description

| File              | Description                                              |
| ----------------- | -------------------------------------------------------- |
| `app.py`          | Streamlit application for car price prediction           |
| `cardata.csv`     | Dataset containing car information                       |
| `model.pkl`       | Trained Linear Regression model                          |
| `Untitled1.ipynb` | Data preprocessing, analysis, model training and testing |
| `README.md`       | Project documentation                                    |

---

## 📊 Dataset Features

The model uses the following features:

* **Car Name** – Car brand
* **Year** – Manufacturing year
* **Present Price** – Current/present price
* **Driven Kms** – Number of kilometers driven
* **Fuel Type** – Petrol, Diesel, or CNG
* **Selling Type** – Individual or Dealer
* **Transmission** – Manual or Automatic
* **Owner** – Number of previous owners

The target variable is:

```text
Selling_Price
```

---

## 🔄 Machine Learning Workflow

```text
             Dataset
                │
                ▼
       Data Preprocessing
                │
                ▼
       Remove Duplicates
                │
                ▼
      Separate Cars & Bikes
                │
                ▼
      Feature Transformation
                │
                ▼
      Categorical Encoding
                │
                ▼
        Train/Test Split
                │
                ▼
       Linear Regression
                │
                ▼
         Model Training
                │
                ▼
          Model Testing
                │
                ▼
          Save Model
                │
                ▼
        Streamlit App
                │
                ▼
       Predicted Car Price
```

---

## 🧹 Data Preprocessing

The dataset is first loaded using Pandas.

The preprocessing steps include:

1. Checking for missing values.
2. Checking for duplicate records.
3. Removing duplicate records.
4. Separating bikes from cars.
5. Extracting the car brand from the car name.
6. Converting categorical features into numerical values.
7. Separating input features and the target variable.

For example, car names are converted into their brand names before encoding.

---

## 🤖 Machine Learning Model

The project uses **Linear Regression** from Scikit-learn.

The dataset is divided into training and testing data using an **80:20 split**.

```python
x_train, x_test, y_train, y_test = train_test_split(
    input_data,
    output_data,
    test_size=0.2
)
```

The model is then trained using:

```python
model = LinearRegression()
model.fit(x_train, y_train)
```

The trained model is saved using Pickle:

```python
pk.dump(model, open('model.pkl', 'wb'))
```

---

## 🌐 Streamlit Application

The Streamlit application provides an interactive interface where the user can enter:

* Car brand
* Manufacturing year
* Kilometers driven
* Fuel type
* Selling type
* Transmission
* Number of previous owners

After clicking **Predict Price**, the trained machine learning model generates the estimated car price.

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/car-price-prediction.git
```

### 2. Open the Project Folder

```bash
cd car-price-prediction
```

### 3. Install Required Libraries

```bash
pip install pandas numpy scikit-learn streamlit
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

### 5. Open the Application

Streamlit will provide a local URL such as:

```text
http://localhost:8501
```

Open it in your browser to use the application.

---

## 💻 Application Preview

Add screenshots of your Streamlit application here.

```text
📸 Add your application screenshot here
```

You can upload a screenshot to your GitHub repository and display it using:

```markdown
![Car Price Prediction App](screenshots/app.png)
```

---

## ✨ Features

* 🚗 Car price prediction
* 📊 Machine learning-based prediction
* 🧹 Data preprocessing
* 🔢 Categorical feature encoding
* 🤖 Linear Regression model
* 🌐 Interactive Streamlit interface
* ⚡ Fast predictions
* 💾 Saved trained model

---

## 📈 Future Improvements

The project can be improved by:

* Using advanced regression algorithms such as Random Forest and Gradient Boosting.
* Comparing multiple machine learning models.
* Improving model accuracy through hyperparameter tuning.
* Adding data visualizations to the Streamlit application.
* Adding model evaluation metrics such as MAE, MSE and R² score.
* Improving the user interface.
* Deploying the application online.
* Adding more car-related features for better predictions.

---

## 🎯 Learning Outcomes

Through this project, I learned:

* How to preprocess a real-world dataset.
* How to handle duplicate records.
* How to transform categorical data.
* How to split data into training and testing sets.
* How to train a Linear Regression model.
* How to save and load a trained machine learning model.
* How to build a machine learning web application using Streamlit.

---

## 👨‍💻 Author

**Vijaya Gagan**

GitHub:
https://github.com/VijayGagan

---

## 📜 License

This project is created for **educational and portfolio purposes**.
