import os
import datetime

def save_document(response_text: str, directory: str = "./output"):
    """Export tracel plan to Markdown file with proper formatting"""
    os.makedirs(directory, exist_ok=True)

    # Create markdown content with metadata header
    markdown_content = f"""# 🌍 AI Travel Plan
    
    # **Generated:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}
    #**Created by:** Atriyo's Travel Agent

    ---
    
    {response_text}
    
    ---
    *This travel plan was generated using AI and is intended for informational purposes only. Please verify all details before making any travel arrangements.*
    """

    try:
        # Write to markdown file with UTF-8 encoding
        # Generate timestamp-based filename
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
        filename = f"{directory}/AI_Travel_Plan_{timestamp}.md"

        print(filename)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(markdown_content)
        print(f"Travel plan saved successfully to {filename}")
        return filename
    except Exception as e:
        print(f"Error saving travel plan: {e}")
        return None
        