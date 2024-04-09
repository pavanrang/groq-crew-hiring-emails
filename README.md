# Cold Outreach with CrewAI and GROQ

This repository contains a Python-based solution for sending personalized cold outreach emails to a list of leads. The system leverages the powerful combination of CrewAI, a library for orchestrating AI tasks, and GROQ, a language model developed by Anthropic that offers exceptional performance and accessibility.

## Key Features

- **GROQ Language Model**: The project utilizes the GROQ language model, which is a large language model developed by Anthropic. GROQ is renowned for its speed and efficiency, making it an ideal choice for real-time applications like this email personalization system. Importantly, GROQ is freely available for use, providing a cost-effective solution for this project.

- **CrewAI Agents**: The project integrates the CrewAI library to orchestrate the email personalization and ghostwriting tasks. CrewAI enables the creation of "agents" and "tasks" that can be efficiently managed and executed in parallel, allowing for scalable and high-throughput processing of the email personalization and sending workflows.

- **Email Personalization**: The `EmailPersonalizationAgents` class creates an "Email Personalizer" agent that can customize a template email for each recipient based on their information (name, email, bio, last conversation).

- **Email Ghostwriting**: The `EmailPersonalizationAgents` class also creates a "Ghostwriter" agent that can revise the personalized email drafts to adopt a more informal, engaging, and sales-oriented tone, mirroring the desired communication style.

- **CSV-based Lead Data**: The script reads lead information from a CSV file and generates personalized email tasks for each lead, streamlining the data management process.

- **Email Sending**: The `mail.py` module handles the process of sending the personalized emails using a Gmail SMTP server, ensuring the delivery of the personalized outreach messages.

## Project Structure

- `main.py`: The main entry point of the application, where the email personalization and ghostwriting tasks are defined and executed.
- `mail.py`: Handles the process of sending the personalized emails using a Gmail SMTP server.
- `tasks.py`: Defines the `PersonalizeEmailTask` and `GhostwriteEmailTask` classes, which encapsulate the email personalization and ghostwriting logic.
- `agents.py`: Defines the `EmailPersonalizationAgents` class, which creates the "Email Personalizer" and "Ghostwriter" agents.
- `pyproject.toml`: The Poetry configuration file, which manages the project dependencies.

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your-username/cold-outreach-crewai.git
```

2. Install the required dependencies using Poetry:

```bash
cd cold-outreach-crewai
poetry install
```

3. Create a `.env` file in the root directory of the project and add your Anthropic GROQ API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

4. Update the `email_template` variable in the `main.py` file with your desired email template.
5. Ensure the `csv_file_path` variable in the `main.py` file points to the correct CSV file containing your lead data.
6. Run the `main.py` script to generate the personalized email drafts and send them:

```bash
poetry run python main.py
```

The personalized email drafts will be saved in the `output/` directory, and the emails will be sent to the corresponding recipients.

## Contributing

If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
