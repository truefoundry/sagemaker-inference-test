import argparse
import logging
from servicefoundry import Build, PythonBuild, Service, Resources, Port, LocalSource, DockerFileBuild

logging.basicConfig(level=logging.INFO)

image = Build(type="build", build_source=LocalSource(), build_spec=DockerFileBuild())

service = Service(
    name="test-sagemaker-service",
    image=image,
    ports=[
        Port(
            port=8080,
            expose=False
        )
    ],
    resources=Resources(
      memory_limit=500,
      memory_request=500,
      ephemeral_storage_limit=600,
      ephemeral_storage_request=600,
      cpu_limit=0.3,
      cpu_request=0.3
    ),
)
service.deploy(workspace_fqn='tfy-ctl-euwe1-devtest:shub-ws')