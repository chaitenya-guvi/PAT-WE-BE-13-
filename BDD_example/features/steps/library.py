from behave.api.pending_step import StepNotImplementedError
from behave import given, when, then


@given(u'Book details.')
def step_impl(context):
    print(u'Given Book details.')


@then(u'Verify book name.')
def step_impl(context):
    assert True


@given(u'Author details.')
def step_impl(context):
    print(u'Given Author details.')


@then(u'Verify author name.')
def step_impl(context):
    assert False