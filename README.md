# 🤖 Agentic AI Projects

A collection of **Agentic AI and Generative AI projects** focused on building intelligent systems that can analyze information, reason over data, generate recommendations, and support real-world decision-making.

This repository currently includes an **AI-powered Smart Inventory Planning System** that demonstrates the integration of **Large Language Models (LLMs)** with a practical inventory management application.

---

## 🧠 Smart Inventory Planning System

### 📌 Overview

The **Smart Inventory Planning System** is an AI-powered inventory management application designed to analyze inventory information and generate intelligent planning recommendations.

The project combines:

- Inventory data
- Python-based application logic
- Flask web framework
- SQLite database
- Large Language Models
- AI-generated recommendations

The system supports both **offline and online LLM modes**, allowing users to experiment with local and cloud-based AI models.

### 🤖 Supported AI Models

The application supports two LLM modes:

| Mode | Technology | Purpose |
|---|---|---|
| 🖥️ Offline | Ollama + Mistral | Local AI processing |
| ☁️ Online | OpenAI GPT-3.5-Turbo | Cloud-based AI processing |

---

# 🎯 Problem Statement

Traditional inventory management often depends on spreadsheets, predefined rules, and manual analysis.

This can make it difficult to:

- Identify inventory problems quickly
- Analyze stock conditions
- Generate useful inventory recommendations
- Reduce manual analysis
- Support inventory planning decisions
- Convert raw inventory information into meaningful insights

The **Smart Inventory Planning System** addresses this problem by integrating AI and Large Language Models into the inventory planning workflow.

---

# 💡 Proposed Solution

The proposed system uses inventory information as input and combines traditional application logic with LLM-based processing to generate understandable inventory planning recommendations.

### Basic Workflow

```text
Inventory Data
      ↓
Data Processing
      ↓
Inventory Analysis
      ↓
AI / LLM Processing
      ↓
Recommendation Generation
      ↓
Inventory Planning Insights
✨ Key Features
📦 Inventory Analysis

The system processes inventory-related information and analyzes the available data to understand the current inventory situation.

🤖 Agentic AI Integration

The project demonstrates an AI-driven approach where an LLM is used to process information and generate recommendations instead of relying only on static rules.

🧠 Multiple LLM Modes

The system supports both local and online LLM processing.

🖥️ Offline LLM

Uses:

Ollama
   ↓
Mistral LLM
   ↓
AI Response
☁️ Online LLM

Uses:

Application
   ↓
OpenAI API
   ↓
GPT-3.5-Turbo
   ↓
AI Response
💡 AI-Powered Recommendations

The selected LLM processes the relevant inventory information and generates planning-oriented recommendations.

🌐 Web-Based Application

The project provides a web-based interface through which users can interact with the inventory planning system.

🗄️ Database Support

The application uses SQLite for storing application-related data.

🔄 Flexible AI Architecture

The system allows experimentation with:

Local LLMs
Cloud LLMs
Different AI processing approaches
🏗️ System Architecture
                    ┌─────────────────────┐
                    │      User / Admin   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Web Interface    │
                    │    HTML / CSS / JS  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Flask App      │
                    │   Backend / Logic   │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
           ┌─────────────────┐   ┌─────────────────┐
           │ SQLite Database │   │    AI / LLM     │
           └─────────────────┘   │      Layer      │
                                 └────────┬────────┘
                                          │
                              ┌───────────┴───────────┐
                              │                       │
                              ▼                       ▼
                    ┌─────────────────┐    ┌─────────────────┐
                    │ Ollama + Mistral│    │ OpenAI GPT-3.5  │
                    │   Offline LLM   │    │   Online LLM    │
                    └─────────────────┘    └─────────────────┘
🔄 Application Workflow
Step 1 — Inventory Input

The user provides the required inventory information to the application.

Step 2 — Data Processing

The Flask backend receives and processes the inventory information.

Step 3 — Inventory Analysis

The system analyzes the available inventory information.

Step 4 — Select AI Mode

The application can use either:

Offline → Ollama + Mistral

or:

Online → OpenAI GPT-3.5-Turbo
Step 5 — AI Processing

The selected LLM processes the relevant information.

Step 6 — Recommendation Generation

The AI generates inventory planning insights and recommendations.

Step 7 — User Review

The generated information is presented to the user through the application.

🛠️ Technology Stack
Programming Language
Python
Backend
Flask
Frontend
HTML
CSS
JavaScript
Database
SQLite
Artificial Intelligence / Generative AI
Large Language Models (LLMs)
Mistral
Ollama
OpenAI GPT-3.5-Turbo
Development Tools
Git
GitHub
Python Development Environment
🧩 Technologies at a Glance
Technology	Purpose
Python	Core application development
Flask	Backend and web framework
HTML	Web page structure
CSS	User interface styling
JavaScript	Frontend interaction
SQLite	Database management
Ollama	Local LLM execution
Mistral	Offline language model
OpenAI GPT-3.5-Turbo	Online language model
Git	Version control
GitHub	Repository management
🤖 LLM Architecture

The project supports two different ways of performing AI processing.

🖥️ Offline Mode — Ollama + Mistral

The offline configuration uses Ollama to run the Mistral language model locally.

User
  ↓
Web Application
  ↓
Flask Backend
  ↓
Ollama
  ↓
Mistral
  ↓
AI Response
  ↓
Web Application
Benefits
Local AI processing
Useful for experimentation
Reduced dependency on cloud APIs
Can work without sending prompts to a cloud LLM
Provides an alternative to online AI services
☁️ Online Mode — OpenAI GPT-3.5-Turbo

The online configuration uses the OpenAI API with GPT-3.5-Turbo.

User
  ↓
Web Application
  ↓
Flask Backend
  ↓
OpenAI API
  ↓
GPT-3.5-Turbo
  ↓
AI Response
  ↓
Web Application
Benefits
Cloud-based AI processing
API-based integration
Easy experimentation with hosted LLM capabilities
Alternative to locally running models
🧠 Agentic AI Concept

The project demonstrates an Agentic AI-oriented workflow for a practical business problem.

Instead of simply displaying inventory information, the system can use an LLM to process relevant information and generate useful planning-oriented responses.

The general concept is:

Input
  ↓
Understand Information
  ↓
Analyze Context
  ↓
LLM Reasoning
  ↓
Generate Recommendation
  ↓
User Decision Support

The project therefore demonstrates how Generative AI can be incorporated into a business application.

📂 Repository Structure
Agentic_AI_Projects/
│
├── Smart_Inventory_planning_System/
│
├── README.md
│
├── demo_of_prototype.mp4
│
├── Project Documentation/
│
└── Supporting Documents/
Main Components
Smart_Inventory_planning_System

Contains the main Smart Inventory Planning System project.

demo_of_prototype.mp4

Contains a demonstration of the project prototype.

Documentation Files

The repository also contains supporting project documentation and reports.

⚙️ Installation and Setup
1. Clone the Repository
git clone https://github.com/prakruthidevanga/Agentic_AI_Projects.git

Move into the repository:

cd Agentic_AI_Projects

Move into the main project:

cd Smart_Inventory_planning_System
🐍 2. Create a Virtual Environment

Creating a virtual environment is recommended.

Windows
python -m venv venv

Activate the environment:

venv\Scripts\activate
macOS / Linux
python3 -m venv venv

Activate:

source venv/bin/activate
📦 3. Install Dependencies

If the project contains a requirements.txt file:

pip install -r requirements.txt

If the dependency file is not present, install the required packages according to the imports used by the project.

🖥️ 4. Configure Ollama for Offline AI

To use the offline LLM mode, install Ollama on your system.

After installing Ollama, download the Mistral model:

ollama pull mistral

Make sure Ollama is running before starting the application.

The application can then communicate with the locally available Mistral model.

☁️ 5. Configure OpenAI

To use the online LLM mode, configure your OpenAI API key.

For example:

OPENAI_API_KEY=your_api_key

It is recommended to store API keys using environment variables rather than directly inside source code.

Example .env
OPENAI_API_KEY=your_api_key
Add .env to .gitignore
.env
venv/
__pycache__/

Never commit API keys or other sensitive credentials to GitHub.

▶️ 6. Run the Application

Start the Flask application using the project's Python entry file.

For example:

python app.py

The terminal will display the local server address.

A typical Flask development address is:

http://127.0.0.1:5000

Open the displayed address in your browser.

The exact entry-point filename depends on the project structure.

🧪 Example Usage

A typical application workflow is:

1. Open the web application
          ↓
2. Provide inventory information
          ↓
3. Select an AI processing mode
          ↓
4. Process inventory information
          ↓
5. AI analyzes the information
          ↓
6. Generate recommendations
          ↓
7. Review inventory planning insights
📊 AI Processing Flow
Inventory Information
        ↓
Data Processing
        ↓
Context Preparation
        ↓
Selected LLM
        ↓
AI Processing
        ↓
Generated Response
        ↓
Inventory Recommendation

The AI layer acts as an intelligent processing component that converts inventory-related information into understandable recommendations.

💼 Business Use Case

Inventory management is an important part of retail, e-commerce, manufacturing, warehousing, and supply-chain operations.

An AI-powered inventory planning system can assist users by:

Understanding inventory information
Identifying important inventory conditions
Generating planning-oriented recommendations
Reducing repetitive manual analysis
Supporting operational decision-making
📈 Potential Applications

The project concept can be extended to:

🛒 Retail stores
🛍️ E-commerce platforms
🏭 Manufacturing companies
📦 Warehouses
🚚 Supply-chain operations
🏪 Grocery stores
🏢 Distribution centers
🔐 Security Considerations

When using online LLM APIs:

Never expose API keys in source code
Use environment variables
Do not commit .env files
Do not share API credentials
Add sensitive files to .gitignore

Example:

.env
*.key
*.secret
venv/
__pycache__/
🧪 Testing and Experimentation

The project can be tested using both supported LLM modes.

Offline Testing
Application
    ↓
Ollama
    ↓
Mistral
    ↓
Generated Response
Online Testing
Application
    ↓
OpenAI API
    ↓
GPT-3.5-Turbo
    ↓
Generated Response

Testing both modes allows comparison of local and cloud-based LLM integration within the same application concept.

📚 Learning Outcomes

This project provides practical experience in:

Python

Using Python to develop an AI-powered application.

Flask

Building a backend web application and connecting application components.

SQLite

Managing application data using a lightweight relational database.

Generative AI

Understanding how Large Language Models can be integrated into real-world applications.

LLM Integration

Connecting applications with both local and cloud-based language models.

Ollama

Understanding how local LLMs can be executed and accessed through an application.

Mistral

Working with an open-source language model for local AI processing.

OpenAI API

Understanding API-based integration with a hosted language model.

AI Application Development

Combining web development, databases, and AI into one practical system.

🔮 Future Enhancements

The system can be further improved with:

📊 Machine Learning-based demand forecasting
📈 Sales trend prediction
📦 Automated reorder recommendations
🔔 Low-stock notifications
📉 Inventory trend dashboards
🧠 Advanced AI agents
🤖 Additional open-source LLMs
☁️ Additional cloud LLM providers
📊 Interactive analytics dashboards
🔐 User authentication
👥 Role-based access control
📱 Mobile-responsive interface
📤 Inventory report export
🗄️ Production database integration
🔄 Automated inventory monitoring
🚀 Future AI Architecture

A possible future architecture is:

                       User
                         │
                         ▼
                 Web Application
                         │
                         ▼
                Inventory Database
                         │
                         ▼
                 Data Processing
                         │
                         ▼
                  AI Agent / Planner
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
        Local LLM               Cloud LLM
      Ollama + Mistral       OpenAI / Other LLM
              │                     │
              └──────────┬──────────┘
                         ▼
                 AI Recommendation
                         │
                         ▼
                    Dashboard

🎥 Prototype Demonstration

A prototype demonstration video is included in the repository.

demo_of_prototype.mp4

The video demonstrates the working concept and interaction flow of the prototype.

🏆 Key Takeaway

The Smart Inventory Planning System demonstrates how Agentic AI and Large Language Models can be integrated with a web application to support inventory analysis and planning.

The project combines:

Business Problem
       +
Inventory Data
       +
Python
       +
Flask
       +
SQLite
       +
Large Language Models
       +
AI Recommendations
       ↓
Smart Inventory Planning System

👩‍💻 Author
Prakruthi BR

BCA — Artificial Intelligence & Machine Learning

Areas of Interest
Artificial Intelligence
Machine Learning
Generative AI
Data Analytics
Software Development
AI-Powered Applications


⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.
