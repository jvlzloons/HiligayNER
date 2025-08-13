from sklearn.metrics import cohen_kappa_score

def read_labels(file_path):
    """
    Read labels from a file where each line has a token and a label.
    """
    labels = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():  # skip empty lines
                parts = line.strip().split()
                if len(parts) == 2:
                    token, label = parts
                    labels.append(label)
    return labels

# Replace with your actual file paths
james_labels = read_labels("James - Dataset.json")
josh_labels = read_labels("Josh - Dataset.json")
rd_labels = read_labels("RD - Dataset.json")

# Sanity check
assert len(james_labels) == len(josh_labels) == len(rd_labels), "Label lengths do not match!"

# Compute Cohen’s κ scores
kappa_james_josh = cohen_kappa_score(james_labels, josh_labels)
kappa_james_rd = cohen_kappa_score(james_labels, rd_labels)
kappa_josh_rd = cohen_kappa_score(josh_labels, rd_labels)

# Print the results
print("Cohen’s κ Scores for Inter-Annotator Agreement:")
print(f"James – Josh: {kappa_james_josh:.4f}")
print(f"James – RD: {kappa_james_rd:.4f}")
print(f"Josh – RD: {kappa_josh_rd:.4f}")