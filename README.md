# gymutils
Tools for OpenAI gym.


## API
```
gymutils
├── Timer()
│   ├── reset()
│   └── get() -> str
├── action
│   └── get_random_action(action_space_n: int) -> int
├── env
│   ├── get_env_infos(env_name: str) -> dict
│   ├── get_all_env_names() -> list
│   ├── get_base_name(env_name: str) -> str
│   ├── get_a_obs(env_name: str, action=None: int, steps=None: int, return_env=False) -> numpy.ndarray
│   ├── ObsEnv(env_name: str, action=None: int, steps=None: int)
│   │   ├── reset(action=None: int, steps=None: int)
│   │   └── step(action=None: int, steps=None: int)
│   ├── info
│   │   ├── ENVS_INFOS
│   │   └── get_env_infos
│   ├── name
│   │   ├── SUFFIXES
│   │   ├── get_base_name
│   │   ├── get_all_env_names
│   │   └── get_all_env_ids() -> list
│   └── wrapper
│       ├── get_random_steps(max_steps: int) -> int
│       ├── step_obs(env: gym.Env, action: int) -> numpy.ndarray
│       ├── step(env: gym.Env, action=None: int, steps=None: int, only_obs=False) -> numpy.ndarray[, int, bool, dict]
│       ├── random_action_step(env: gym.Env, only_obs=False) -> numpy.ndarray[, int, bool, dict]
│       ├── random_step(env: gym.Env, action=None: int, only_obs=False) -> numpy.ndarray[, int, bool, dict]
│       ├── get_a_obs
│       └── ObsEnv
├── observation
│   ├── look(observation: numpy.ndarray)
│   ├── TrajectoryDrawer(env_name='Pong-v0', alpha=0.5)
│   │   ├── get_env_name() -> str
│   │   └── draw(observation: numpy.ndarray) -> numpy.ndarray
│   ├── Recorder(fps=15, size=(210, 160), path='.', out='out')
│   │   ├── record(observations: numpy.ndarray, cvt_color=True)
│   │   └── stop()
│   ├── save(observations: numpy.ndarray, path: str, name: str, prefix='', suffix='', ext='png')
│   ├── concat
│   │   ├── concat_horizontally(observations: list, margin_width=0) -> numpy.ndarray
│   │   ├── concat_table(observations_table: list, margin_width=0, margin_height=0) -> numpy.ndarray
│   │   └── concat_vertically(observations: list, margin_height=0) -> numpy.ndarray
│   ├── draw
│   │   └── TrajectoryDrawer
│   ├── pad
│   │   ├── pad_to_fit_the_width(observation1: numpy.ndarray, observation2: numpy.ndarray) -> numpy.ndarray, numpy.ndarray
│   │   └── pad_to_fit_the_height(observation1: numpy.ndarray, observation2: numpy.ndarray) -> numpy.ndarray, numpy.ndarray
│   └── view
│       ├── look
│       ├── Recorder
│       └── save
├── text_array
│   ├── TextArrayGenerator3D(canvas_size=None: tuple, font_size=1)
│   │   ├── reset(canvas_size=None: tuple, font_size=1)
│   │   └── generate(text: list) -> numpy.ndarray
│   ├── generator
│   │   ├── generate_string_array_3D(char_dict_3D: dict, string: str) -> numpy.ndarray
│   │   ├── generate_text_array_3D(char_dict_3D: dict, text: list, canvas_size=None: tuple) -> numpy.ndarray
│   │   └── TextArrayGenerator3D
│   └── loader
│       ├── get_char_list_from_file() -> list
│       ├── get_char_dict() -> dict
│       └── get_char_dict_3D(font_size=1) -> dict
└── time
    └── Timer
```


## Installation
```
git clone https://github.com/walkingmask/gymutils.git
cd gymutils && pip install -e .
```


## Requirements
- numpy
- opencv-python
- Pillow
- scikit-image >= 0.14


## Examples
### Look and save multiple observations
```
import gym
from gymutils.observation.concat import concat_horizontally
from gymutils.observation.view import look, save

env = gym.make('Pong-v0')
_ = env.reset()

obs1, _, _, _ = env.step(0)
obs2, _, _, _ = env.step(2)
obs3, _, _, _ = env.step(3)

observation = concat_horizontally([obs1, obs2, obs3], margin_height=5)
look(observation)
save(observation, './images/', 'result1')
```

![Result1](./images/result1.png)

### Attach text label to observation
```
from gymutils.observation.concat import concat_vertically
from gymutils.text_array import TextArrayGenerator3D

generator = TextArrayGenerator3D(canvas_size=(20, 160), font_size=2)

text_none = generator.generate(['None'])
text_up = generator.generate(['Up'])
text_down = generator.generate(['Down'])

obs_none = concat_vertically([obs1, text_none])
obs_up = concat_vertically([obs2, text_up])
obs_down = concat_vertically([obs3, text_down])

observation = concat_horizontally([obs_none, obs_up, obs_down], margin_width=3)
save(observation, './images/', 'result2')
```

![Result2](./images/result2.png)

### Record observations as video
```
from gymutils.observation.view import Recorder

recorder = Recorder(size=(230, 160), path='./images', out='result3')

done, _ = False, env.reset()
while not done:
    observation, _, done, _ = obs.step(2)
    text = generator.generate(["{:0.5f}".format(observation.mean())])
    observation = concat_vertically([observation, text])
    recorder.record(observation)

recorder.stop()
```

~~[result3](./images/result3.mov)~~

### Draw ball trajectory
```
from gymutils.observation import TrajectoryDrawer

_ = env.reset()
for _ in range(20): _ = env.step(0)

drawer = TrajectoryDrawer()

for _ in range(5):
    obs, _, _, _ = env.step(2)
    drawing = drawer.draw(obs)

save(drawing, './images', 'result4')
```

![Result4](./images/result4.png)
