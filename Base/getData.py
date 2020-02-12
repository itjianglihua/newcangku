import yaml,os
import base_dir


class GetData:
    def get_yaml_data(self,yaml_name):
        # with open("../Data" + os.sep + yaml_name, "r")as f:
        with open(base_dir.BASE_DIR+"./Data"+ os.sep + yaml_name, "r")as f:
            return yaml.safe_load(f)

