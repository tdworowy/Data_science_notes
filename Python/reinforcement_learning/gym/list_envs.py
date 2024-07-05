from gym import envs
import retro
from retro import RetroEnv

envs = envs.registry.all()
print(len(envs))
for env in envs:
    print(env)
