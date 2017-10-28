from django.test import TestCase
import backInterface
# Create your tests here.
def test():
    a='www.baidu.com'
    b=backInterface.getLinkById("1")
    assert (a == b)