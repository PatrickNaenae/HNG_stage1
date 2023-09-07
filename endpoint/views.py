from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime

from .serializers import InfoSerializer

@api_view(['GET'])
def info_endpoint(request):
    data = {
        "slack_name": request.GET.get('slack_name'),
        "current_day": datetime.utcnow().strftime('%A'),
        "utc_time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": request.GET.get('track'),
        "github_file_url": "https://github.com/PatrickNaenae/HNG_stage1/blob/main/endpoint/views.py",
        "github_repo_url": "https://github.com/PatrickNaenae/HNG_stage1",
        "status_code": 200
    }

    serializer = InfoSerializer(data=data)
    serializer.is_valid()

    return Response(serializer.data)
