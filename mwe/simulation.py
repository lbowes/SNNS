from agent import Agent
from environment import Environment


def main() -> None:
    env = Environment()
    agent = Agent()

    # temp
    agent.draw()

    obs = env.reset()
    # temp
    env.draw()

    for step in range(0, 1):
        act = agent.update(obs)
        obs = env.update(act)


if __name__ == '__main__':
    main()
