import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification
import json

# Load model and config
model_path = "hiligaynon-ner-mbert-deploy"
model = AutoModelForTokenClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

with open(f"{model_path}/ner_config.json", 'r') as f:
    config = json.load(f)

def predict(text):
    """Predict entities in Hiligaynon text"""
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.argmax(outputs.logits, dim=-1)[0]
    
    tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
    
    entities = []
    current_entity = None
    
    for token, pred_id in zip(tokens, predictions):
        label = config['id_to_label'][str(pred_id.item())]
        
        if label.startswith('B-'):
            if current_entity:
                entities.append(current_entity)
            current_entity = {'tokens': [token], 'label': label[2:]}
        elif label.startswith('I-') and current_entity:
            current_entity['tokens'].append(token)
        else:
            if current_entity:
                entities.append(current_entity)
                current_entity = None
    
    if current_entity:
        entities.append(current_entity)
    
    # Clean up tokens
    for entity in entities:
        entity['text'] = tokenizer.convert_tokens_to_string(entity['tokens'])
    
    return entities

# Example usage
if __name__ == "__main__":
    text = "Si Maria kag si Juan nagkadto sa Manila."
    entities = predict(text)
    
    print(f"Text: {text}")
    print("Entities:")
    for entity in entities:
        print(f"  - {entity['text']} ({entity['label']})")
