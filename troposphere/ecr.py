from troposphere import Join, Parameter, Output
from troposphere import Ref, Tags, Template
from troposphere.ec2 import SecurityGroup, SecurityGroupIngress
from troposphere.ecr import Repository
from troposphere.iam import InstanceProfile
from troposphere.iam import PolicyType
from troposphere.iam import Role

t = Template()

t.add_version("2010-09-09")
t.add_description("Stack that creates Elastic Container Registry")

appName = t.add_parameter(Parameter(
    "AppName",
    Type="String",
    Description="Name of the application",
))

ECRRepository = t.add_resource(Repository(
    "ECRRepository",
    RepositoryName=Ref(appName)
))

t.add_output(Output(
    "Registry",
    Value=Join(".", [Ref("AWS::AccountId"), "dkr.ecr", Ref("AWS::Region"), "amazonaws.com", ]),
    Description="Hostname of the registry")
)
t.add_output(Output(
    "Repository",
    Value=Join("/", [Join(".", [Ref("AWS::AccountId"), "dkr.ecr", Ref("AWS::Region"), "amazonaws.com", ]), Ref("ECRRepository")]),
    Description="Full name of the ECR Repository")
)

print(t.to_json())
