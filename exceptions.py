# file of custom exceptions

# raised when daily API query limit is reached
class RequestLimitReachedError(RuntimeError):
    def __init__(self):
        self.message = "Daily API query limit has been reached."

# raised when the user runs out of api calls and
# there are records that need to be geocoded
class PartialDataError(RuntimeError):
    def __init__(self, records, typeOfRecord):
        self.message = "{0} {1}s have been added to the database".format(records, typeOfRecord)
