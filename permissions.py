import yaml

class Permissions():

    def parseYML(self, path):
        # Create the full path including the workspace prefiox
        with open(path, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        
        return ""

