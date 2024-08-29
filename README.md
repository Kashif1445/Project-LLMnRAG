# Project LLMnRAG: Comparative Study of NLP Models and Retrieval-Augmented Generation (RAG) for Legal Document Analysis

## Project Overview

This project explores the development and evaluation of a chatbot designed to answer legal queries related to the Constitution of Pakistan. The study compares the performance of custom Natural Language Processing (NLP) models with a Retrieval-Augmented Generation (RAG) model. Given the specific nature and limited scope of the Constitution of Pakistan, which comprises only 280 pages, RAG emerges as a potentially superior solution, as traditional NLP models often struggle to produce high-quality results on limited data. The project implements and tests various deep learning architectures, including Artificial Neural Network (ANN), Long Short-Term Memory (LSTM), Gated Recurrent Unit (GRU), and Convolutional Neural Network (CNN), along with their enhanced versions for improved performance.

## Dataset

- **Name:** Pakistan Constitution Law Dataset
- **Description:** This dataset is a textual representation of the Constitution of Pakistan, consisting of 280 pages that include all the clauses and rules. It is openly available on the government website.
- **Format:** PDF
- **Download Link:** [Pakistan Constitution Law Dataset (PDF)](https://biblioteka.sejm.gov.pl/wp-content/uploads/2017/04/Pakistan_ang_010117.pdf)

## Project Structure

The project is divided into two main branches:

1. **Custom Deep Learning Models Branch** (`main-custom-deep-learning`)
   - This branch contains the implementation of various deep learning models, including ANN, LSTM, GRU, and CNN, as well as their enhanced versions. The models are trained on a dataset of question-answer pairs derived from the Constitution of Pakistan.
   
2. **Retrieval-Augmented Generation (RAG) Branch** (`RAG`)
   - This branch focuses on the implementation of a Retrieval-Augmented Generation (RAG) model. RAG combines retrieval-based methods with generative models, making it well-suited for handling specialized documents like the Constitution of Pakistan, where data is limited but context is critical.

## Cloning the Repository

To clone this repository, follow the instructions below:

### Clone the Deep Learning Branch

```bash
git clone -b main-custom-deep-learning --single-branch https://github.com/Kashif1445/Project-LLMnRAG
```
### Clone the RAG Branch

```bash
git clone -b RAG --single-branch https://github.com/Kashif1445/Project-LLMnRAG
```
## Installation and Setup

### Prerequisites

Ensure you have the following software installed on your system:

- Python 3.8+
- pip (Python package installer)
- Git

### Setting Up the Environment

1. **Clone the Repository**

   Choose the branch you want to work with (either `main-custom-deep-learning` or `RAG`) and clone it as instructed below.

2. **Navigate to the Project Directory**

   ```bash
   cd Project-LLMnRAG
   ```
### Create a Virtual Environment

It's recommended to create a virtual environment to manage your project dependencies.

```bash
python3 -m venv venv
```
### Activate the Virtual Environment

```bash
.\venv\Scripts\activate
### Install Dependencies

```bash
pip install -r requirements.txt
```
**##Test the code**
1. Now if you are in RAG branch, then run the following command 
```bash
python main.py
```
2. And if you are in Custom Deep Learning Models Branch, then run the **updated_deep_learning_testing.ipynb** file

