# FastAPI Web Scraping Tool

This project is a web scraping tool built with the FastAPI framework in Python. It automates the process of scraping product information from the [Dentalstall shop](https://dentalstall.com/shop) Shop. The tool extracts the product name, price, and image from each page of the catalogue without opening each product card.

## Features

- **Scraping Capabilities**: Extracts product names, prices, and images from each catalogue page.
- **Optional Settings**:
  - Page Limit: Limit the number of pages to scrape (e.g., limit_pages=5).
  - Proxy Support: Use a proxy server for scraping (e.g., proxy=http://your_proxy_address).
- **Data Storage**: Stores scraped data in a local JSON file and downloads images to a local directory.
- **Notification System**: Notifies the user about the scraping status at the end of the cycle.
- **Extensibility**: Uses an object-oriented approach with strategy patterns for easy extension of storage and notification methods.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Project Structure](#project-structure)
4. [Usage](#usage)
   - [Running the Server](#running-the-server)
   - [API Endpoint](#api-endpoint)
   - [Examples](#examples)
5. [Data Storage](#data-storage)
6. [Extending the Tool](#extending-the-tool)
   - [Storage Strategy](#storage-strategy)
   - [Notification Strategy](#notification-strategy)
7. [Notes](#notes)
8. [License](#license)

## Prerequisites

- Python 3.7 or higher
- pip package manager

## Installation

1. Clone the Repository

   ```bash
   git clone https://github.com/nareshNishad/fastapi-web-scraper.git
   cd fastapi-web-scraper
   ```

2. Create a Virtual Environment (Optional but Recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install Dependencies

   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
your_project/
├── main.py               # Main FastAPI application
├── requirements.txt      # Project dependencies
├── scraper/
│   ├── __init__.py
│   ├── scraper.py        # Scraper class and helper functions
│   ├── storage.py        # Storage strategy classes
│   └── notification.py   # Notification strategy classes
├── data/
│   ├── products.json     # JSON file where scraped data is stored
│   └── images/           # Directory for downloaded images
└── README.md             # Project documentation
```

### Description of Files and Directories

- `main.py`: Contains the FastAPI application and defines the API endpoints.
- `requirements.txt`: Lists all Python dependencies required to run the application.
- `scraper/`: Package containing modules related to scraping, storage, and notifications.
  - `scraper.py`: Contains the Scraper class and helper functions.
  - `storage.py`: Contains storage strategy classes like StorageStrategy and JSONStorageStrategy.
  - `notification.py`: Contains notification strategy classes like NotificationStrategy and ConsoleNotificationStrategy.
- `data/`: Directory for storing output data.
  - `products.json`: JSON file where the scraped product data is saved.
  - `images/`: Directory where all downloaded product images are stored.
- `README.md`: Contains instructions and documentation for the project.

## Usage

### Running the Server

1. Start the FastAPI Server

   ```bash
   uvicorn main:app --reload
   ```

   The server will start on http://127.0.0.1:8000.

### API Endpoint

`GET /scrape`

Initiates the scraping process.

Query Parameters:
- `limit_pages` (optional): Integer to limit the number of pages to scrape.
- `proxy` (optional): Proxy server URL to use during scraping.

Example:

```bash
GET /scrape?limit_pages=5&proxy=http://your_proxy_address
```

### Examples

1. Scrape Without Limits and Proxy

   ```bash
   curl -X GET "http://127.0.0.1:8000/scrape"
   ```

2. Scrape with Page Limit

   Limit the scraping to the first 5 pages:

   ```bash
   curl -X GET "http://127.0.0.1:8000/scrape?limit_pages=5"
   ```

3. Scrape Using a Proxy

   Replace `http://proxy_address:port` with your actual proxy address:

   ```bash
   curl -X GET "http://127.0.0.1:8000/scrape?proxy=http://proxy_address:port"
   ```

4. Scrape with Both Page Limit and Proxy

   ```bash
   curl -X GET "http://127.0.0.1:8000/scrape?limit_pages=5&proxy=http://proxy_address:port"
   ```

5. Accessing the API via Swagger UI

   You can also interact with the API using the automatically generated Swagger UI:

   URL: http://127.0.0.1:8000/docs

## Data Storage

- **Product Data**: The scraped product data is stored in `data/products.json`.
- **Images**: Downloaded product images are saved in `data/images/`.

Sample `products.json` Structure:

```json
[
  {
    "product_title": "1 x GDC Extraction Forceps Lo...",
    "product_price": 850.0,
    "path_to_image": "data/images/GDC-Extraction-Forceps-Lower-Molars-86A-Standard-FX86AS-300x300.jpg"
  },
  ...
]
```

## Extending the Tool

### Storage Strategy

The tool uses a strategy pattern for storage, allowing easy extension to other storage methods.

To add a new storage method:

1. Create a new class in `scraper/storage.py` inheriting from `StorageStrategy`.
2. Implement the `save` and `save_image` methods.

### Notification Strategy

Similarly, the notification method can be extended.

To add a new notification method:

1. Create a new class in `scraper/notification.py` inheriting from `NotificationStrategy`.
2. Implement the `notify` method.

## Notes

- **Legal Considerations**: Ensure you comply with the website's Terms of Service and robots.txt file. Unauthorized scraping may violate legal agreements and lead to legal action.
- **Error Handling**: The provided code includes basic error handling. For production use, consider adding comprehensive error checking and logging mechanisms.
- **Dependencies**: Make sure all dependencies are installed as per the `requirements.txt` file.
- **Python Version**: The code is compatible with Python 3.7 and above.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
