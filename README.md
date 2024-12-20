# Browser History Visualizer

## Overview
The **Browser History Visualizer** is a Python-based tool that analyzes your browsing habits by extracting and visualizing your top 20 most visited websites. This tool demonstrates how to combine **Python**, **Data Analysis**, and **Data Visualization** to derive insights from local browser data.

## Features
- Extracts history from Google Chrome.
- Analyzes visit counts to identify your top 20 most visited websites.
- Visualizes the data using bar charts, including annotations for visit counts on the bars.

## Privacy and Security
- **Local Processing**: All data is processed entirely on your local machine.
- **No Data Sharing**: The tool does not upload or share your browser history.

## Notes
- This tool is tested for the **default installation path** of Google Chrome on **Windows**.
- If your Chrome browser is installed in a non-default location, you may need to modify the script to specify the correct path to the `History` database file.

## Requirements
To use this tool, ensure you have the following:

- **Python 3.8+**
- Required Python libraries (install via `requirements.txt`):
  - `pandas`
  - `matplotlib`
  - `sqlite3` (built into Python)
  - `os` and `shutil` (built into Python)

## Installation
### Step 1: Clone the Repository
```bash
git clone <repository_url>
cd browser-history-visualizer
```

### Step 2: Set Up the Environment
Install the required dependencies using the following command:
```bash
pip install -r requirements.txt
```

### Step 3: Verify the Chrome History Path
Ensure that the script points to the correct Chrome history database file. By default, the script assumes the Windows path:
```
C:\Users\<YourUsername>\AppData\Local\Google\Chrome\User Data\Default\History
```
If Chrome is installed elsewhere, update the file path in the script.

## Get Started
1. Run the script:
   ```bash
   python browser_history_visualizer.py
   ```
2. The tool will generate:
   - A CSV file (`top_20_sites.csv`) containing the top 20 websites.
   - A bar chart visualization of your most visited websites with annotated visit counts.

3. Open the generated chart to explore your browsing habits!

## Example Output
- **CSV Output**:
  ```csv
  Rank,Website,Visit Count
  1,example.com,150
  2,anotherexample.com,120
  ...
  ```
- **Visualization**:
  A bar chart displaying the top 20 most visited sites with visit counts shown on the bars.

## Customization
You can modify the script to:
- Support other browsers by changing the database file path.
- Extend the analysis to include time-based trends.

## Contributions
Feel free to fork the repository and submit pull requests for improvements or additional features.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Disclaimer
This tool is for personal use and educational purposes only. Use responsibly and ensure compliance with local privacy laws.
