# Heart Disease Prediction System

## Project Description
This project presents an interactive web application built with Streamlit for predicting heart disease. Leveraging a Logistic Regression model trained on a comprehensive heart disease dataset, the system offers an intuitive interface for users to input various health parameters and receive an instant prediction regarding their heart health status.

## Features
*   **User-friendly Interface:** Developed with Streamlit, providing a clean and responsive design.
*   **Machine Learning Integration:** Utilizes a pre-trained Logistic Regression model for accurate predictions.
*   **Comprehensive Data Input:** Allows users to input key health metrics such as age, sex, chest pain type, blood pressure, cholesterol, and more.
*   **Instant Predictions:** Delivers immediate results on whether a person is likely to have heart disease.
*   **Customizable Design:** Includes custom CSS for an enhanced visual experience.

## Technologies Used
*   Python
*   Streamlit
*   scikit-learn (for Logistic Regression)
*   Pandas (for data handling)
*   NumPy (for numerical operations)
*   Pickle (for model serialization)

## Setup and Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    # If you don't have a requirements.txt, install directly:
    # pip install numpy pandas scikit-learn streamlit streamlit-option-menu pyngrok
    ```

4.  **Ensure model and data files are present:**
    Make sure you have `heart_disease_model.sav` in a `saved_models` directory and `heart_gtigwd.csv` in the project root.
    You will need to create the `saved_models` directory:
    ```bash
    mkdir saved_models
    ```

## Running the Application

1.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

2.  **Access the web app:**
    Streamlit will typically open the application in your web browser at `http://localhost:8501`. If you are running this in a cloud environment (like Google Colab) or need external access, you might use `ngrok`.

    **Using ngrok (for public access):**
    If you are in a Colab environment or need to expose your local Streamlit app to the internet, you can use `ngrok`.
    *   Sign up for `ngrok` and get your authtoken from their website.
    *   Set your authtoken:
        ```python
        from pyngrok import ngrok
        ngrok.set_auth_token('YOUR_NGROK_AUTHTOKEN')
        ```
    *   Run Streamlit in the background and create a public URL:
        ```python
        # In your notebook cell (or separate terminal for local setup)
        !streamlit run app.py &>/dev/null &
        import time
        time.sleep(5) #wait for streamlit to start
        public_url = ngrok.connect(8501)
        print("Open your app here!:", public_url)
        ```

## Usage
Once the application is running, navigate to the provided URL. You will see an input form where you can enter various patient data points. Click the 'Heart Disease Test Result' button to get a prediction on the likelihood of heart disease.

## Developer Info
Developed by Nafisat Musa | musanafisat59@gmail.com
