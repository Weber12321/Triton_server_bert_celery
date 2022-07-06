from torch.utils.data import DataLoader

from data_set.dataset_class import AudienceDataset


def create_data_loader(df, tokenizer, max_len, batch_size):
    ds = AudienceDataset(
        reviews=df.text.to_numpy(),
        targets=df.labels.to_numpy(),
        tokenizer=tokenizer,
        max_len=max_len
        )
    return DataLoader(
        ds,
        batch_size=batch_size,
        num_workers=0,
        shuffle=True,
        )
