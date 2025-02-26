# Code Bug Fixer

A web application that helps developers fix bugs in their code. The application uses the OpenAI API to analyze code errors and provide fixes along with explanations.

## Features

- Input your buggy code and error messages
- Receive fixed code suggestions
- Get detailed explanations of what went wrong and how it was fixed
- Clean, responsive user interface

## Technologies Used

- Python
- Flask
- OpenAI API
- HTML/CSS

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/code-bug-fixer.git
cd code-bug-fixer
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a configuration file:
Create a file named `config.py` with your OpenAI API key:
```python
OPENAI_API_KEY = "your_openai_api_key_here"
```

5. Run the application:
```bash
python app.py
```

6. Open your browser and navigate to http://127.0.0.1:5000/

## Usage

1. Enter your buggy code in the first text area
2. Enter the error message in the second text area
3. Click "Code Fix" to submit
4. View the fixed code and explanation in the right column

## Security Note

The `config.py` file containing your API key is excluded from version control in `.gitignore`. Make sure to keep your API keys secure.

## License

MIT

## Future Improvements

- Support for more programming languages
- Code syntax highlighting
- Save and share fixed code
- User authentication system 