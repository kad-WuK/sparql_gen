#%%
from transformers import GPT2Tokenizer, TrainingArguments, Trainer, GPTNeoForCausalLM
from gen import subgraphgen
import spacy
import argparse

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




def parse_args():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", type=str, help="Your natural language question in English.")
    args = parser.parse_args()
    return args

def main(args):
    question = args.question
    #question = 'Show places of Eindhoven'
    subgraph = generate_description(question)
    test_question = 'Suppose we have a graph pattern:\n' + subgraph + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n'
    generated = tokenizer("<|startoftext|>"+test_question, return_tensors="pt").input_ids.cuda()
    sample_outputs = model.generate(generated, do_sample=True, top_k=2, 
                                max_length=1000, top_p=0.95, temperature=0.1, num_return_sequences=1)
    for i, sample_output in enumerate(sample_outputs):
        #print("{}".format(tokenizer.decode(sample_output, skip_special_tokens=True)))
        query = tokenizer.decode(sample_output, skip_special_tokens=True)[len(test_question)+len('<|startoftext|>'):]
        print(query)

if __name__ == "__main__":
    tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-125M", bos_token='<|startoftext|>',
                                          eos_token='<|endoftext|>', pad_token='<|pad|>')
    model = GPTNeoForCausalLM.from_pretrained("./pretrained/gpt-neo-125M").cuda()
    model.resize_token_embeddings(len(tokenizer))
    nlp = spacy.load("en_core_web_md")
    #text='Show all hotels and police stations in Eindhoven'
    entities = ['Administrative Area','Place','date Created','floor Size','geometry','Postal Address','Postal Code','Street Address','House','Building','Neighbourhood','Woonfunctie','Hotel','Mosque','Church','Castle','Museum','Police station','City Hall','Post office','Woonplaats','Name']
    #entities = ['Place','date Created','floor Size','geometry','Postal Address','Postal Code','Street Address','House','Building','Neighbourhood','Woonfunctie','Hotel','Mosque','Church','Castle','Museum','Police station','City Hall','Post office','Woonplaats','Name']
    s = subgraphgen()
    args = parse_args()
    main(args)