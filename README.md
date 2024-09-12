# 🌱 **Soilitical API**

Soilitical's API provides endpoints for interacting with our machine learning model, designed to assist in predicting agricultural outcomes based on various input parameters. This API is built using Django and offers two main endpoints.

## 🚀 **Endpoints**

### 1. Model Information

- **Endpoint:** `/model-info`
- **Method:** `GET`
- **Description:** Retrieves details about the currently deployed machine learning model, including information such as model classes and configuration.

**Example Request:**

**GET https://apisoilitical.pythonanywhere.com/model-info**


**Example Response:**

```json
{
    "model_info": {
        "model_type": "RandomForestClassifier",
        "n_features": 6,
        "n_estimators": 100,
        "max_depth": 15,
        "feature_importances": [
            0.14326060206149363,
            0.18178319059935868,
            0.2145381231970259,
            0.11872886382040583,
            0.2638537653793756,
            0.07783545494234051
        ]
    }
}
```

### 2. Make Prediction

- **Endpoint:** `/predict`
- **Method:** `POST`
- **Description:** Takes input data to make a prediction using the machine learning model. Returns the predicted class label.

**Request Format:**

- **Headers:**

```http
Content-Type: application/json
```
# **Body:**
```json
{
    "N": 42,
    "P": 55,
    "K": 42,
    "Humidity": 3,
    "Temp": 35,
    "PH": 7
}
```

### Example Request: POST https://apisoilitical.pythonanywhere.com/predict

### Example Response: 
```json
{
    "prediction": "class1"
}```




