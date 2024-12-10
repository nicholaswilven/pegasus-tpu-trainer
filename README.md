# PEGASUS TPU Trainer
Model Card : [pegasus-indonesian-base_finetune](https://huggingface.co/thonyyy/pegasus-indonesian-base_finetune)
Report : [Draft Final Buku Tugas Akhir - Anthony 10119038 (1).pdf](https://github.com/user-attachments/files/18071465/Draft.Final.Buku.Tugas.Akhir.-.Anthony.10119038.1.pdf)
Reference Paper : [“PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization”](https://arxiv.org/abs/1912.08777)

In this project, I implemented Transformer encoder-decoder model (PEGASUS) pretraining and finetuning using Tensorflow + TFRecords on TPU. Weights for final model can be used to make abstractive summarization of Indonesian News. 

## Sample summarization
![image](https://github.com/user-attachments/assets/5cd1b721-232b-46a1-bf26-5788be91e172)

Pretrain dataset: 
1. [kaggle id news 2017](https://www.kaggle.com/datasets/aashari/indonesian-news-articles-published-at-2017)
2. [CC_news_id](https://github.com/Wikidepia/indonesian_datasets/tree/master/dump/cc-news)
3. [OSCAR_2201](https://huggingface.co/datasets/oscar-corpus/OSCAR-2201/viewer/id/train)

Finetune dataset: 
1. [Indosum](https://paperswithcode.com/dataset/indosum)
2. [Liputan6](https://paperswithcode.com/dataset/liputan6)
3. [XLSum](https://huggingface.co/datasets/csebuetnlp/xlsum)
   
## Performance

| datasets | rouge-1 | rouge-2 | rouge-L | BERTScore |
| ---- | ---- | ---- | ---- | --- |
| Indosum | 52.43 | 41.23 | 48.18 | 80.68 | 
| Liputan6 | 38.27 | 20.22 | 31.26 | 76.31 | 
| XLSum | 26.97 | 9.99 | 21.70 | 73.62|

## ⚡️ Getting Started
### Clone Repository
To start working on this project, clone `PEGASUS TPU Trainer` repository.
```
git clone https://github.com/nicholaswilven/pegasus-tpu-trainer.git
```
## Structure of this Repository
The structure of this project can be seen in the tree diagram below.
```
.
├── LICENSE
├── README.md
├── app.py
├── model
│   ├── evaluate.py
│   ├── generate_demo.py
│   ├── generate_iter.py
│   ├── trainer.py
│   └── utils
│       ├── cleaning.py
│       ├── convert_to_records.py
│       ├── gap_sentence_generation.py
│       ├── model_config.py
│       ├── parse_records.py
│       ├── process_xlsum.py
│       └── sentencepiece_tokenizer.py
├── notebook
│   ├── demo_pegasus.ipynb
│   └── preprocessing.ipynb
├── requirements.txt
├── script.sh
├── setup.py
├── tpu-test.py
└── train_tokenizer.py
```

### Environment Variables
There are various of Environment Variables contained in this project. Some credentials are not stored in this repository but expects a value.
We expect `.env` with values containing below
```
MODEL_MAX_LENGTH = 
MAX_SUMMARY_LENGTH = 
MIN_SUMMARY_LENGTH = 
GCS_BUCKET_NAME = 
PATH_TO_TOKENIZER = 
TOKENIZER_TYPE = 
SAMPLE_PER_FILE = 

GSG_RATE = 
RETURN_MASK_RATE = 

LOAD_CKPT_PATH = 
VOCAB_SIZE = 

REPO_NAME = 
```

## 📑 Usage Documentation
### Infrastructure setup
1. Create TPU VM on GCP (TF version 2.12.0, preferable v3-8, free access from [TRC](https://sites.research.google/trc/about/) program)
2. Create GCS buckets on GCP

### First time setup
1. pip install -r requirements.txt
2. python setup.py (Download ntlk data)
3. python tpu-test.py (Check TPU)

### Prepare training dataset
0. Preprocess all dataset on notebook (except OSCAR, XLSum)
1. Upload to GCS bucket as parquet file
2. Dump all text into one .txt file
3. Train sentencepiece tokenizer using train_tokenizer.py
4. Convert all training data to TFRecords using convert_to_records.py

### Training model
1. Specify model hyperparams on model_config.py, trainer.py args and .env
2. Run trainer.py

### Deploy mini showcase using FastAPI
1. Load model on demo.py (use checkpoint or huggingface repo)
2. Start server by `uvicorn app:app`

## Special Thanks
Research supported with Cloud TPUs from Google’s TPU Research Cloud (TRC)

 
