# 🧾 FirmSync: Clio ⇄ QuickBooks Online Integration Toolkit

**FirmSync** is a Python-based integration toolkit designed to simulate and troubleshoot the sync between [Clio](https://www.clio.com) and [QuickBooks Online (QBO)](https://quickbooks.intuit.com/online/).  
This tool is currently focused on managing hard cost sync logic using QBO's API and sandbox environment.

---

## 🚀 Features

- 🔐 OAuth 2.0 Authentication with QBO (sandbox)
- 👤 Create Customers (Clio Contacts)
- 📁 Create Sub-Customers (Clio Matters)
- 💰 Create Expenses (Hard Costs)
- 🔍 Explore and query QBO data via Python SDK
- 🔁 Future: Map and push to Clio API

---

## 🛠 Project Structure
```
FirmSync/ 
        ├── .env # Secure credentials (not committed) 
        ├── README.md # You're here! 
        ├── requirements.txt 
        ├── firm_qbo/ 
        │ 
        ├── qbo_client.py # QuickBooks client setup 
        │ 
        ├── create_customer.py # Create a QBO Customer 
        │ 
        ├── create_subcustomer.py # Create a QBO Sub-Customer 
        │  ├── create_expense.py # Create a QBO Expense 
        │  └── query_expenses.py # (Coming soon) 
```

## 🔧 Setup Instructions

## 1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/FirmSync.git
cd FirmSync
```

## 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```
## 4. Configure .env
```env
CLIENT_ID=your_qbo_client_id
CLIENT_SECRET=your_qbo_client_secret
ACCESS_TOKEN=your_access_token
REFRESH_TOKEN=your_refresh_token
REALM_ID=your_realm_id
REDIRECT_URI=http://localhost:8000/callback
ENVIRONMENT=sandbox
```
## ✅ Run Test Scripts
```bash 
# Create a QBO Customer
python firm_qbo/create_customer.py

# Create a Sub-Customer (Matter)
python firm_qbo/create_subcustomer.py

# Create an Expense for the Matter
python firm_qbo/create_expense.py
```
## 🔮 Coming Soon
* 🔁 Clio API integration for syncing hard costs
* 🔍 Expense querying and mapping logic
* 🧪 Unit tests for sync workflows
* 📊 Sync status dashboard (optional)

## Author 
Travis Crawford

