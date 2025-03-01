# Reinforcement Learning Agent for CartPole

## Overview
This project demonstrates a reinforcement learning (RL) agent trained to balance a pole on a cart (the classic CartPole environment). It uses [Stable-Baselines3](https://stable-baselines3.readthedocs.io/) for training, [OpenAI Gym](https://gym.openai.com/) as the environment, and includes tools for monitoring and evaluating the agent's performance. This project also highlights MLOps best practices by providing a Dockerfile for containerized deployment.

## Features
- **RL Training:** Train an RL agent on the CartPole-v1 environment using the PPO algorithm.
- **Evaluation:** Evaluate the trained agent's performance.
- **Model Saving/Loading:** Save the trained model for future inference or further training.
- **Interactive Notebook:** A Jupyter Notebook is provided to experiment with training parameters and visualize performance.
- **Containerization:** Dockerfile included for deployment.

## Project Structure
   ```
reinforcement-learning-agent/
├── README.md               # Overview, installation, usage, etc.
├── requirements.txt        # Required Python packages
├── Dockerfile              # Container configuration (optional)
├── agent.py                # Main code for training and evaluating the RL agent
└── notebooks/
    └── RL_Development.ipynb  # Notebook for interactive development and analysis
   ```

## Installation

**Clone the Repository:**

   ```
   git clone https://github.com/mda84/reinforcement-learning-agent.git
   cd reinforcement-learning-agent
   ```

Create and Activate a Virtual Environment:

   ```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

Install Dependencies:

   ```
pip install -r requirements.txt
   ```

## Usage
Training and Evaluating the Agent
Run the main script:
   ```
python agent.py
   ```

This will train an agent on the CartPole-v1 environment using PPO, save the trained model to models/cartpole_ppo.zip, and then evaluate its performance.

## Interactive Development
Open the notebook in the notebooks/ directory for interactive analysis and visualization:

   ```
jupyter notebook notebooks/RL_Development.ipynb
   ```

## Docker Deployment
To build and run the Docker container:
   ```
docker build -t rl-agent .
docker run -it rl-agent
   ```

## License
This project is licensed under the MIT License.

## Contact
For questions, collaboration, or contributions, please contact dorkhah9@gmail.com