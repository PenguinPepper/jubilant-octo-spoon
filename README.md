# Spaza Shop Stock Manager

A lightweight inventory dashboard for small shops. The application lets you upload a stock spreadsheet, identify products that have reached their low-stock threshold, review the complete inventory, and generate a simple PDF invoice for selected products.

## Features

- Upload stock data in CSV format.
- Upload Excel workbooks (`.xlsx`) when the required Excel reader is installed.
- Highlight products where `quantity` is less than or equal to `threshold`.
- Display low-stock items and the complete stock table in the browser.
- Select products for an invoice and enter a customer name.
- Generate and download a PDF invoice containing the selected products, prices, quantities, and total.

## Technology

- **Python**: Application runtime.
- **Streamlit**: Web interface and local application server.
- **pandas**: Loading and filtering CSV/Excel inventory data.
- **fpdf2**: Creating downloadable PDF invoices.

## Requirements

- Python 3.9 or newer is recommended.
- `pip` for installing Python packages.
- A modern web browser.

## Installation

1. Clone or download this project and open a terminal in its directory:

	```bash
	cd stock-manager
	```

2. Create a virtual environment:

	```bash
	python3 -m venv .venv
	```

3. Activate the virtual environment.

	On Linux or macOS:

	```bash
	source .venv/bin/activate
	```

	On Windows PowerShell:

	```powershell
	.venv\Scripts\Activate.ps1
	```

4. Install the project dependencies:

	```bash
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt
	```

	CSV files work with the listed dependencies. To enable `.xlsx` uploads, also install an Excel engine:

	```bash
	python -m pip install openpyxl
	```

## Running the application

Start the Streamlit server from the project directory:

```bash
streamlit run app.py
```

Streamlit will print a local address, normally `http://localhost:8501`. Open that address in a browser.

## Using the application

1. Click the upload control and choose a CSV or Excel stock file.
2. Review the **Low Stock Alert** table. A product is considered low in stock when its quantity is less than or equal to its threshold.
3. Review the **All Stock** table for the full uploaded inventory.
4. Enter a customer name.
5. Select one or more products in the invoice selector.
6. Click **Generate PDF Invoice**.
7. Download the generated `invoice.pdf` from the download button.

The included [sample_stock.csv](sample_stock.csv) is ready to use as a starting point.

## Stock file format

The uploaded file must contain these four columns:

| Column | Type | Description |
| --- | --- | --- |
| `item` | Text | Product name. |
| `quantity` | Number | Current quantity in stock. |
| `price` | Number | Price per item. |
| `threshold` | Number | Minimum quantity before the product is reported as low stock. |

Example:

```csv
item,quantity,price,threshold
Bread,5,18.5,10
Milk,2,25.0,8
Coke 500ml,30,15.0,12
```

Column names are case-sensitive. Prices are displayed in South African rand (`R`) in the invoice.

## Invoice calculation

For each selected product, the application uses the uploaded stock quantity as the invoice quantity:

```text
line total = quantity × price
invoice total = sum of all line totals
```

The current interface does not provide a separate quantity field for an invoice. Selecting a product therefore invoices its full uploaded quantity.

## Project structure

```text
.
├── app.py             # Streamlit application
├── requirements.txt   # Python dependencies
├── sample_stock.csv   # Example inventory file
└── README.md          # Project documentation
```