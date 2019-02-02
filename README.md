# gymutils
Tools for OpenAI gym.


## Installation
```
git clone https://github.com/walkingmask/gymutils.git
cd gymutils && pip install -e .
```


## Usage
### Look and save multiple observations
```
import gym
from gymutils.observation.concat import concat_horizontally
from gymutils.observation.view import look, save

env = gym.make('Pong-v0')
_ = env.reset()

obs1, _, _, _ = env.step(0)
obs2, _, _, _ = env.step(0)
obs3, _, _, _ = env.step(0)

observation = concat_horizontally([obs1, obs2, obs3], margin_height=5)
look(observation)
save(observation, './images/', 'result1')
```

![Result1](./images/result1.png)

### Attach text label to observation
```
import gym
from gymutils.observation.concat import concat_horizontally, concat_vertically
from gymutils.text_array import TextArrayGenerator3D
from gymutils.observation.view import save

env = gym.make('Pong-v0')
_ = env.reset()

obs_none, _, _, _ = env.step(0)
obs_up, _, _, _ = env.step(2)
obs_down, _, _, _ = env.step(3)

generator = TextArrayGenerator3D(canvas_size=(20, 160), font_size=2)

text_none = generator.generate(['None'])
text_up = generator.generate(['Up'])
text_down = generator.generate(['Down'])

obs_none = concat_vertically([obs_none, text_none])
obs_up = concat_vertically([obs_up, text_up])
obs_down = concat_vertically([obs_down, text_down])

observation = concat_horizontally([obs_none, obs_up, obs_down], margin_width=3)
save(observation, './images/', 'result2')
```

![Result2](./images/result2.png)


## API
```
gymutils
├── observation
│   ├── concat
│   │   ├── concat_horizontally(observations, margin_width=0)
│   │   └── concat_vertically(observations, margin_height=0)
│   └── view
│       ├── look(observations)
│       └── save(observations, path, name, prefix='', suffix='', ext='png')
└── text_array
    └── TextArrayGenerator3D(canvas_size=None, font_size=1)
        ├── reset(canvas_size=None, font_size=1)
        └── generate(list_of_str)
```
