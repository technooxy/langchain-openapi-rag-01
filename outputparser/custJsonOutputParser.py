import json
from travelData import TravelData

class JsonOutputParser:
  """
  Custom parser to handle JSON output from an LLM for travel data.
  """
  def __init__(self, data_class=TravelData):
    self.data_class = data_class  # Class used to create data objects

  def parse(self, json_output: str) -> TravelData | None:
    """
    Parses JSON output and returns a TravelData object or None if parsing fails.
    """
    try:
      data = json.loads(json_output)
      # Assuming JSON has keys matching TravelData class attributes
      return self.data_class(data["destination"], data["date"], data["duration"],
                             data.get("additional_param1", None), data.get("additional_param2", False))
    except (json.JSONDecodeError, KeyError) as e:
      print(f"Error parsing JSON output: {e}")
      return None