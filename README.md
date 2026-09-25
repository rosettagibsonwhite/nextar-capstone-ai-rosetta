# AI Engineering Capstone

This repository contains three mini-projects completed as part of the AI Engineering Capstone:

1. Exploratory Data Analysis (EDA)
2. Retrieval-Augmented Generation (RAG)
3. YOLO Object Detection

Each project is contained in its own folder with the relevant code, data, dependencies, and sample outputs.

---

## Project Structure

```text
nextar-capstone-ai-YOURNAME/
│
├── README.md
├── eda/
├── rag/
└── yolo/
```

---

# 1. Exploratory Data Analysis (EDA)

## Beyond Discounts: Exploring Sales, Discounts and Profit in Retail

### Overview

This project uses exploratory data analysis (EDA) to investigate the relationship between sales, discounts, and profit in a retail dataset.

The goal is to identify patterns in profitability across product categories and discount levels and translate those findings into practical business recommendations.

### Business Question

**How are discounts related to profitability, and which product categories generate the most profit?**

The analysis explores:

- Which product categories generate the most sales and profit
- How discount levels relate to profit
- How many transactions result in a loss
- Differences between sales and profitability across categories
- Business decisions that can be informed by these findings

### Dataset

The dataset contains **9,994 retail transactions and 21 columns**, including:

- Orders and customers
- Product categories and sub-categories
- Sales
- Quantity
- Discounts
- Profit
- Geographic information
- Order and shipping dates

### Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Google Colab

### Methodology

The analysis followed these steps:

1. Loaded and inspected the dataset.
2. Examined the dataset structure and data types.
3. Checked for missing values.
4. Generated descriptive statistics.
5. Analyzed sales and profit across product categories.
6. Examined the relationship between discounts and profit.
7. Identified loss-making transactions.
8. Interpreted the findings and developed business recommendations.

### Key Findings

- Technology generated the highest total profit at approximately **$145,455**.
- Office Supplies generated approximately **$122,491** in profit.
- Furniture generated approximately **$742,000 in sales** but only approximately **$18,451 in profit**.
- Furniture had the highest average discount at approximately **17.4%**.
- Technology had the lowest average discount at approximately **13.2%**.
- Discount and profit had a correlation of approximately **-0.22**, indicating a weak negative relationship.
- Average profit became negative at higher discount levels, particularly around **30% discount and above**.
- **1,871 out of 9,994 transactions (18.72%)** were loss-making.

### Business Recommendations

- Review high discount levels, particularly discounts around 30% and above.
- Use targeted discounting rather than applying large discounts broadly.
- Investigate Furniture's pricing, costs, and discount strategy.
- Examine the factors contributing to Technology's strong profitability.
- Investigate products, sub-categories, and discount levels associated with losses.
- Consider profitability alongside sales volume when evaluating business performance.

### Conclusion

The analysis suggests that higher discount levels are associated with lower profitability, although discounting alone does not explain all differences in profit.

The results demonstrate how exploratory data analysis can help businesses identify patterns in sales and profitability and support more informed business decisions.

---

# 2. Retrieval-Augmented Generation (RAG)

## Overview

This project demonstrates a Retrieval-Augmented Generation (RAG) pipeline using a fictional company knowledge base.

The system loads company documents, splits them into smaller chunks, converts the chunks into vector embeddings, stores them in ChromaDB, retrieves relevant information for a question, and uses a local Llama 3.2 language model through Ollama to generate an answer based on the retrieved context.

### Technologies Used

- Python
- LangChain
- Hugging Face Sentence Transformers
- ChromaDB
- Ollama
- Llama 3.2 3B

### RAG Pipeline

The system follows these steps:

1. Load documents from the `documents` folder.
2. Split the documents into smaller chunks.
3. Generate vector embeddings using `all-MiniLM-L6-v2`.
4. Store the embeddings in ChromaDB.
5. Retrieve the most relevant document chunks for each question.
6. Pass the retrieved context to the local Llama 3.2 model.
7. Generate an answer based on the retrieved information.

### Sample Q&A

The system was tested using five questions covering:

- Employee annual leave
- Remote work policy
- NovaCloud storage capacity
- Standard working hours
- NovaNote supported platforms

The sample questions and generated answers are documented in:

`rag/sample_qa.md`

### Running the RAG Project

Navigate to the RAG directory:

```bash
cd rag
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Make sure Ollama is installed and download the required model:

```bash
ollama pull llama3.2:3b
```

Run the RAG system:

```bash
python main.py
```

The program loads the documents, creates embeddings, performs similarity search, and generates answers using the local Llama 3.2 model.

### Limitations

- The knowledge base contains only three small fictional documents.
- The information is intended for demonstration purposes.
- Answer quality depends on the retrieved context and language model.
- The system does not use external web search or live information.

---

# 3. YOLO Object Detection

## Overview

This project demonstrates object detection using the pretrained **YOLOv8n** model from Ultralytics.

The model was tested on a collection of sample images and evaluated using the COCO128 validation dataset.

### Model

- YOLOv8n
- Ultralytics
- Pretrained COCO model

### Detection Results

The model was tested on seven sample images and detected objects including:

- People
- Cars
- Motorcycles
- Bicycles
- Chairs
- Dogs
- Trucks

The annotated images are stored in:

`yolo/results/`

The detection summary is stored in:

`yolo/results_summary.csv`

### Evaluation Results

Evaluation on the COCO128 validation dataset produced:

| Metric | Result |
|---|---:|
| Precision | 63.9% |
| Recall | 53.6% |
| mAP@50 | 60.5% |
| mAP@50–95 | 44.5% |

### Running the YOLO Project

Navigate to the YOLO directory:

```bash
cd yolo
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

Run object detection on the sample images:

```bash
python main.py
```

To evaluate the model:

```bash
python evaluate.py
```

### Limitations

The model does not detect every object in an image.

For example, the penguins in one of the test images were not detected because the pretrained COCO model does not contain a dedicated penguin class.

Small, partially hidden, or unusual objects may also be missed.

The detection script uses a confidence threshold of **0.5**, meaning detections below 50% confidence are excluded.

---

# Conclusion

This capstone demonstrates three practical AI and data workflows:

- **EDA** for discovering patterns and relationships in a retail dataset.
- **RAG** for retrieving information from a custom knowledge base and generating grounded answers.
- **YOLO** for detecting objects in images using a pretrained computer vision model.

Together, these projects demonstrate practical experience with data analysis, natural language processing, vector search, large language models, and computer vision.
