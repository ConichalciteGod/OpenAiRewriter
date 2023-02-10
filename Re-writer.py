import tkinter as tk
import openai

# Initialize the API client with your API key
openai.api_key = "you_api_key_here"

# Define the function for rewriting text
def rewrite_text(text):
    text = text.strip()
    needs_quotes = " " in text or "\n" in text
    prompt = 'Rewrite the text: ' + (f'"{text}"' if needs_quotes else text)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"].strip()

# Use the function to rewrite a sample text
original_text = "The quick brown fox jumps over the lazy dog."
rewritten_text = rewrite_text(original_text)
print("Original Text:", original_text)
print("Rewritten Text:", rewritten_text)

root = tk.Tk()
root.title("Text Rewriter")

# Create a label for the original text
original_text_label = tk.Label(root, text="Original Text:")
original_text_label.pack()

# Create a text box for the original text
original_text_box = tk.Text(root, height=5, width=30)
original_text_box.pack()

# Create a button to rewrite the text
rewrite_button = tk.Button(root, text="Rewrite Text", command=lambda: rewrite_text_button_clicked())
rewrite_button.pack()

# Create a label for the rewritten text
rewritten_text_label = tk.Label(root, text="Rewritten Text:")
rewritten_text_label.pack()

# Create a text box for the rewritten text
rewritten_text_box = tk.Text(root, height=5, width=30)
rewritten_text_box.pack()

# Create a button to copy the rewritten text
copy_button = tk.Button(root, text="Copy Text", command=lambda: copy_text_button_clicked())
copy_button.pack()

# Function to handle the "Rewrite Text" button click
def rewrite_text_button_clicked():
    original_text = original_text_box.get("1.0", "end")
    rewritten_text = rewrite_text(original_text)
    rewritten_text_box.delete("1.0", "end")
    rewritten_text_box.insert("1.0", rewritten_text)

# Function to handle the "Copy Text" button click
def copy_text_button_clicked():
    rewritten_text = rewritten_text_box.get("1.0", "end")
    root.clipboard_clear()
    root.clipboard_append(rewritten_text)

# Start the GUI event loop
root.mainloop()
