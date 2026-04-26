import yaml

def generate_yaml(spec):
    node_version = spec.get("build", {}).get("runtime", "node@18").split("@")[1]
    install_cmd = spec.get("build", {}).get("install", "npm install")
    test_cmd = spec.get("test", {}).get("command", "npm test")

    workflow = {
        "name": "Generated Pipeline",
        "on": {
            "push": {"branches": ["main"]}
        },
        "jobs": {
            "build": {
                "runs-on": "ubuntu-latest",
                "steps": [
                    {"uses": "actions/checkout@v3"},
                    {
                        "uses": "actions/setup-node@v3",
                        "with": {"node-version": node_version}
                    },
                    {"run": install_cmd},
                    {"run": test_cmd}
                ]
            }
        }
    }

    return yaml.dump(workflow, sort_keys=False)
