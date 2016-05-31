from behave import *
from twentyone import *

@given('un crupier')
def step_impl(context):
    context.crupier = Crupier()
