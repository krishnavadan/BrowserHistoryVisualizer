import os
import sqlite3
import platform
import shutil

def get_chrome_history():
    # Identify the OS and browser history file location
    if platform.system() == "Windows":
        db_path = os.path.join(os.getenv('LOCALAPPDATA'), 
                               r"Google\Chrome\User Data\Default\History")
    elif platform.system() == "Darwin":  # macOS
        db_path = os.path.expanduser(
            "~/Library/Application Support/Google/Chrome/Default/History"
        )
    else:  # Linux
        db_path = os.path.expanduser("~/.config/google-chrome/Default/History")

    # Create a temporary copy of the history database
    temp_db = "temp_chrome_history.db"
    try:
        shutil.copyfile(db_path, temp_db)
    except Exception as e:
        print(f"Failed to copy history database: {e}")
        return None

    # Connect to the copied database
    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()

    # Query browsing history
    try:
        cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls")
        rows = cursor.fetchall()
        conn.close()
        os.remove(temp_db)  # Remove the temporary database
        return rows
    except Exception as e:
        print(f"Failed to read history database: {e}")
        conn.close()
        os.remove(temp_db)
        return None

def save_history_to_file(history, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("URL, Title, Visit Count, Last Visit Time\n")
            for row in history:
                f.write(f"{row[0]}, {row[1]}, {row[2]}, {row[3]}\n")
        print(f"History saved to {file_path}")
    except Exception as e:
        print(f"Failed to save history to file: {e}")

if __name__ == "__main__":
    history = get_chrome_history()
    if history:
        save_history_to_file(history, "browser_history.csv")
    else:
        print("No history data retrieved.")

