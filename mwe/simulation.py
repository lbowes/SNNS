from agent import Agent
from environment import Environment


def main() -> None:
    env = Environment()
    agent = Agent()

    obs = env.reset()

    for step in range(0, 100):
        act = agent.update(obs)
        obs = env.update(act)


if __name__ == '__main__':
    main()
