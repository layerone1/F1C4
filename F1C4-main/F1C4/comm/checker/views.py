from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def custom_response(request):
    response = {

        "message" : {

                "header" : {
                    "machine" : "F1C4"
                },

                "body" : {
            
                },

                "footer" : {
            
                }

        }

    }
    return Response(response)
    