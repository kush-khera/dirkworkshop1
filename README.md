# Streamlit To-Do List Manager

A simple to-do list app built with Streamlit. Users can add tasks, mark them as complete, and delete them. Tasks persist in a local JSON file (`tasks.json`).

## Features
- **Add Tasks**: Quickly add new tasks with a single click.
- **Mark as Complete**: Strike through completed tasks for clarity.
- **Delete Tasks**: Remove tasks you no longer need.
- **Persistent Storage**: Data is saved to a simple JSON file, ensuring your tasks are there next time you open the app.

## Installation

1. **Clone this repository**:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Install required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**:
    ```bash
    streamlit run app.py
    ```

4. **Usage**:
    - Open the local URL provided by Streamlit (e.g., [http://localhost:8501](http://localhost:8501)).
    - Add, mark complete, or delete tasks as needed.

## Deploying on Streamlit Cloud

1. Push your code to a GitHub repository (already done if you cloned your own repo).
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Sign in using GitHub and **Create a new app**.
4. Select your repository, branch, and `app.py` as the entry point.
5. Click **Deploy**. Your to-do app will be online for the world to see!

## License
This project is licensed under the [MIT License](LICENSE).

## References
- [Streamlit Documentation](https://docs.streamlit.io/)
- [JSON in Python](https://docs.python.org/3/library/json.html)
- [Streamlit Cloud](https://share.streamlit.io/)

