####  **python-collision-detection**
____________________________________
#####  make all classes inheritable to base class to enable collision detection

#####  Base class to contain all other classes

```python
class BaseClass(*classes):
    def __init__(self):
        self.instance = {}
        self.iTree = {}
        for className in classes:
            className.__init__(self)```


:smile:
