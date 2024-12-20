import os 
import sqlite3
import platform
import shutil
import pandas as pd
import matplotlib.pyplot as plt

def get_chrome_history():
    if platform.system() == "Windows":
        db_path = os.path.join(os.getenv('LOCALAPPDATA'), 
                               r"Google\Chrome\User Data\Default\History")
    elif platform.system() == "Darwin":  # macOS
        db_path = os.path.expanduser(
            "~/Library/Application Support/Google/Chrome/Default/History"
        )
    else:  # Linux
        db_path = os.path.expanduser("~/.config/google-chrome/Default/History")

    temp_db = "temp_chrome_history.db"
    try:
        shutil.copyfile(db_path, temp_db)
    except Exception as e:
        print(f"Failed to copy history database: {e}")
        return None

    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls")
        rows = cursor.fetchall()
        conn.close()
        os.remove(temp_db)
        return rows
    except Exception as e:
        print(f"Failed to read history database: {e}")
        conn.close()
        os.remove(temp_db)
        return None

def process_data(history):
    # Convert raw data into a DataFrame
    df = pd.DataFrame(history, columns=["URL", "Title", "VisitCount", "LastVisitTime"])

    # Simplify URLs to domain names for analysis
    df['Domain'] = df['URL'].str.extract(r'(https?://(?:www\.)?([^/]+))')[1]

    # Convert "LastVisitTime" from Chrome's timestamp format to readable datetime
    df['LastVisitTime'] = pd.to_datetime(df['LastVisitTime'] / 1000000 - 11644473600, unit='s')

    return df

def visualize_data(df):
    # Top 20 most visited domains
    top_domains = df.groupby('Domain')['VisitCount'].sum().sort_values(ascending=False).head(20)

    plt.figure(figsize=(20, 6))
    bars = top_domains.plot(kind='bar', color='skyblue')
    plt.title('Top 20 Most Visited Domains', fontsize=16)
    plt.ylabel('Visit Count', fontsize=14)
    plt.xlabel('Domain', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=12)

    # Annotate bars with visit counts
    for bar in bars.patches:
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f'{int(bar.get_height())}',
            ha='center',
            va='bottom',
            fontsize=10,
            color='black'
        )

    plt.tight_layout()
    plt.savefig("top_domains.png")
    plt.show()

if __name__ == "__main__":
    history = get_chrome_history()
    if history:
        df = process_data(history)
        visualize_data(df)
    else:
        print("No history data retrieved.")
