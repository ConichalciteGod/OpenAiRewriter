import openai
import tkinter as tk

def get_api_key():
    # replace this with your OpenAI API key
    return "YOUR_API_KEY"

def rewrite_text(text, model):
    openai.api_key = get_api_key()
    completions = openai.Completion.create(
        engine=model,
        prompt=(f"rewrite {text}"),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message

def on_submit():
    text = text_box.get("1.0", "end-1c")
    option = model_var.get()
    new_text = rewrite_text(text, option)
    result_label.config(text=new_text)

root = tk.Tk()
root.title("Text Rewriter")

# Creating a frame to hold all the widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Creating a text box to enter the text
text_box = tk.Text(frame, height=10, width=50)
text_box.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Creating a label to show the selected model
model_label = tk.Label(frame, text="Select a model:")
model_label.grid(row=1, column=0, padx=10, pady=10)

# Creating a dropdown to select the model
model_var = tk.StringVar(value="text-davinci-002")
model_dropdown = tk.OptionMenu(frame, model_var, "text-davinci-002", "text-curie-001", "text-babbage-001", "text-bart-002")
model_dropdown.grid(row=1, column=1, padx=10, pady=10)

# Creating a button to submit the text and rewrite it
submit_button = tk.Button(frame, text="Rewrite", command=on_submit)
submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Creating a label to show the rewritten text
result_label = tk.Label(frame, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
