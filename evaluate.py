from src import parse_arguments, load_config
import pandas as pd

def main():
    scores = []
    args = parse_arguments()
    config = load_config()

    model_path = args.model

    default_path = f"{config['file_path']}/{model_path.split('/')[1]}.jsonl"
    cot_path = f"{config['file_path']}/{model_path.split('/')[1]}-cot.jsonl"
    output_path = f"{config['file_path']}/{model_path.split('/')[1]}-acc.csv"
    
    df = pd.read_json(default_path,lines=True)
    df['target_answer'] = df.target_idx.apply(lambda x: ['A','B','C'][x])
    df['is_correct'] = [1 if f==t else 0 for f,t in df[['final_answer','target_answer']].values]

    for (lang,tgt),batch in df.groupby(['language','target']):
        scores.append(["default",lang,tgt,batch.is_correct.mean()])

    df = pd.read_json(cot_path,lines=True)
    df['target_answer'] = df.target_idx.apply(lambda x: ['A','B','C'][x])
    df['is_correct'] = [1 if f==t else 0 for f,t in df[['final_answer','target_answer']].values]

    for (lang,tgt),batch in df.groupby(['language','target']):
        scores.append(["CoT",lang,tgt,batch.is_correct.mean()])

    df = pd.DataFrame(scores,columns=['type','language','target','acc'])
    df.to_csv(output_path,index=False)

if __name__ == "__main__":
    main()