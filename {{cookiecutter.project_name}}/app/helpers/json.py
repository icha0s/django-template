import json
from decimal import Decimal
from uuid import UUID


class CustomJSONEncoder(json.JSONEncoder):
    """Custom json encoder."""

    def default(self, obj):
        """Returns a serializable object."""
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)
