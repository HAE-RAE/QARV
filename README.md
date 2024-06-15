# QARV (Question and Answers with Regional Variance)
```EleutherAI Community Project```

The QARV (Question and Answers with Regional Variance) project aims to curate a collection of questions with answers that exhibit regional variations across different nations. 

## How to install.
```
git clone https://github.com/HAE-RAE/QARV.git
cd QARV
pip install -r requirements.txt
```

## How to run.
You can run evaluations as following:
``` python
python evaluate.py --model_name "Qwen/Qwen2-7B" --output_path "results"
```
To run multiple evaluations at once, update the list of models in this [script](scripts/eval.sh) and run:
``` python
./scripts/eval.sh
```
