# TextSummarizer
NLP Project to handle text summarization. Takes a huge amount of data, and it can summarize and produce the meaning in variable length as need by the user.

Model Used: Pegasus Samsum Pretrained Model available from hugging face fine tuned on different dataset.
Tokenizer: Respective Tokenizer availabe from transformers library. 



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/stalker0418/TextSummarizer.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
python -m venv "Your environment name"
```

```bash
source "Your environment name"/scripts/activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
Default here: localhost:8080
```


# For Custom Data, Model and Tokenizer
If you want to train your model with your custom data, you can just change the data paths from config.yaml either by providing the source url or by downloading the zip file and providing that path in config.yaml for data extraction

The same way, if you want to change your model, or tokenizer, just approach config.yaml and update the values to your desired model names, and the workflow will be automatically be updated accordingly.