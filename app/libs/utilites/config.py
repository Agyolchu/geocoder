import yaml


class Config:

    @property
    def storage(self) -> dict:
        yml_file = open('etc/config.yml')
        return yaml.load(yml_file, Loader=yaml.FullLoader)
