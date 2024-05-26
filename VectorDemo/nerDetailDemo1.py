from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import torch

model_id='dslim/bert-base-NER'

access_token = "dYrzPElzVKpqMLMeowngodapvXuhPAjRpnpuqcyJyEJfoHbovUArMRaomQClzybLbBBaBMJjkUBWsuYMrDYgUfRCojPUOWusUJlWvmFKpccVDkUDoFrtpVlOjacOlxRR"

tokenizer_ner= AutoTokenizer.from_pretrained(model_id)
ner_model = AutoModelForTokenClassification.from_pretrained(model_id)

device= torch.cuda.current_device() if torch.cuda.is_available() else 'cpu'

nlp = pipeline('ner',model=ner_model, tokenizer=tokenizer_ner, aggregation_strategy='max',device=None, token=access_token)

res= nlp('My Name is Rajesh, I work as freelancer, from coimbatore, Tamilnadu, India')

print(res)
print("==================")