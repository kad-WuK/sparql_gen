
#%%
from gen import subgraphgen
import spacy
nlp = spacy.load("en_core_web_md")
#text='Show all hotels and police stations in Eindhoven'
entities = ['Administrative Area','Place','date Created','floor Size','geometry','Postal Address','Postal Code','Street Address','House','Building','Neighbourhood','Woonfunctie','Hotel','Mosque','Church','Castle','Museum','Police station','City Hall','Post office','Woonplaats','Name']
#entities = ['Place','date Created','floor Size','geometry','Postal Address','Postal Code','Street Address','House','Building','Neighbourhood','Woonfunctie','Hotel','Mosque','Church','Castle','Museum','Police station','City Hall','Post office','Woonplaats','Name']
s = subgraphgen()

def generate_description(question):
    #print(question)
    #question = qPattern.format(city)
    #print(question)
    surfaceDict = s.getSurface(question,nlp,entities)
    #print(surfaceDict)
    surfaceDict = s.merge_surfaces(surfaceDict)
    #print(surfaceDict)
    des = s.to_description(surfaceDict)
    return des


import pandas as pd
import torch
from torch.utils.data import Dataset, random_split
from transformers import GPT2Tokenizer, TrainingArguments, Trainer, GPTNeoForCausalLM

torch.manual_seed(42)
#model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B").cuda()

tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-125M", bos_token='<|startoftext|>',
                                          eos_token='<|endoftext|>', pad_token='<|pad|>')
model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M").cuda()
model.resize_token_embeddings(len(tokenizer))
#descriptions = pd.read_csv('netflix_titles.csv')['description']
descriptions = pd.read_csv('auto_gen.csv')['text']
max_length = max([len(tokenizer.encode(description)) for description in descriptions])


class NetflixDataset(Dataset):
    def __init__(self, txt_list, tokenizer, max_length):
        i = 0
        self.input_ids = []
        self.attn_masks = []
        self.labels = []
        for txt in txt_list:
            encodings_dict = tokenizer('<|startoftext|>' + txt + '<|endoftext|>', truncation=True,
                                       max_length=max_length, padding="max_length")
            self.input_ids.append(torch.tensor(encodings_dict['input_ids']))
            self.attn_masks.append(torch.tensor(encodings_dict['attention_mask']))
    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.attn_masks[idx]


dataset = NetflixDataset(descriptions, tokenizer, max_length=max_length)

train_size = int(0.9 * len(dataset))
train_dataset, val_dataset = random_split(dataset, [train_size, len(dataset) - train_size])
training_args = TrainingArguments(output_dir='./results', num_train_epochs=5, logging_steps=5000, save_steps=5000,
                                  per_device_train_batch_size=16, per_device_eval_batch_size=16,
                                  warmup_steps=100, weight_decay=0.01, logging_dir='./logs')
Trainer(model=model, args=training_args, train_dataset=train_dataset,
        eval_dataset=val_dataset, data_collator=lambda data: {'input_ids': torch.stack([f[0] for f in data]),
                                                              'attention_mask': torch.stack([f[1] for f in data]),
                                                              'labels': torch.stack([f[0] for f in data])}).train()
generated = tokenizer("<|startoftext|>", return_tensors="pt").input_ids.cuda()
sample_outputs = model.generate(generated, do_sample=True, top_k=50, 
                                max_length=1000, top_p=0.95, temperature=0.1, num_return_sequences=1)
for i, sample_output in enumerate(sample_outputs):
    print("{}: {}".format(i, tokenizer.decode(sample_output, skip_special_tokens=True)))


# %%
#subgraph = "('u_0',https://www.w3.org/1999/02/22-rdf-syntax-ns#type','https://schema.org/AdministrativeArea'), ('u_0','https://schema.org/containsPlace','u_1'), ('u_0','https://schema.org/geo','u_2'), ('u_0','https://schema.org/name','u_3'), ('u_1',https://www.w3.org/1999/02/22-rdf-syntax-ns#type','https://schema.org/place'), ('u_1',https://schema.org/address','u_4'), ('u_1',https://schema.org/containedInPalce','u_5'), ('u_1',https://schema.org/dataCreated','u_6'), ('u_1',https://schema.org/floorsize','u_7'), ('u_1',https://schema.org/Geo','u_8'), ('u_1',https://schema.org/name','u_9'), ('u_2',,https://www.w3.org/1999/02/22-rdf-syntax-ns#type','https://schema.org/GeoShape'), ('u_2',https://schema.org/polygon','u_10'), ('u_4','https://www.w3.org/1999/02/22-rdf-syntax-ns#type','https://schema.org/PostalAddress'), ('u_4',https://schema.org/addressCountry','u_11'), ('u_4',https://schema.org/addressLocality','u_12'), ('u_4',https://schema.org/name','u_13'), ('u_4',https://schema.org/postalCode','u_14'), ('u_4',https://schema.org/streetAddress','u_15')"
from gen import subgraphgen
import spacy
#subgraph = "PostalAddress"
question = 'Show places of administrative area that street address Victoriapark 611 is in.'
subgraph = generate_description(question)
#subgraph = 'Postal Address, PostalCode, Postal Code\nPlace, Address, Postal Address\nAdministrative Area, containsPlace, Place\n'
test_question = 'Suppose we have a graph pattern:\n' + subgraph + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n'



generated = tokenizer("<|startoftext|>"+test_question, return_tensors="pt").input_ids.cuda()
sample_outputs = model.generate(generated, do_sample=True, top_k=2, 
                                max_length=1000, top_p=0.95, temperature=0.1, num_return_sequences=1)
for i, sample_output in enumerate(sample_outputs):
    print("{}: {}".format(i, tokenizer.decode(sample_output, skip_special_tokens=True)))



