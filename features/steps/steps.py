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



@given('una {mano}')
def step_impl(context, mano):
    context.crupier = Crupier()
    context.crupier.mano = mano.split(',')

@when('el crupier suma las cartas')
def step_impl(context):
    context.crupier_total = context.crupier.total_mano()

@then('el {total:d} es correcto')
def step_impl(context, total):
    assert (context.crupier_total == total)
