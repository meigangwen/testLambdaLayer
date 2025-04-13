from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_lambda_python_alpha as _alambda
)
from constructs import Construct

class TestLambdaLayerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Reference public Lambda Layer using ARN
        aws_sdk_pandas_layer = _lambda.LayerVersion.from_layer_version_arn(
            self,
            'AwsSdkPandasLayer',
            'arn:aws:lambda:ap-southeast-1:336392948345:layer:AWSSDKPandas-Python312:5'
        )

        initiator = _alambda.PythonFunction(
            self,
            "Main",
            entry="./lambda/",
            runtime=_lambda.Runtime.PYTHON_3_9,
            index='main.py',
            handler="handle",
            layers=[aws_sdk_pandas_layer],
            timeout=Duration.seconds(10)
        )
