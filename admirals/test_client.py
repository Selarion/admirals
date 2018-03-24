import json

import requests

request = {
            "name": "Category 1",
            "children": [
                {
                    "name": "Category 1.1",
                    "children": [
                        {
                            "name": "Category 1.1.1",
                            "children": [
                                {
                                    "name": "Category 1.1.1.1"
                                },
                                {
                                    "name": "Category 1.1.1.2"
                                },

                                {
                                    "name": "Category 1.1.1.3"
                                }
                            ]
                        },
                        {
                            "name": "Category 1.1.2",
                            "children": [
                                {
                                    "name": "Category 1.1.2.1"
                                },
                                {
                                    "name": "Category 1.1.2.2"
                                },
                                {
                                    "name": "Category 1.1.2.3"
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "Category 1.2",
                    "children": [
                        {
                            "name": "Category 1.2.1"
                        },
                        {
                            "name": "Category 1.2.2",
                            "children": [
                                {
                                    "name": "Category 1.2.2.1"
                                },
                                {
                                    "name": "Category 1.2.2.2"
                                }
                            ]
                        }
                    ]
                }
            ]
        }

r = requests.post("http://127.0.0.1:8000/categor/", data=json.dumps(request))
r = requests.post("http://127.0.0.1:8000/categor/15/")
print(r.status_code)
print(r.text)
