import os
import app

def test_add():
    assert app.add(2, 3) == 5

def test_environment():
    env = os.environ.get("Environment")
    print("Environment:", env)
    assert env is not None

def test_suite():
    suite = os.environ.get("TestSuite")
    print("Test Suite:", suite)
    assert suite == "regression"