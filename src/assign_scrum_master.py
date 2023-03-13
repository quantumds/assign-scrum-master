import os
from pathlib import Path
import random

import yaml

# Define root folder of repo:
root_folder = Path(__file__).parents[1]

# Define route of 'properties' YAML file:
yaml_rel_route = "src/properties/properties.yaml"
# Read 'properties' YAML file:
with open(os.path.join(Path(root_folder), Path(yaml_rel_route))) as f:
    properties = yaml.load(f, Loader=yaml.BaseLoader)

# Print selected colleague to present:
print('\n' + "Python has decided that today's Scrum Master will be:" + '\n' + '\n' + random.choice(
    properties['todays_colleagues']))
