# SMART EMAIL WRITER 📧

SMART EMAIL WRITER is an AI-powered email reply generator built with **Streamlit** and **Google Gemini AI**. It helps users quickly create professional email responses with an appropriate subject line, tone, and structure.

## 🚀 Features

* Generate professional email replies instantly
* Creates a suitable email subject line
* Adjusts tone based on the email content
* Produces clear, concise, and professional responses
* Simple and user-friendly Streamlit interface
* Powered by Google Gemini 2.5 Flash

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Generative AI (Gemini API)

## 📂 Project Structure

```text
SMART-EMAIL-WRITER/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-email-writer.git
cd smart-email-writer
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit google-generativeai
```

## 🔑 Configure Gemini API Key

Replace the API key in your code with your own Gemini API key.

```python
genai.configure(api_key="YOUR_API_KEY")
```

**Important:** Never upload your actual API key to GitHub. Use environment variables or Streamlit secrets instead.

Example:

```python
import os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

## 📖 How It Works

1. Enter the email content or message that requires a reply.
2. Click the **Submit** button.
3. Gemini AI analyzes the content.
4. The application generates:

   * A suitable subject line
   * Professional email tone
   * Well-structured email response
5. Copy and use the generated email directly.

## 💡 Example

### Input

```text
Hi Team,

Could you please provide the project status update by tomorrow?

Thanks,
John
```

### Generated Output

**Subject:** Project Status Update

Dear John,

Thank you for your email.

I will prepare the project status update and share it with you by tomorrow as requested.

Please let me know if there are any specific details you would like included.

Best regards,
[Your Name]

## 🔒 Security Note

Do not hardcode API keys in public repositories. Use:

* Environment Variables
* Streamlit Secrets
* Configuration Files excluded from Git

## 🌟 Future Enhancements

* Multiple email tone options (Formal, Friendly, Professional)
* Email summarization
* Copy-to-clipboard functionality
* Download email as PDF
* Multi-language support
* Email templates

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository and submit pull requests for improvements.

## 📜 License

This project is licensed under the MIT License.

---

**Built with ❤️ using Streamlit and Google Gemini AI**

```
```
