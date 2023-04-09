import json
import numpy as np
import pickle

def convert_to_json(data):

    def custom_serializer(obj):
        # Check if the object is a NumPy array
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        # Check if the object is a list of lists
        elif isinstance(obj, list) and len(obj) > 0 and isinstance(obj[0], list):
            return [custom_serializer(item) for item in obj]
        # Check if the object is a dictionary
        elif isinstance(obj, dict):
            # Define the structure of the dictionary
            return {'type': 'dict', 'data': {key: custom_serializer(value) for key, value in obj.items()}}
        # Raise a TypeError for any other data types
        raise TypeError('Object of type %s is not JSON serializable' % type(obj).__name__)

    # Convert the dictionary to JSON using the custom serializer
    json_string = json.dumps(data, default=custom_serializer)

    return json_string

def convert_to_json_from_path(file_path):
    with open(file_path, 'rb') as f:
        data = pickle.load(f)

    def custom_serializer(obj):

        
        # Check if the object is a NumPy array
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        # Check if the object is a list of lists
        elif isinstance(obj, list) and len(obj) > 0 and isinstance(obj[0], list):
            return [custom_serializer(item) for item in obj]
        # Check if the object is a dictionary
        elif isinstance(obj, dict):
            # Define the structure of the dictionary
            return {'type': 'dict', 'data': {key: custom_serializer(value) for key, value in obj.items()}}
        # Raise a TypeError for any other data types
        raise TypeError('Object of type %s is not JSON serializable' % type(obj).__name__)

    # Convert the dictionary to JSON using the custom serializer
    json_string = json.dumps(data, default=custom_serializer)

    return json_string


def parse_input(input_data):
    result = {
        "query": [
            {
                "text": input_data.text,
                "segs": input_data.segs,
                "asp_pol":[

                ],
                "segs_labels":{},
                "segs2idx": [],
                "asp_pol_idx": [],
            }
        ]
    }

    return result

if __name__ == "__main__":
    result = convert_to_json_from_path('sample.raw')
    print(result)
    
    # input_data = {
    #     "text": "The menu changed , portions were even smaller than before , a lentil dish was salty beyond edibility , a basmati rice dish lacked flavor .",
    #     "segs": ["The menu changed ,", "portions were even smaller than before ,", "a lentil dish was salty beyond edibility", ", a basmati rice dish lacked flavor ."]
    # }
    # parsed_data = parse_input(input_data)
    # print(parsed_data)
      