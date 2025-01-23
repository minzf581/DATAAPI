Introduction
This API is designed to support the EON Protocol Data Solution. The APIs support secure, privacy-preserving, and efficient data integration, management, Website Data Scraping ，and computation functionalities for AI agents, aligned with the system’s dynamic and flexible features. Meeting modern data and AI application requirements.

This API will deployed on the google cloud platform.

API Features

1. Data Integration and Encryption

API: Data Upload

Description:
Allows data providers to upload datasets, define metadata, apply encryption, and specify access policies.

Endpoint:
POST /api/data/upload

Request Parameters:
	•	data_description (string): Metadata describing the dataset.
	•	privacy_algorithm (string): Selected privacy-preserving algorithm (e.g., FHE, TEE).
	•	access_policy (string): Access policy for the dataset (e.g., public, private).
	•	data_file (binary): Dataset file.

Example Request:

{
  "data_description": "Sales data for Q1 2025",
  "privacy_algorithm": "FHE",
  "access_policy": "private"
}

2. Data Query and Computation

API: Data Query

Description:
Enables users to query data dynamically with privacy-preserving algorithms.

Endpoint:
POST /api/data/query

Request Parameters:
	•	query_text (string): Natural language or structured query.
	•	filters (object): Optional filters (e.g., time range, data type).
	•	privacy_algorithm (string): Privacy-preserving algorithm for computation.

Example Request:

{
  "query_text": "Retrieve customer feedback for December 2024",
  "filters": {
    "time_range": "2024-12",
    "data_type": "customer_feedback"
  },
  "privacy_algorithm": "MPC"
}

3. Dynamic Data Support

API: Dynamic Data Injection

Description:
Supports real-time injection of new data into the system without retraining models.

Endpoint:
POST /api/data/dynamic_update

Request Parameters:
	•	data_id (string): Unique identifier of the dataset.
	•	new_data (binary): New data file.
	•	update_metadata (boolean): Whether to update dataset metadata.

Example Request:

{
  "data_id": "dataset_123",
  "new_data": "base64_encoded_data",
  "update_metadata": true
}

API: Knowledge Retrieval

Description:
Utilizes vector databases for dynamic semantic search and fast data retrieval.

Endpoint:
POST /api/data/semantic_search

Request Parameters:
	•	query (string): Natural language or keyword query.
	•	filters (object): Optional filters (e.g., time range, data type).

Example Request:

{
  "query": "Find text data containing product reviews",
  "filters": {
    "data_type": "text",
    "time_range": "2024-01"
  }
}

API: Multi-Modal Data Processing

Description:
Processes diverse data types such as text, images, audio, and video.

Endpoint:
POST /api/data/multimodal_process

Request Parameters:
	•	data_id (string): Unique identifier for the dataset.
	•	data_type (string): Type of data (e.g., text, image, audio, video).
	•	operation (string): Data processing operation (e.g., extract_features, classify).

Example Request:

{
  "data_id": "dataset_456",
  "data_type": "image",
  "operation": "extract_features"
}

4. AI Training Data Management

API: Data Quality Assessment

Description:
Analyzes data distribution, balance, and bias to provide optimization recommendations.

Endpoint:
POST /api/data/quality_assessment

Request Parameters:
	•	data_id (string): Unique identifier for the dataset.

Example Request:

{
  "data_id": "dataset_123"
}

API: Generate Data Report

Description:
Generates a quality report or optimization recommendations for datasets.

Endpoint:
POST /api/data/report

Request Parameters:
	•	data_id (string): Unique identifier for the dataset.
	•	format (string): Format of the report (e.g., PDF, JSON).

Example Request:

{
  "data_id": "dataset_789",
  "format": "PDF"
}

5. Dynamic User Request Handling

API: Natural Language Parsing

Description:
Parses natural language descriptions from users to generate actionable data queries.

Endpoint:
POST /api/data/nlp_parse

Request Parameters:
	•	query (string): User’s natural language input.
	•	context (object): Optional context information (e.g., user preferences).

Example Request:

{
  "query": "Analyze last month’s sales data and calculate growth rate"
}

API: Result Delivery

Description:
Delivers computation results in user-specified formats, such as encrypted data or visualized reports.

Endpoint:
POST /api/data/result_delivery

Request Parameters:
	•	task_id (string): Unique identifier for the task.
	•	delivery_format (string): Result format (e.g., JSON, PDF, visualization).

Example Request:

{
  "task_id": "task_001",
  "delivery_format": "visualization"
}

6. Website Data Scraping (New)

API: Website Data Scraping

Description:
Allows dynamic data scraping from specified websites, supporting structured and unstructured data extraction.

Endpoint:
POST /api/web/scrape

Request Parameters:
	•	url (string, required): The website URL to scrape data from.
	•	selectors (object, optional): CSS or XPath selectors for extracting specific data.
	•	key (string): Name of the data field.
	•	selector (string): Path to locate the data.
	•	headers (object, optional): Custom request headers (e.g., proxy, user-agent).
	•	method (string, optional): HTTP method (default GET).
	•	payload (object, optional): Data to send for POST requests.
	•	format (string, optional): Response format (e.g., JSON, CSV, HTML).
	•	schedule (string, optional): Schedule for periodic scraping (e.g., every 24 hours).

Example Request:

{
  "url": "https://example.com/articles",
  "selectors": {
    "title": "h1.article-title",
    "content": "div.article-content",
    "author": "span.author-name",
    "published_date": "//time/@datetime"
  },
  "headers": {
    "User-Agent": "Mozilla/5.0"
  },
  "format": "JSON"
}

Example Response:

{
  "status": "success",
  "data": [
    {
      "title": "How to build an API",
      "content": "This is an example article.",
      "author": "John Doe",
      "published_date": "2025-01-20T12:00:00Z"
    }
  ],
  "metadata": {
    "request_time": "2025-01-20T12:01:00Z",
    "data_count": 1
  }
}

Key Advantages
	1.	Multi-Layer Privacy Protection:
Utilizes FHE, TEE, MPC, and Federated Learning for data security.
	2.	Dynamic and Flexible Data Management:
Supports vector databases, real-time updates, multi-modal data processing, and website scraping.
	3.	Enhanced Usability:
Features intuitive APIs, natural language parsing, and versatile result formats.

