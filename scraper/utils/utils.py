import os  
import yaml
import pandas as pd
from typing import Dict, Any 
import plotly.graph_objs as go 
from wordcloud import WordCloud, STOPWORDS


CONFIG_PATH = os.path.join(os.getcwd(), 'config', 'config.yaml')

def read_config(config_path: str = CONFIG_PATH) -> Dict[str, Any]:
    """
    Reads and parses a YAML configuration file.

    Args:
        config_path (str): Path to the YAML configuration file. Defaults to CONFIG_PATH.

    Returns:
        Dict[str, Any]: Parsed configuration data as a dictionary.

    Raises:
        FileNotFoundError: If the configuration file does not exist.
        yaml.YAMLError: If there is an error parsing the YAML file.
    """
    try:
        with open(config_path) as file:
            content = yaml.safe_load(file)
        return content
    except FileNotFoundError as e:
        raise FileNotFoundError(f'The coniguration file at {config_path} does not exist.')
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f'Error parsing the yaml configuration file: {e}.')


