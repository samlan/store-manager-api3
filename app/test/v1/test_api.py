import json
import os
import app
import pytest
from instance.config import app_config
from app import create_app

sales ={ 
    2:{'id':'2','prodname':'Iphone X','category':'mobile phones','price':'$1550','img':''},
    9:{'id':'9', 'prodname':'Google Pixel','category':'mobile phones','price':'$800','img':''},
    8:{'id':'8', 'prodname':'Macbook Pro','category':'laptop','price':'$1800','img':''},
    7:{'id':'7','prodname':'Lenovo Yoga','category':'laptop','price':'$690','img':''},
    3:{'id':'3','prodname':'LG TV','category':'flatscreen','price':'$550','img':''},
    1:{'id':'1', 'prodname':'Samsung TV','category':'flatscreen','price':'$450','img':''}
	}

products = {
     2:{'id':'2','prodname':'Iphone X','category':'mobile phones','price':'$1550','img':''},
    9:{'id':'9', 'prodname':'Google Pixel','category':'mobile phones','price':'$800','img':''},
    8:{'id':'8', 'prodname':'Macbook Pro','category':'laptop','price':'$1800','img':''},
    7:{'id':'7','prodname':'Lenovo Yoga','category':'laptop','price':'$690','img':''},
    3:{'id':'3','prodname':'LG TV','category':'flatscreen','price':'$550','img':''},
    1:{'id':'1', 'prodname':'Samsung TV','category':'flatscreen','price':'$450','img':''},
    12:{'id':'12','prodname':'Toshiba TV','category':'flatscreen','price':'$655','img':''},
    4:{'id':'4', 'prodname':'Sony TV','category':'flatscreen','price':'$800','img':''},
    5:{'id':'5', 'prodname':'Samsung S8','category':'mobile phone','price':'$1100','img':''},
    71:{'id':'71','prodname':'Iphone 7','category':'mobile phone','price':'$390','img':''},
    33:{'id':'33','prodname':'LG TV','category':'flatscreen','price':'$550','img':''},
    11:{'id':'11', 'prodname':'Samsung TV','category':'flatscreen','price':'$450','img':''}
		
}


@pytest.fixture
def client():
    flask_app = create_app('development')
    
    client = flask_app.test_client()
    yield client

def test_admin_view_all_products(client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/api/v1/products')
    assert response.status_code == 200
    
    
    

