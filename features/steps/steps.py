from behave import *
from twentyone import *

@given('un crupier')
def step_impl(context):
    context.crupier = Crupier()

@when('comienza la ronda')
def step_impl(context):
    context.crupier.nueva_ronda()

@then('el crupier toma dos cartas')
def step_impl(context):
    assert (len(context.crupier.mano) == 2)
