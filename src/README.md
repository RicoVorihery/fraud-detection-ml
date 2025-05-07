## 🛠️ Feature Engineering – Version 1

This script (`features.py`) performs the initial data transformation steps for the IEEE-CIS Fraud Detection project.

### Steps completed:
1. Loaded raw data files (`train_transaction.csv`, `train_identity.csv`)
2. Merged both datasets on `TransactionID`
3. Handled missing values:
   - Numeric columns → filled with `-999`
   - Categorical columns → filled with `"missing"`
4. Encoded categorical text columns using `LabelEncoder`
5. Saved the processed dataset to `data/processed/train_processed.csv`

### Execution command:

```bash
python src/features.py
