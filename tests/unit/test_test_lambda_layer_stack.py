import aws_cdk as core
import aws_cdk.assertions as assertions

from test_lambda_layer.test_lambda_layer_stack import TestLambdaLayerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in test_lambda_layer/test_lambda_layer_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TestLambdaLayerStack(app, "test-lambda-layer")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
