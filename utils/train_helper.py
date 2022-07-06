import numpy as np

def sigmoid_logits_to_one_hot(arr: np.array, thresh=0.5):
    arr[arr > thresh] = 1
    arr[arr <= thresh] = 0
    return arr.astype(int)


def one_hot_to_label(arr, label_col):
    temp = []
    for i in range(len(arr)):
        if arr[i] == 1:
            temp.append(label_col[i])
    return temp


# https://huggingface.co/docs/transformers/serialization#using-torchscript-in-python
def get_dummy_input(data, tokenizer, max_len, device):
    encoding = tokenizer.encode_plus(
        data,
        add_special_tokens=True,
        max_length=max_len,
        return_token_type_ids=False,
        padding='max_length',
        return_attention_mask=True,
        return_tensors='pt',
        truncation=True
    )

    return encoding['input_ids'].to(device), encoding['attention_mask'].to(device)
