import gym
import os
import numpy as np
import torch
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

def train_agent(env_id="CartPole-v1", total_timesteps=100000, model_path="models/cartpole_ppo.zip"):
    # Create environment
    env = gym.make(env_id)

    # Create PPO model
    model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./ppo_cartpole_tensorboard/")

    # Train the agent
    model.learn(total_timesteps=total_timesteps)

    # Save the trained model
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    model.save(model_path)
    print(f"Model saved to {model_path}")
    return model, env

def evaluate_agent(model, env, n_eval_episodes=10):
    mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=n_eval_episodes)
    print(f"Evaluated over {n_eval_episodes} episodes: mean reward = {mean_reward:.2f} +/- {std_reward:.2f}")
    return mean_reward, std_reward

if __name__ == "__main__":
    # Train the agent
    model, env = train_agent(total_timesteps=50000)

    # Evaluate the trained agent
    evaluate_agent(model, env)

    # Demonstrate agent performance by running one episode
    obs = env.reset()
    done = False
    total_reward = 0
    while not done:
        action, _states = model.predict(obs)
        obs, reward, done, info = env.step(action)
        total_reward += reward
        env.render()
    env.close()
    print(f"Total reward in demo episode: {total_reward}")
